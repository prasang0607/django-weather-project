const add = document.querySelector("#add");
const city = document.querySelector(".city");
const empty = document.querySelector('#empty');

function removeEmpty() {
    empty.style.display = 'none';
    city.classList.remove("is-danger");
}

function delete_notification() {
    const notification = document.querySelector(".msg");
    notification.style.display = 'none';
}

add.addEventListener('click', () => {

    if (city.value.length === 0) {
        empty.style.display = 'block';
        city.classList.add("is-danger");
        setTimeout(removeEmpty, 3000);
    } else {
        add.classList.add("is-loading");
    }
});


document.addEventListener('DOMContentLoaded', () => {
    setTimeout(delete_notification, 4000);
});