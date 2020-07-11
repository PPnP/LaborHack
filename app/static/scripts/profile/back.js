/**
 * Responsible for the functionality of the "Back" button.
 */

const backButton = document.querySelector('.back-button');

backButton.classList.add('back-button_on');
backButton.addEventListener('click', () => window.history.back());
