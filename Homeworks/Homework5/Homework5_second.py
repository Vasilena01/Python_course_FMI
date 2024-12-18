""" [Title/Звание]
Ultimate Travel Planner

[Description/Обрисовка]
Ultimate Travel Planner е идея за платформа, която помага на потребителите да организират по-лесно
своите ваканции, предоставяйки им цялата основно необходима информация на едно място. 
Приложението ще позволи на потребителите да избират дестинация от списъка с дестинации (държава и град), 
да намират хотели в района, както и популярни забележителности, да създават персонализирани планове,
изброявайки местата, които искат да посетят и да откриват ресторанти и магазини в близост. 
Освен това ще има форум за обмен на съвети и опит между потребителите.

[Functionalities/Надарености]
Функционалности, които Ultimate Travel Planner ще поддържа:
* - допълнителни функционалности
1. Регистрация и вход за потребители.
2. Избор на дестинация от списъка с дестинации.
3. Зареждане на хотели в избрания район чрез външно API.
    * при зареждане на даден хотел може да показва и цени, наличност и рейтинг.
4. Показване на забележителности и атракции в избрания район чрез API (например Google Maps Places API).
5. Създаване на персонализиран план за екскурзията с опция за добавяне на:
    - място за отсядане
    - забележителности, които ще се посетят
6. Форум за потребители за дискусии, съвети и ревюта на дестинации.
7. Съхраняване на планове и списъци с любими места в профила на потребителя.
8.* Възможност за зареждане на ресторанти и магазини в района.

[Milestones/Възлови точки]
1. Модул за вход и регистрация на потребители.
2. Интеграция на API за търсене на хотели, забележителности и *ресторанти.
3. Модул за създаване и редактиране на персонализирани планове за конкретната екскурзия.
4. Форум модул за дискусии.
5. Модул за съхранение на вече направениете планове и списъци с любими места в профила на потребителя.

[Estimate in man-hours/Времеоценка в човекочасове]
Около 80 часа, като най-времеемки ще бъдат интеграцията на API и разработката на форума.

[Usage of technologies/Потребление на технологии]
- основно Django
Външни API:
    - Booking.com API или Expedia API: за информация за хотели.
    - Google Maps Places API: за забележителности, ресторанти и магазини.
    -* Yelp Fusion API: за ревюта и рейтинги на ресторанти и магазини.
    - Форум: Django Rest Framework за API за форума.
    - Геолокация и координати: Geopy за обработка на географски данни.
- HTML, CSS, JavaScript за front-end частта
- GitHub for version control.
"""