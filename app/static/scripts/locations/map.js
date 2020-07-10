var ymap; // глобальный объект карты
let activeFilter = null; // slug текущего фильтра
const categoryButtons = document.querySelectorAll(".category");

// Возвращает JSON из файла /data/?
async function getPlaceJson(slug) {
    const response = await fetch(`/data/${slug}`);
    return await response.json();
}

// Фильтрует точки на карте в зависимости от переданного slug
const filterPlaces = (slug) => {
    ymap.geoObjects.each((collection) => {
        collection.each((obj) => {
            let feature = collection.options._options.feature;

            /* 
            Если slug коллекции совпадает с необходимым, показываем
            точку, иначе скрываем. null передается для показа всех точек.
            */
            obj.options.set({ visible: slug == null || feature == slug });
        })
    });

    activeFilter = slug;
}

// Активирует все кнопки фильтров
const activateButtons = () => {
    categoryButtons.forEach(button => {
        button.classList.remove("category_inactive");
    });
}

// Деактивирует все кнопки, кроме данной
const deactivateButtons = (except) => {
    categoryButtons.forEach(button => {
        if (button == except) {
            return button.classList.remove("category_inactive");
        }

        button.classList.add("category_inactive");
    });
};

// Главная функция, запускает работу карты
const init = () => {
    ymap = new ymaps.Map("map", {
        center: [59.91, 30.50], // центр района Кудрово
        zoom: 12
    });

    loadPlacesJSON(ymap);

    categoryButtons.forEach(button => {
        button.addEventListener("click", () => categoryButtonClick(button));
    });
}

// Обрабатывает нажатие на кнопку фильтра
const categoryButtonClick = (button) => {
    let slug = button.getAttribute("data-slug");

    if (activeFilter == slug) {
        // произошло нажатие на кнопку текущего фильтра, сбрасываем фильтры
        filterPlaces(null);
        return activateButtons();
    }

    filterPlaces(slug);
    deactivateButtons(button);
};

// Добавляет точки на карту
const drawPlace = (map, slug, color, placesJSON) => {
    let collection = new ymaps.GeoObjectCollection({}, {
        feature: slug
    });

    placesJSON.forEach(place => {
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
        let slug = button.getAttribute("data-slug");
        let color = button.style.backgroundColor;

        getPlaceJson(slug).then((json) => {
            drawPlace(map, slug, color, json);
        });
    });
}

ymaps.ready(init);