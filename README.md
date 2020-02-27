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
<li>url_product - ссылка на сам товар.
<li>title - название товара
<li>quality - оценка товара
<li>price - цена тоара, в рублях


POSTING_IN_VK.PY
###

Этот же файл использует библиотек: [vk_api](https://pypi.org/project/vk-api/), [requests](https://pypi.org/project/requests/).
<br>

Определяется класс Make_post, в который первым аргументом передается номер телефона или же электронная почта от вашего аккаунта Вконтаке, а во второй пароль.

Внутренние функциии:

`auth` - выполняется авторизация на основе переданныых данных в класс.
<br>

`create_post`- создание поста в группе, к которой у вас есть доступ. Единственный аргумент, который нужно передать это id группы(сообщества) со знаком минус в начале.

---------------
# Introduction.


This project was created by me in order to make an autopost in the social network Vkontakte. 
Later, this project should be expanded, both for link parsing and for parsing extension
data about the product.


PARSERALI.PY
###

This file uses libraries such as [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/), as well as the library [Selenium](https://pypi.org/project/selenium/).
<br>
The Ali_parser class is defined and nothing is passed to It.

Internal function::

`get_url` - collects a link to the product from the main page, as well as a link to a photo of the product, which is then transmitted
functions `get_data_product`, as a rule, you don't need to pass anything to the function.
<br>
Returns a link to the product.

`get_data_product` - collects product data using the library's resources [Selenium](https://pypi.org/project/selenium/), since the data on the page is passed through js, which is loaded later and get the data through the same [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) quite difficult.
<br>
You don't need to send anything.
<br>
Returns a dictionary with information about the product. In certainty this is:

<br>

<li>url_img - link to the product image.
<li>url_product - link to the product itself.
<li>title - name of item.
<li>quality - evaluation of the product.
<li>price - toar price, in rubles.


POSTING_IN_VK.PY
###

This same file uses libraries: [vk_api](https://pypi.org/project/vk-api/), [requests](https://pypi.org/project/requests/).
<br>

The Make_post class is defined, in which the first argument is passed to the phone number or email from your Vvcontake account, but the second password.

Internal functions:

`auth` - authorization is performed based on the data passed to the class.
<br>

`create_post`- creating a post in a group that you have access to. The only argument to pass is the group(community) id with a minus sign at the beginning.






























