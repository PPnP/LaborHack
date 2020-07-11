const input = document.querySelector(".search-input");
const contents = document.querySelectorAll(".person-card");
const searchButton = document.getElementById("find_button");
const backButton = document.querySelector(".back-button");
const contentFilters = document.querySelector(".content__filters");
const languageSelection = document.querySelectorAll("#language_selection .checkbox");

// Выполняет поиск
const search = () => {
    let query = input.value;

    let districts = getCheckboxes(document.getElementById("district_selection"));
    let languages = getCheckboxes(document.getElementById("language_selection"));

    contents.forEach(card => {
        // регистронезависимый поиск
        let needleRegExp = new RegExp(query.trim(), "i");

        let found = needleRegExp.test(card.innerText);

        if (districts.length) {
            found = found && districts.includes(card.getAttribute("data-district"));
        }

        if (languages.length) {
            found = found && languages.includes(card.getAttribute("data-language"));
        }

        card.classList.toggle("person-card_invisible", !found);
    });
};

// Очищает строку поиска и показывает все результаты
const cancelSearch = () => {
    backButton.classList.remove("back-button_on");
    setCheckboxes(contentFilters, false);
    input.value = "";
    search();
}

// Возвращает массив выбранных пользователем чекбоксов в node
const getCheckboxes = (node) => {
    const checkboxes = node.querySelectorAll("input[type=checkbox]");

    let checked = [];

    checkboxes.forEach(box => {
        if (box.checked) {
            checked.push(box.value);
        }
    });

    return checked;
}

// Устанавливает все чекбоксы в node на значение value
const setCheckboxes = (node, value) => {
    const checkboxes = node.querySelectorAll("input[type=checkbox]");

    checkboxes.forEach(box => {
        box.checked = value;

        /* 
        "The onchange event does not fire when the 
        selected option of the select object is changed programmatically."
        */
        box.dispatchEvent(new Event('change'));
    });
}

searchButton.addEventListener("click", () => {
    backButton.classList.add("back-button_on");
    search();
});

backButton.addEventListener("click", cancelSearch);

languageSelection.forEach(selection => {
    var checkbox = selection.querySelector("input[type=checkbox]");

    checkbox.addEventListener("change", () => {
        selection.classList.toggle("selection__button_checked", checkbox.checked);
    });
});