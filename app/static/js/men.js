const items = document.getElementById("items")
document.addEventListener("DOMContentLoaded", () => {
    const sleevSelector = document.getElementById('sleeve')
    const pantsSelector = document.getElementById('length')
    const colorSelector = document.getElementById('color')
    function filterData() {
        console.log(sleevSelector, pantsSelector)
        const slev = sleevSelector.value
        const pnts = pantsSelector.value
        const colr = colorSelector.value
        let url;
        if (!slev && !pnts && !colr) {
            url = `http://127.0.0.1:5000/api/${user}`;
        } else {
            const arg = new URLSearchParams();
            if (slev) {
                console.log('sleeve', slev);
                arg.append("sleeve", slev);
            }
            if (pnts) {
                console.log('length', pnts);
                arg.append("length", pnts);
            }
            if (colr) {
                console.log('color', colr);
                arg.append("color", colr);
            }
            url = `http://127.0.0.1:5000/api/${user}?${arg.toString()}`
        }
        console.log("used url", url)
        fetch(url)
            .then(response => response.json())
            .then((elmnt) => {
                items.innerHTML = ""
                elmnt.forEach(itm => {
                    console.log("its a price of  ", user, itm.price)
                    if (itm.image_url !== null) {
                        const newItem = document.createElement('div')
                        newItem.innerHTML = `
                        <div class="cards">
                            <div class="card_image">
                            <img src="${itm.image_url}"  width=800 height=1000>
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