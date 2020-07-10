const addButton = document.getElementById("add_event");
const map = document.getElementById("map");
const addBlock = document.querySelector(".add-event");
const backButton = document.querySelector(".back-button");

const hideForm = () => {
    // Возвращаем карту и кнопку добавления мероприятия
    map.style.display = "block";
    addButton.style.display = "block";

    // Скрываем форму добавления мероприятия и кнопку назад
    addBlock.classList.remove("add-event_visible");
    backButton.classList.remove("back-button_on");
};

const showForm = () => {
    // Скрываем карту и кнопку добавления мероприятия
    map.style.display = "none";
    addButton.style.display = "none";

    // Показываем форму добавления мероприятия и кнопку назад
    addBlock.classList.add("add-event_visible");
    backButton.classList.add("back-button_on");

    activateButtons();

    backButton.addEventListener("click", hideForm);
};

addButton.addEventListener("click", showForm);