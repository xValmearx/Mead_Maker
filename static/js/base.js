class MeadCard extends HTMLElement {
    connectedCallback() {
        const slug = this.getAttribute("slug");
        const type = this.getAttribute("type") || "";
        const name = this.getAttribute("name") || "Blank";
        const icon = this.getAttribute("icon") || "";
        const dialog = this.getAttribute("dialog") || "";

        if(icon == ""){
            this.innerHTML = `
            <a href="/mead/create/${slug}/" class="card-link">
                <div class="card ${type}">

                <h1>${name}</h1>

                <p>${dialog}</p>
            </div>
            </a>
            
        `;
        }
        else{
            this.innerHTML = `
            <a href="/mead/create/${slug}/" class="card-link">
            <div class="card ${type}">

                <h1>${name}</h1>

                <img class="card-icon" src="${icon}" alt="${name} icon">

                <p>${dialog}</p>
            </div>
            </a>
        `;
        }

        
    }
}

customElements.define("mead-card", MeadCard);