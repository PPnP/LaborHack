const categoryButtons = document.querySelectorAll(".category");
var ymap;
let activeFilter = null;

async function getPlaceJson(slug) {
    const response = await fetch(`/data/${slug}`);
    return await response.json();
}

const filterPlaces = (slug) => {
    ymap.geoObjects.each((collection) => {
        collection.each((obj) => {
            let feature = collection.options._options.feature;
            obj.options.set({ visible: slug == null || feature == slug });
        })
    });

    activeFilter = slug;
}

const activateButtons = () => {
    categoryButtons.forEach(button => {
        button.classList.remove("category_inactive");
    });
}

const deactivateButtons = (except) => {
    categoryButtons.forEach(button => {
        if (button == except) {
            return button.classList.remove("category_inactive");
        }

        button.classList.add("category_inactive");
    });
};

const init = () => {
    // Создание карты.    
    ymap = new ymaps.Map("map", {
        // Координаты центра карты.
        // Порядок по умолчанию: «широта, долгота».
        // Чтобы не определять координаты центра карты вручную,
        // воспользуйтесь инструментом Определение координат.
        center: [59.91, 30.50],
        // Уровень масштабирования. Допустимые значения:
        // от 0 (весь мир) до 19.
        zoom: 12
    });

    loadPlacesJSON(ymap);

    categoryButtons.forEach(button => {
        button.addEventListener("click", () => categoryButtonClick(button));
    });
}

const categoryButtonClick = (button) => {
    let slug = button.getAttribute("data-slug");

    if (activeFilter == slug) {
        filterPlaces(null);
        return activateButtons();
    }

    filterPlaces(slug);
    deactivateButtons(button);
};

const drawPlace = (map, category, placeJSON) => {
    let collection = new ymaps.GeoObjectCollection({}, {
        feature: category
    });

    placeJSON.forEach(place => {
        let obj = new ymaps.GeoObject({
            geometry: {
                type: "Point",
                coordinates: [
                    place.latitude,
                    place.longitude
                ]
            }
        });

        collection.add(obj);
    });

    map.geoObjects.add(collection);
}

const loadPlacesJSON = (map) => {
    let categories = [
        "culture",
        "development",
        "food",
        "leisure",
        "life",
        "religion",
    ];

    categories.forEach(category => {
        getPlaceJson(category).then((json) => {
            drawPlace(map, category, json);
        });
    });
}

ymaps.ready(init);