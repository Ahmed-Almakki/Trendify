document.addEventListener('DOMContentLoaded', () => {
    const top = document.getElementById('top');
    const bottom = document.getElementById('bottom');
    const newItem = document.getElementById('topBot');

    function chooseTopBottom() {
        if (top.checked) {
            newItem.innerHTML = `
                    <legend>Sleeve</legend>
                    <input type="radio" class="sleeve" id="short" name="sleeve" value="short"><label for="short">Short</label>
                    <input type="radio" class="sleeve" id="long" name="sleeve" value="long"><label for="long">Long</label>
                    `
        } 
        if (bottom.checked) {
            newItem.innerHTML = `
                    <legend>Pants</legend>
                    <input type="radio" class="pants" id="short" name="length" value="short"><label for="short">Short</label>
                    <input type="radio" class="pants" id="long" name="length" value="long"><label for="long">Long</label>
            `
        }
    }
    chooseTopBottom();

    top.addEventListener('change', chooseTopBottom);
    bottom.addEventListener('change', chooseTopBottom);
})