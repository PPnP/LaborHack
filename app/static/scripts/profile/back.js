const backButton = document.querySelector(".back-button");

const activateBackButton = () => {
    backButton.classList.add("back-button_on");
};

const goBack = () => {
    window.history.back();
};

activateBackButton();
backButton.addEventListener("click", goBack);