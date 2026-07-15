class MeadCard extends HTMLElement {
    connectedCallback() {

        const type = this.getAttribute("type") || "";
        const name = this.getAttribute("name") || "Blank";
        const icon = this.getAttribute("icon") || "";
        const dialog = this.getAttribute("dialog") || "";

        if(icon == ""){
            this.innerHTML = `
            <div class="card ${type}">

                <h1>${name}</h1>

                <p>${dialog}</p>
            </div>
        `;
        }
        else{
            this.innerHTML = `
            <div class="card ${type}">

                <h1>${name}</h1>

                <img class="card-icon" src="${icon}" alt="${name} icon">

                <p>${dialog}</p>
            </div>
        `;
        }

        
    }
}

customElements.define("mead-card", MeadCard);