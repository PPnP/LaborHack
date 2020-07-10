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
    ymap = new ymaps.Map("map", {
        center: [59.91, 30.50],
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

const drawPlace = (map, category, color, placeJSON) => {
    let collection = new ymaps.GeoObjectCollection({}, {
        feature: category
    });

    placeJSON.forEach(place => {
        let obj = new ymaps.Placemark([place.latitude, place.longitude], {
            hintContent: place.title,
            balloonContentHeader: place.title,
            balloonContentBody: place.description,
            balloonContentFooter: place.address
        }, {
            iconColor: color
        });

        collection.add(obj);
    });

    map.geoObjects.add(collection);
}

const loadPlacesJSON = (map) => {
    categoryButtons.forEach(button => {
        let category = button.getAttribute("data-slug");
        let color = button.style.backgroundColor;

        getPlaceJson(category).then((json) => {
            drawPlace(map, category, color, json);
        });
    });
}

ymaps.ready(init);