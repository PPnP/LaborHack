const preloader = document.querySelector(".preloader");

const hideLoader = () => {
    preloader.classList.add("preloader_hidden");
}

window.addEventListener("load", hideLoader);