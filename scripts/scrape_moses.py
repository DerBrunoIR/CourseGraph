# This scripts reads module hrefs from stdin and writes module information (from moses) as json to stdout.


from bs4 import BeautifulSoup
import sys
from playwright.async_api import async_playwright, Page, BrowserContext
import asyncio
import itertools as it
from collections import defaultdict
import time
import json
import functools


ERROR_RETRY = 300
ERROR_FAIL = 400
ERROR_RATELIMTED = 301
SUCCESS = 200

@functools.total_ordering
class StatusCode:
    def __init__(self, code: int, msg: str=None):
        self.code = code
        self.msg = msg
    
    def code() -> int:
        return self.code
    
    def msg() -> str:
        return self.msg

    def __add__(self, other):
        assert isinstance(other, self.__class__), f"{other}, {type(other)}, {self.__class__}"
        if self.code > other.code:
            return self
        else:
            return other

    def __eq__(self, other):
        match other:
            case int(x):
                return self.code == x
            case StatusCode(code):
                return self.code == code
            case _:
                raise TypeError("expected either 'int' or 'StatusCode'")

    def __lt__(self, other):
        match other:
            case int(x):
                return self.code < x
            case StatusCode(code):
                return self.code < code
            case _:
                raise TypeError("expected either 'int' or 'StatusCode'")


class ModulePageRequest:
    def __init__(self, ctx, url):
        self.url = url
        self.ctx = ctx

    async def request_html(self) -> int:
        page = await self.ctx.new_page()
        await page.goto(self.url, wait_until='networkidle')
        await asyncio.sleep(1)
        content = await page.content()

        # check if redirected
        # #j_idt47\:j_idt72 > div.alert-text-with-icon > a
        redirect_elem = await page.query_selector('#j_idt48\\:j_idt73 > div.alert-text-with-icon > a')
        if redirect_elem:
            new_url = await redirect_elem.get_attribute('href')
            print(f"redirected to {self.url} from {new_url}\n", file=sys.stderr)
            self.url = new_url
            await page.goto(self.url, wait_until='networkidle')
            await asyncio.sleep(1)
        
        # check if outdated
        outdated_elem = await page.query_selector('#j_idt48\\:j_idt73 > div.alert-text-with-icon > p > strong')
        if outdated_elem:
            await page.close()
            return StatusCode(ERROR_FAIL, f'content is outdated')


        # scrape data
        module_page = ModulePage(self.url)
        try:
            # text elements
            await module_page.add_inner_text(page, 'module_requirements', '#j_idt48 > div:nth-child(9) > div > div > div > div:nth-child(2)')
            await module_page.add_inner_text(page, 'module_title', '#page-title > h1')
            await module_page.add_inner_text(page, 'module_content', '#j_idt48 > div:nth-child(5) > div > div > div')
            await module_page.add_inner_text(page, 'module_learning_outcomes', '#j_idt48 > div:nth-child(4) > div > div')
            await module_page.add_inner_text(page, 'module_max_num_participants', '#j_idt48 > div:nth-child(12) > div > div > div')
            await module_page.add_inner_text(page, 'module_duration', '#j_idt48 > div:nth-child(11) > div > div')
            await module_page.add_inner_text(page, 'module_registration_procedure', '#j_idt48 > div:nth-child(13) > div > div')
            await module_page.add_inner_text(page, 'module_teching_methods', '#j_idt48 > div:nth-child(8) > div > div')
            await module_page.add_inner_text(page, 'module_mandatory_parts', '#j_idt48 > div:nth-child(9) > div > div > div > div:nth-child(3)')
            await module_page.add_inner_text(page, 'module_exam_type', '#j_idt48 > div.row.equal > div.col-xs-12.col-md-6 > div > div:nth-child(3) > div:nth-child(4) > div')
            await module_page.add_inner_text(page, 'module_credits', '#j_idt48 > div.row.equal > div.col-xs-12.col-md-6 > div > div:nth-child(3) > div:nth-child(1) > div')
            await module_page.add_inner_text(page, 'module_id', '#j_idt48 > div.row.equal > div.col-xs-12.col-md-6 > div > div:nth-child(1) > div:nth-child(1)')
            await module_page.add_inner_text(page, 'module_responsible_person', '#j_idt48 > div.row.equal > div.col-xs-12.col-md-6 > div > div:nth-child(3) > div:nth-child(2) > div')
            await module_page.add_inner_text(page, 'module_faculty', '#j_idt48 > div.row.equal > div:nth-child(2) > div > div > div:nth-child(2)')
            await module_page.add_inner_text(page, 'module_institute', '#j_idt48 > div.row.equal > div:nth-child(2) > div > div > div:nth-child(3) > div')
            await module_page.add_inner_text(page, 'module_validity', '#j_idt48 > div.row.equal > div.col-xs-12.col-md-6 > div > div:nth-child(1) > div:nth-child(2) > div')
            await module_page.add_inner_text(page, 'module_default_language', '#j_idt48 > div.row.equal > div.col-xs-12.col-md-6 > div > div:nth-child(1) > div:nth-child(3) > div')
            await module_page.add_inner_text(page, 'module_is_graded','#j_idt48 > div.row.equal > div.col-xs-12.col-md-6 > div > div:nth-child(3) > div:nth-child(3) > div')
            # html tables
            await module_page.add_inner_html(page, 'module_related_programs', '#j_idt48\\:j_idt409 > div')
            await module_page.add_inner_html(page, 'module_recommended_literature', '#j_idt48\\:j_idt395 > div')
            await module_page.add_inner_html(page, 'module_workload_table', '#j_idt48\\:j_idt228\\:0\\:j_idt233 > div')
        except Exception as e:
            await page.close()
            return StatusCode(ERROR_RETRY, f'failed to scrape data from page: \n{e}')

        self.module_page = module_page
        await page.close()
        return StatusCode(SUCCESS)
    

