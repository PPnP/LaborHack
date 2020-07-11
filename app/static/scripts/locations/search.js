const input = document.querySelector(".search-input");
const contents = document.querySelectorAll(".category");

const debounceEvent = (callback, time) => {
    let interval;
    return (...args) => {
        clearTimeout(interval);
        interval = setTimeout(() => {
            interval = null;
            callback(...args);
        }, time);
    };
};

const search = debounceEvent(() => {
    let query = input.value;

    contents.forEach(category => {
        // регистронезависимый поиск
        let needleRegExp = new RegExp(query.trim(), "i");
        let found = needleRegExp.test(category.innerText);

        category.classList.toggle("category_invisible", !found);
    });
}, 300)

input.addEventListener("keyup", search);