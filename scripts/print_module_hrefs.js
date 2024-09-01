// script for extracting unique module hrefs from 'https://moseskonto.tu-berlin.de/moses/modultransfersystem/studiengaenge/anzeigen.html?studiengang=179&mkg=24541&semester=73' via a semi automated workflow.


// IMPORTANT: It is intended that the following class is pasted into dev tools console.
// IMPORTANT: Further bugs can arise if the css selectors are outdated.

class Extractor {
	constructor() {
		this.hrefs = new Set();
	}

	// adds all links from the currently selected program course section
	extract_links() {
		let modules_elem = document.querySelector("#j_idt43\\:studiengangsbereich");
		let module_elems = Array.from(
			document.querySelectorAll("#j_idt43\\:j_idt158_data > tr > td:nth-child(1) > a")
		);
		module_elems.forEach(elem => this.hrefs.add(elem.href));
		console.log('totally extracted links:' + this.hrefs.size);
	}	

	// returns a list of unique module hrefs 
	get_hrefs() {
		return [...this.hrefs];
	}
}


