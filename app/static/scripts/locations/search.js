/**
 * Responsible for searching for categories of events.
 */

const input = document.querySelector('.search-input');
const contents = document.querySelectorAll('.category');

// Runs search and hides/shows matching profiles
const search = debounceEvent(() => {
    const query = input.value;

    contents.forEach((category) => {
        // Case-insensitive search among category card content
        const needleRegExp = new RegExp(query.trim(), 'i');
        const found = needleRegExp.test(category.innerText);

        category.classList.toggle('category_invisible', !found);
    });
}, 300);

// Clears the search input and shows all results
const cancelSearch = () => {
    input.value = '';
    backButton.classList.remove('back-button_on');

    search();
};

backButton.addEventListener('click', cancelSearch);

input.addEventListener('keyup', () => {
    backButton.classList.add('back-button_on');
    search();
});
