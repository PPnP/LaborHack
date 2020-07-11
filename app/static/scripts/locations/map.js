/**
 * Responsible for showing events on a map.
 */

let ymap; // map object
let activeFilter = null; // current filter slug
const categoryButtons = document.querySelectorAll('.category');

// Returns JSON from /data/slug
async function getPlaceJson(slug) {
    const response = await fetch(`/data/${slug}`);
    return response.json();
}

// Adds points to the map
const drawPlace = (map, slug, color, placesJSON) => {
    const collection = new ymaps.GeoObjectCollection({}, {
        feature: slug,
    });

    placesJSON.forEach((place) => {
        const obj = new ymaps.Placemark([place.latitude, place.longitude], {
            hintContent: place.title,
            balloonContentHeader: place.title,
            balloonContentBody: place.description,
            balloonContentFooter: place.address,
        }, {
            iconColor: color,
        });

        collection.add(obj);
    });

    map.geoObjects.add(collection);
};

// Loads events and draws them on the map
const loadPlacesJSON = (map) => {
    categoryButtons.forEach((button) => {
        const slug = button.getAttribute('data-slug');
        const color = button.style.backgroundColor;

        getPlaceJson(slug).then((json) => {
            drawPlace(map, slug, color, json);
        });
    });
};

// Filters points on a map based on slug provided
const filterPlaces = (slug) => {
    ymap.geoObjects.each((collection) => {
        collection.each((obj) => {
            let { feature } = collection;
            feature = collection.options._options.feature;

            /* If collection's slug matches the provided one, then
            show the point. Otherwise hide it. null denotes all points
            should be shown. */
            obj.options.set({ visible: slug === null || feature === slug });
        });
    });

    activeFilter = slug;
};

// Activate all categories buttons
const activateButtons = () => {
    categoryButtons.forEach((button) => {
        button.classList.remove('category_inactive');
    });
};

// Deactivates all categories buttons except the one provided
const deactivateButtons = (except) => {
    categoryButtons.forEach((button) => {
        button.classList.toggle('category_inactive', button !== except);
    });
};

// Handles category button click
const categoryButtonClick = (button) => {
    const slug = button.getAttribute('data-slug');

    if (activeFilter === slug) {
        // current filter button was clicked, reset filters
        filterPlaces(null);
        return activateButtons();
    }

    filterPlaces(slug);
    deactivateButtons(button);
};

// Runs map rendering
const init = () => {
    ymap = new ymaps.Map('map', {
        center: [59.91, 30.50], // Kudrovo centre
        zoom: 12,
    });

    loadPlacesJSON(ymap);

    categoryButtons.forEach((button) => {
        button.addEventListener('click', () => categoryButtonClick(button));
    });
};

ymaps.ready(init);