class ModulePage:
    data: dict[str,str]

    def __init__(self, url):
        self.data = {'module_url': url}

    async def add(self, page: Page, attr_name: str, elem_func: callable, selector: str):
        elem = await page.query_selector(selector)
        if elem is None:
            raise Exception(f"could not locate attribtue '{attr_name}'\ncss selector '{selector}')")
        self.data[attr_name] = await elem_func(elem)

    async def add_inner_text(self, page: Page, attr_name: str, selector: str):
        return await self.add(page, attr_name, lambda elem: elem.inner_text(), selector)

    async def add_inner_html(self, page: Page, attr_name: str, selector: str):
        return await self.add(page, attr_name, lambda elem: elem.inner_html(), selector)

    async def add_contains_text(self, page: Page, attr_name: str, text: str, selector: str):
        async def handler(elem):
            elem_text = await elem.inner_text()
            return text in elem_text

        return await self.add(page, attr_name, handler, selector)

    def data(self):
        return self.data


class RequestScheduler:
    def __init__(self, tasks: list[ModulePageRequest]):
        self.tasks = tasks
        self.finished = []
        self.failed = []
        self.max_retires = 3
        self.batchsize = 4
        self.batch_delay_secs = 2
        self.ratelimite_delay_secs = 20
        self.retry_counts = defaultdict(lambda: 0)

    async def run(self):
        while len(self.tasks) > 0:
            print(f"{len(self.tasks)} tasks left\n", file=sys.stderr)
            selection = self.tasks[:self.batchsize]
            self.tasks = self.tasks[self.batchsize:]

            async def run_task(idx: int, task: ModulePageRequest):
                await asyncio.sleep(idx)
                status = await task.request_html()
                print(f"{status.code} {status.msg}\n{task.url}\n", file=sys.stderr)
                if status >= ERROR_FAIL:
                    self.failed.append(task)
                elif status >= ERROR_RETRY:
                    print(f"we got probably ratelimited, sleeping {self.ratelimite_delay_secs}s\n", file=sys.stderr)
                    time.sleep(self.ratelimite_delay_secs) # we got probably ratelimited
                    if self.retry_counts[task] < self.max_retires:  
                        self.tasks.insert(0, task)
                        self.retry_counts[task] += 1
                    else:
                        print(f"droppping {task.url}\n", file=sys.stderr)
                        self.failed.append(task)
                else:
                    assert status == SUCCESS
                    self.finished.append(task)

            runnable_tasks = [run_task(i, task) for i, task in enumerate(selection)]
            await asyncio.gather(*runnable_tasks)
            await asyncio.sleep(self.batch_delay_secs)

        return 


async def main_loop(module_hrefs):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()

        requests = [ModulePageRequest(context, href) for href in module_hrefs] 
        n = len(requests)
        scheduler = RequestScheduler(requests)
        await scheduler.run()
        await browser.close()

        finished = scheduler.finished
        failed = scheduler.failed

        if len(failed) > 0:
            print("list of failed urls:", file=sys.stderr)
            for task in failed:
                print(f"{task.url}", file=sys.stderr)
            print(f"{len(failed)}/{n} failed", file=sys.stderr)

        modules = [task.module_page.data for task in finished]
        print(json.dumps(modules, indent=4))



def main():
    urls = sys.stdin.readlines()
    urls = map(lambda line: line.strip(), urls)
    urls = filter(lambda line: bool(line), urls)
    urls = list(urls)
    asyncio.run(main_loop(urls))


if __name__ == '__main__':
    main()