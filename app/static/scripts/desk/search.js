/**
 * Responsible for searching for ads.
 */

const input = document.querySelector('.search-input');
const contents = document.querySelectorAll('.ad-card');

const searchButton = document.getElementById('find_button');
const backButton = document.querySelector('.back-button');

const contentFilters = document.querySelector('.content__filters');
const languageSelection = document.querySelectorAll('#language_selection .checkbox');


// Returns an array of values of checked checkboxes inside node
const getCheckboxes = (node) => {
    const checkboxes = node.querySelectorAll('input[type=checkbox]');
    const checked = [];

    checkboxes.forEach((box) => {
        if (box.checked) {
            checked.push(box.value);
        }
    });

    return checked;
};

// Sets all checkboxes to value inside node
const setCheckboxes = (node, value) => {
    const checkboxes = node.querySelectorAll('input[type=checkbox]');

    checkboxes.forEach((box) => {
        box.checked = value;

        /* "The onchange event does not fire when the
        selected option of the select object is changed
        programmatically." MDN */
        box.dispatchEvent(new Event('change'));
    });
};

// Runs search and hides/shows matching ads
const search = () => {
    const query = input.value;

    // Get districts, languages and service type filters
    const districts = getCheckboxes(document.getElementById('district_selection'));
    const languages = getCheckboxes(document.getElementById('language_selection'));
    const services = getCheckboxes(document.getElementById('service_selection'));

    contents.forEach((card) => {
        // Case-insensitive search among profile card content
        const needleRegExp = new RegExp(query.trim(), 'i');

        let found = needleRegExp.test(card.innerText);

        // If at least one district was selected
        if (districts.length) {
            found = found && districts.includes(card.getAttribute('data-district'));
        }

        // If at least one language was selected
        if (languages.length) {
            found = found && languages.includes(card.getAttribute('data-language'));
        }

        // If at least one service type was selected
        if (services.length) {
            found = found && services.includes(card.getAttribute('data-type'));
        }

        card.classList.toggle('ad-card_invisible', !found);
    });
};

// Clears the search input and shows all results
const cancelSearch = () => {
    input.value = '';
    backButton.classList.remove('back-button_on');

    setCheckboxes(contentFilters, false);
    search();
};

// Attach event listeners
searchButton.addEventListener('click', () => {
    backButton.classList.add('back-button_on');
    search();
});

backButton.addEventListener('click', cancelSearch);

// Add class to language checkbox on click (box-shadow)
languageSelection.forEach((selection) => {
    const checkbox = selection.querySelector('input[type=checkbox]');

    checkbox.addEventListener('change', () => {
        selection.classList.toggle('selection__button_checked', checkbox.checked);
    });
});
