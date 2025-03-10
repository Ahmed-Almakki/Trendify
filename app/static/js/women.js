const items = document.getElementById("items")
document.addEventListener("DOMContentLoaded", () => {
    fetch('http://127.0.0.1:5000/api/women')
    .then(response => response.json())
    .then((data) => {
        const item = data;
        item.forEach(element => {
            if (element.image_url !== null) {
                const newItem = document.createElement('div');
                // newItem.classList.add('cards')
                newItem.innerHTML = `
                <div class="cards">
                    <div class="card_image">
                        <img src="${element.image_url}"  width=800 height=800>
                    </div>
                    <div>
                        <p class="boold"><span>Price:</span>  ${element.price}    $</p>
                    </div>
                </div>
                `
                items.appendChild(newItem)
            }
        });
    })
    .catch(error => console.error(error))
});