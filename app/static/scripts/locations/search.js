const input = document.querySelector(".search-input");
const contents = document.querySelectorAll(".category");

// Выполняет поиск
const search = debounceEvent(() => {
    let query = input.value;

    contents.forEach(category => {
        // регистронезависимый поиск
        let needleRegExp = new RegExp(query.trim(), "i");
        let found = needleRegExp.test(category.innerText);

        category.classList.toggle("category_invisible", !found);
    });
}, 300)

// Очищает строку поиска и показывает все результаты
const cancelSearch = () => {
    backButton.classList.remove("back-button_on");
    input.value = "";
    search();
}

backButton.addEventListener("click", cancelSearch);

input.addEventListener("keyup", () => {
    backButton.classList.add("back-button_on");
    search();
});