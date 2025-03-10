const items = document.getElementById("items")
document.addEventListener("DOMContentLoaded", () => {
    const sleevSelector = document.getElementById('sleeve')
    const pantsSelector = document.getElementById('pants')
    const colorSelector = document.getElementById('color')
    function filterData() {
        const slev = sleevSelector.value
        const pnts = pantsSelector.value
        const colr = colorSelector.value
        let url;
        if (!slev && !pnts && !colr) {
            url = "http://127.0.0.1:5000/api/men";
        } else {
            const arg = new URLSearchParams();
            if (slev) arg.append("sleeve", slev);
            if (pnts) arg.append("pants", pnts);
            if (colr) arg.append("color", colr);
            url = `http://127.0.0.1:5000/api/men?${arg.toString()}`
        }
        fetch(url)
            .then(response => response.json())
            .then((elmnt) => {
                items.innerHTML = ""
                elmnt.forEach(itm => {
                    if (itm.image_url !== null) {
                        const newItem = document.createElement('div')
                        newItem.innerHTML = `
                        <div class="cards">
                            <div class="card_image">
                            <img src="${itm.image_url}"  width=800 height=800>
                            </div>
                            <div>
                            <p class="boold"><span>Price:</span>  ${itm.price}    $</p>
                            </div>
                        </div>
                        `
                        items.appendChild(newItem)
                    }
                });
            })
            .catch(error => console.error(error));
    }
    filterData();

    // now wait for event 
    sleevSelector.addEventListener('change', filterData);
    pantsSelector.addEventListener('change', filterData);
    colorSelector.addEventListener('change', filterData);

});