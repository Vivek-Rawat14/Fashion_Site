  document.addEventListener('DOMContentLoaded', () => {
    let searchinput = document.getElementById('searcht');
    let searchbutton = document.getElementById('searchbuttont');

    searchbutton.addEventListener("click", (event) => {
        event.preventDefault();
        let query = encodeURIComponent(searchinput.value.trim());
        if (query) {
            window.location.href = `${window.location.origin}/search/${query}/`;
        }
    });
});