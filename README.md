# parsing_ali_and_posting_in_vk
собирает информацию о товаре и постит ее во Вконтакте

`English version below`

# Вступление.

Данный проект создавался мной для того, чтобы делать автопост в социальную сеть Вконтакте. 
Позже данный проект должен расширяться, как разнообразие парсинга ссылок, так и для расширения парсинга
данных о товаре.

PARSERALI.PY
###

Данный файл использует такие библиотеки, как [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/), а также библиотеку [Selenium](https://pypi.org/project/selenium/).
<br>
Определяется класс Ali_parser, в который ничего не передается.

Внутренние функции:

`get_url` - собирает ссылку на товар с главной страницы, а также ссылку на фото товара, которые дальше передаются
функции `get_data_product`, как правило передавать в функцию ничего не надо.
<br>
Возвращает ссылку на товар.

`get_data_product` - собирает данные о товаре по средствам библиотеки [Selenium](https://pypi.org/project/selenium/), т.к. данные на страницу передаются через js, который подгружается позже и получить данные через тот же [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) достаточно сложно. 
<br>
Передавать ничего не нужно.
<br>
Возвращает словарь с данными о товаре. В определенности это:
<br>

<li>url_img - ссылка на картинку товара.
<li>
url_product - ссылка на сам товар.
<li>
title - название товара

