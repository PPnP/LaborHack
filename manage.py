import os
import shutil
import json

from app import application, db, manager
from app.api import routes


@manager.command
def runserver():
    application.config['DOMAIN'] = 'localhost:5000/'
    application.register_blueprint(routes.api, url_prefix='/')
    application.run(host='localhost', port=5000, debug=True)


@manager.command
def db_delete():
    if os.path.exists('migrations'):
        shutil.rmtree('migrations')
    if os.path.exists('database.db'):
        os.remove('database.db')


@manager.command
def db_reset():
    db.drop_all()
    db.create_all()


@manager.command
def data_dumping():
    leisure = [
        {"latitude": "59.90266", "longitude": "30.47485", "address": "ул. Дыбенко, 23к3", "title": "Спортплощадка",
         "type": "Спорт", "description": "", "language": "", "rating": 4},
        {"latitude": "45.84887", "longitude": "40.12593", "address": "ул. Подвойского, 17", "title": "Спортплощадка",
         "type": "Спорт", "description": "", "language": "", "rating": 2.2},
        {"latitude": "55.46934", "longitude": "38.33663", "address": "Центральная ул., 54к1", "title": "Летний каток",
         "type": "Спорт/отдых", "description": "Каток от 300руб/час", "language": "Русский", "rating": 3.4},
        {"latitude": "59.89706", "longitude": "30.49369", "address": "пр. Большевиков, 38к1", "title": "Футбольное поле",
         "type": "Спорт", "description": "Бесплатное футбольное поле. Инвентарь приносить свой", "language": "",
         "rating": 4.9}
    ]
    religion = [
        {"latitude": "60.01775", "longitude": "30.28112", "address": "Репищева ул., 1, Санкт-Петербург",
         "title": "Квартальная мечеть им. Джафара Насибулловича", "type": "Мечеть",
         "description": "Вторая по величине мечеть Санкт-Петербурга, находится на севере города в районе Коломяги, на Парашютной улице. Открыта 16 июля 2009 года.",
         "language": "русский, арабский, киргизский, казахский, узбекский, таджикский", "rating": 4.1},
        {"latitude": "59.95523", "longitude": "30.3239", "address": "Кронверкский просп., 7, Санкт-Петербург",
         "title": "Соборная мечеть", "type": "Мечеть",
         "description": "Соборная мечеть находится центре города и до сих пор в ней проходят службы. К сожалению, попасть внутрь неудалось, хотя такая возможность имеется. Санкт-Петербургская мечеть является самой крупной в Европе и самой северной в мире. Ее длина 45 метров, ширина — 32 метра, высота главного купола — 39 метров, высота минаретов — 48 метров, вместимость — до пяти тысяч человек. Это красивое и величественное здание, сочетающее элементы традиционной восточной архитектуры и черты северного модерна. При этом она очень похожа на усыпальницу Амира Темура (Тамерлана), которая находится в г. Самарканде",
         "language": "русский, арабский, киргизский, казахский, узбекский, таджикский", "rating": 4.7},
        {"latitude": "59.92412", "longitude": "30.31809",
         "address": "Московский просп., 10-12Г, Санкт-Петербург", "title": "Соборная мечеть, молельная комната",
         "type": "Молельная комната", "description": "Место для молитвы",
         "language": "русский, арабский, киргизский, казахский, узбекский, таджикский", "rating": 4.6},
        {"latitude": "59.92263", "longitude": "30.46424", "address": "парк Оккервиль",
         "title": "Изучение Корана в парке", "type": "Встреча", "description": "Общаемся и познаём Аллаха",
         "language": "русский, узбекский", "rating": 4.9}
    ]
    life = [
        {"latitude": "59.90339", "longitude": "30.47485", "address": "пр. Большевиков, 25", "title": "Только ты",
         "type": "Парикмахерская", "description": "Профессиональные стилисты и визажисты со всей страны!",
         "language": "Русский", "rating": 3.4},
        {"latitude": "59.901", "longitude": "30.48305", "address": "ул. Шотмана, 7к1", "title": "Парикмахерская",
         "type": "Парикмахерская", "description": "", "language": "Русский, Узбекский", "rating": 4.5},
        {"latitude": "59.89681", "longitude": "30.51033", "address": "Центральная ул., д.54 к.2, Кудрово",
         "title": "РЕСО-мед", "type": "Медицина", "description": "Здесь можно купить все лекарства",
         "language": "Русский", "rating": 2.9},
        {"latitude": "59.9001", "longitude": "30.52047", "address": "просп. Строителей, 33, Кудрово",
         "title": "МФЦ ГБУ ЛО", "type": "МФЦ", "description": "Многофункциональный центр",
         "language": "Русский, Узбекский, Казахский, Английский", "rating": 4.7}
    ]
    food = [
        {"latitude": "59.91416", "longitude": "30.47454", "address": "просп. Большевиков, 9, корп. 1, Санкт-Петербург",
         "title": "Чайхана Чабрец", "type": "Кафе", "description": "Вкусно и недорого!",
         "language": "русский, узбекский, киргизский", "rating": 4.4,
         "reviews": "Хорошая сеть. Чабрец на бизнес ланч шикарно. 400 р отличный сытный обед. ; Очень вкусный шашлык. Место приятное, симпатичный интерьер. К обслуживанию нареканий нет."},
        {"latitude": "59.90773", "longitude": "30.48502", "address": "просп. Большевиков, 18, Санкт-Петербург",
         "title": "Макдоналдс", "type": "Кафе", "description": "Известные бургеры и кола", "language": "", "rating": 4.3,
         "reviews": "Перед кассами и на выдаче очень мало места. Учитывая, разумеется, толпу голодного народа (почти) в любое время дня и вечера. Хотя на выходных вроде обслуживание столиков ввели.. это, несомненно, плюс. Но столиков свободных мало. И это минус :-) ; Kafe va qulay joylashgan, juda keng xona, buyurtma berish uchun terminallar mavjud, xizmat tezdir ."},
        {"latitude": "59.90442", "longitude": "30.50956", "address": "Европейский просп., 13, корп. 1, Кудрово",
         "title": "Шаверма Евро Кебаб", "type": "Кафе", "description": "Шаверма", "language": "русский, киргизский",
         "rating": 4,
         "reviews": "Мне эта сеть харчевен нравится Съедобно, надеюсь безопасно Везде чисто Цены по моему мнению бюджетные"},
        {"latitude": "59.9031371", "longitude": "30.5123403", "address": "Европейский просп., 13, корп. 6, Кудрово",
         "title": "Мясной № 1", "type": "Продуктовый", "description": "", "language": "русский, узбекский",
         "rating": 4.6, "reviews": ""},
        {"latitude": "59.90401", "longitude": "30.51957", "address": "Английская ул., 2, Кудрово", "title": "Дикси",
         "type": "Продуктовый", "description": "", "language": "русский, киргизский", "rating": 4, "reviews": ""},
        {"latitude": "59.9036", "longitude": "30.50919", "address": "Австрийская ул., 4, корп. 1, Кудрово",
         "title": "Семишагофф", "type": "Продуктовый", "description": "", "language": "русский, узбекский, киргизский",
         "rating": 3.5,
         "reviews": "көп учурда, жөө аралыкта жайгашкан, башка супермаркеттер менен бирге, бирок аны кезекти бул дүкөн дээрлик жок, жана башкы нерсе тандап."}
    ]
    culture = [
        {"latitude": "59.90061", "longitude": "30.50858", "address": "Венская ул., 4, корп. 1, Кудрово",
         "title": "EXPODOM", "type": "Выставка", "description": "Постоянная выставка загородного строительства",
         "language": "Русский, Английский", "rating": 3},
        {"latitude": "59.901", "longitude": "30.48305", "address": "ул. Шотмана, 7/1",
         "title": "Невская ЦБС. Библиотека № 5 им. Н. Рубцова", "type": "Библиотека",
         "description": "Библиотека СБб ГБУ", "language": "Русский", "rating": 4},
        {"latitude": "59.90773", "longitude": "30.48502", "address": "ТРК Невский, пр. Большевиков, 18",
         "title": "Картины в дом", "type": "Картинная галерея", "description": "", "language": "", "rating": 2.3},
        {"latitude": "59.9006", "longitude": "30.5087", "address": "Венская ул., 3", "title": "Шить - Легко!",
         "type": "Курсы", "description": "Курсы шитья в ателье Шить - Легко!, бесплатно научим шить!",
         "language": "Русский", "rating": 4.9}
    ]
    development = [
        {"latitude": "59.9027904", "longitude": "30.5170321", "address": "Английская улица, 3",
         "title": "Курсы русского языка", "type": "Курсы",
         "description": "Бесплатные занятия по русскому языку",
         "language": "русский, киргизский, казахский, узбекский, таджикский", "rating": 4.8,
         "reviews": "Теперь я знаю русский!!! Всем советую"},
        {"latitude": "59.9030465", "longitude": "30.5127805", "address": "Европейский просп., 14, Кудрово",
         "title": "Академия цифровых технологий", "type": "Курсы",
         "description": "Современное образование для современного города", "language": "русский",
         "rating": 5, "reviews": "класс Көлөм"},
        {"latitude": "59.9053", "longitude": "30.52055", "address": "Пражская ул., 15, Кудрово",
         "title": "ЦОПП «Профстандарт»", "type": "Курсы",
         "description": "Программы профессионального обучения (профессиональной подготовки, переподготовки, повышения квалификации по профессиям рабочих и должностям служащих)",
         "language": "", "rating": 5, "reviews": "абдан жакшы"},
        {"latitude": "59.89681", "longitude": "30.51033", "address": "Центральная ул., 54, корп. 2, Кудрово",
         "title": "Готовим плов", "type": "Мастер-класс", "description": "Научим готовить очень вкусный плов",
         "language": "русский, узбекский", "rating": 4, "reviews": "juda yaxshi yoqdi"}
    ]
    services = [
        {"title": "Срочно нужна дрель", "type": "Инструменты", "get/provide": "Получить",
         "description": "Только на один день", "author_id": "562792", "price": ""},
        {"title": "телефон на день", "type": "", "get/provide": "Получить",
         "description": "сломался телефон не включается срочно нужен телефон на завтра", "author_id": "109290",
         "price": "200"},
        {"title": "отдам коляску", "type": "Для детей", "get/provide": "Оказать",
         "description": "Отдам коляску, пользовалась два года", "author_id": "125123", "price": ""},
        {"title": "Молоток", "type": "Инструменты", "get/provide": "Получить",
         "description": "Нужен качественный молоток для стойки", "author_id": "991255", "price": "1400"},
        {"title": "Подстригу как себя", "type": "Парикмахер", "get/provide": "Оказать",
         "description": "Очень красиво недорого любая стрижка", "author_id": "562794", "price": "1000"},
        {"title": "Срочно ребенка дать", "type": "Няня", "get/provide": "Получить",
         "description": "Посиди с ребенком один день марҳамат очень надо накормлю", "author_id": "109294", "price": "0"},
        {"title": "Любой ремонт хорошо", "type": "Стройка", "get/provide": "Оказать",
         "description": "Сделаю всё стены пол крыша обои всё быстро очень", "author_id": "125124", "price": "500"},
        {"title": "Сломался телефон", "type": "Ремонт", "get/provide": "Получить",
         "description": "Сломался экран на nokia срочно надо", "author_id": "991254", "price": "300"}
    ]
    people = [
        {"id": "562792", "name": "Игорь", "surname": "Ванко", "country": "Украина",
         "language": "Русский, Украинский", "phone": "89043538951", "district": "Кудрово"},
        {"id": "109290", "name": "Алтай", "surname": "Рашидов", "country": "Узбекистан",
         "language": "Узбекский", "phone": "89218903153", "district": "Кудрово"},
        {"id": "125123", "name": "Зухра", "surname": "Юсупова", "country": "Узбекистан",
         "language": "Русский, Узбекский", "phone": "89644789234", "district": "Кудрово"},
        {"id": "991255", "name": "Айдар", "surname": "Пак", "country": "Казахстан",
         "language": "Русский, Казахский", "phone": "89522971424", "district": "Кудрово"},
        {"id": "562797", "name": "Азамат", "surname": "Исмаилов", "country": "Киргизия",
         "language": "Киргизский", "phone": "89992453423", "district": "Кудрово"},
        {"id": "109294", "name": "Нурбек", "surname": "Абдуллаев", "country": "Таджикистан",
         "language": "Русский, Таджикский", "phone": "89045367489", "district": "Кудрово"},
        {"id": "125124", "name": "Айбек", "surname": "Акматов", "country": "Таджикистан",
         "language": "Таджикский", "phone": "89212342433", "district": "Кудрово"},
        {"id": "991254", "name": "Аслан", "surname": "Каримов", "country": "Узбекистан",
         "language": "Русский, Узбекский", "phone": "89994322353", "district": "Кудрово"}
    ]

    if os.path.exists('data'):
        shutil.rmtree('data')
    os.mkdir('data')

    with open('data/leisure.json', 'w') as output:
        json.dump(leisure, output)
    with open('data/religion.json', 'w') as output:
        json.dump(religion, output)
    with open('data/life.json', 'w') as output:
        json.dump(life, output)
    with open('data/food.json', 'w') as output:
        json.dump(food, output)
    with open('data/culture.json', 'w') as output:
        json.dump(culture, output)
    with open('data/development.json', 'w') as output:
        json.dump(development, output)
    with open('data/services.json', 'w') as output:
        json.dump(services, output)
    with open('data/people.json', 'w') as output:
        json.dump(people, output)


if __name__ == '__main__':
    manager.run()
