# Ежедневные праздники

Этот репо парсит праздники и памятные даты на сегодня с сайта [kakoysegodnyaprazdnik.ru](https://kakoysegodnyaprazdnik.ru/). Данные сохраняются в `holidays.json` и обновляются ежедневно через GitHub Actions. Кому надо — берите [прямо отсюда](https://raw.githubusercontent.com/holidaystoday/now/refs/heads/main/holidays.json). Формат простой: `{"holidays": ["Праздник 1", "Праздник 2"]}`.

## Как работает
- Workflow запускается по крону в 21:01 UTC (или вручную).
- Скрипт `parser.py` использует Playwright для загрузки страницы в Chrome, ждёт контент и парсит с selectolax.
- Если JSON изменился — коммитим.

Лол, просто парсим, ничего сложного. Если сломается — фиксь сам.
