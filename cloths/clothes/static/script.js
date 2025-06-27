document.addEventListener('DOMContentLoaded', () => {
    let searchinput = document.getElementById('search');
    let searchbutton = document.getElementById('searchbutton');

    searchbutton.addEventListener("click", (event) => {
        event.preventDefault();
        let query = encodeURIComponent(searchinput.value.trim());
        if (query) {
            window.location.href = `${window.location.origin}/search/${query}/`;
        }
    });
});