const addButton = document.getElementById("add_event");
const map = document.getElementById("map");
const addBlock = document.querySelector(".add-event");
const backButton = document.querySelector(".back-button");

const showForm = () => {
    map.style.display = "none";
    addButton.style.display = "none";

    addBlock.classList.add("add-event_visible");

    backButton.classList.add("back-button_visible");
    backButton.addEventListener("click", () => {
        map.style.display = "block";
        addButton.style.display = "block";

        addBlock.classList.remove("add-event_visible");
        backButton.classList.remove("back-button_visible");

    });
};

addButton.addEventListener("click", showForm);