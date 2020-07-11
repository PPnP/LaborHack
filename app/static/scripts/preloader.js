/**
 * Responsible for hiding the preloader after page loading.
 */

const preloader = document.querySelector('.preloader');

window.addEventListener('load', () => {
    preloader.classList.add('preloader_hidden');
});
