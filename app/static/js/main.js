const items = document.getElementById("items")
document.addEventListener("DOMContentLoaded", () => {
    fetch('http://127.0.0.1:5000/api/men')
    .then(response => response.json())
    .then((data) => {
        console.log(data[3]);
        const item = data[3];
        const newItem = document.createElement('div');
        newItem.innerHTML = `
        <div class="cards">
            <figure>
                <img src="${item.image_url}" >
            </figure>
            <span><p>${item.price}</p> $</span>
        `
        items.appendChild(newItem)
    })
    .catch(error => console.error(error))
});