class mead_card extends HTMLElement {
  connectedCallback() {

    const type = this.getAttribute("type") || "traditional";
    const name = this.getAttribute("name") || "blank";
    this.innerHTML = `
		<div class="card ${type}"> 
			<h1>${name}</h1>
			<p> this is the cards information</p>
		</div>
    `;
  }
}
customElements.define("mead-card", mead_card);

console.log("js loaded ")