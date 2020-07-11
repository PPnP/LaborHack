/**
 * Responsible for showing/hiding "Add event" form on button click.
 */

const map = document.getElementById('map');

const addBlock = document.querySelector('.add-event');
const addButton = document.querySelector('.content__add-event');

const backButton = document.querySelector('.back-button');

const hideForm = () => {
    // Show map and "Add event" button
    map.style.display = 'block';
    addButton.style.display = 'block';

    // Hide form and deactivate "Back" button
    addBlock.classList.remove('add-event_visible');
    backButton.classList.remove('back-button_on');
};

const showForm = () => {
    // Hide map and "Add event" button
    map.style.display = 'none';
    addButton.style.display = 'none';

    // Show form and activate "Back" button
    addBlock.classList.add('add-event_visible');
    backButton.classList.add('back-button_on');

    activateButtons();

    backButton.addEventListener('click', hideForm);
};

addButton.addEventListener('click', showForm);
