# file: json []{.module_title, .module_requirements}
# stdin: user input for translating requirements into edges, eg. a;b;c  means a has edges to b and c
# stdout: adjacency list of modules

# 'jq '[.[] | {title:.module_title, requirements:.module_requirements}]' modules_24_8_30.json'

import sys
import json

def main(_, json_file: str, output_file: str):
    with open(json_file, 'r') as f:
        modules = json.loads(f)

    with
    for module in modules:
        title = module['module_title']
        requirements = module['module_requirements']
        print(f"-- {module} --")
        print(requirements)
        print()
        source, neighbours = input("> ").split(';')



if __name__ == '__main__':
    main(*sys.argv)
