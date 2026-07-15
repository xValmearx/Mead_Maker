class MeadCard extends HTMLElement {
    connectedCallback() {

        const type = this.getAttribute("type") || "";
        const name = this.getAttribute("name") || "Blank";
        const icon = this.getAttribute("icon") || "";

        if(icon == ""){
            this.innerHTML = `
            <div class="card ${type}">

                <h1>${name}</h1>

                <p>This is the card's information.</p>
            </div>
        `;
        }
        else{
            this.innerHTML = `
            <div class="card ${type}">

                <h1>${name}</h1>

                <img class="card-icon" src="${icon}" alt="${name} icon">

                <p>This is the card's information.</p>
            </div>
        `;
        }

        
    }
}

customElements.define("mead-card", MeadCard);