import requests
from time import sleep
from bs4 import BeautifulSoup as bs
from selenium import webdriver


class Ali_parser:

	def get_url(self):
		'''
		получаем url на первый товар в списке, используется для того,
		чтобы постились рандомные товары

		get the url for the first item in the list, used to, 
		to fast random products

		'''
		headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36/(KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36 OPR/60.0.3255.95"}
		session = requests.Session()
		page = session.get('https://best.aliexpress.ru/?lan=ru', headers= headers, timeout=(3, 10))
		soup = bs(page.content, 'html.parser')
		first_product = soup.find('li', attrs={'class':'first'})
		self.product_url = 'https:' + first_product.find('a')['href']
		self.img_url = 'https:' + first_product.find('img')['data-best']
		return self.product_url

	def get_data_product(self, url_product):
		'''
		парсим данные товара, указывается сразу ссылка на товар.
		используется  selenium, размещать chromedriver.exe в одной папке 
		с данным файлом

		в случае, если выйдет 'Please, using VPN' это означает то, что 
		при парсинге ссылки, вместо товара вышла страница авторизации, 
		это фиксится использованием VPN

		parse the product data, specify the link to the product immediately.
		used by selenium, chromedriver.ru in one folder 
		with this file 

		if 'Please, using VPN' is released, this means that 
		when parsing a link, an authorization page appeared instead of the product, 
		this is fixed by using a VPN

		'''
		chromedriver = 'chromedriver.exe'
		options = webdriver.ChromeOptions()
		options.add_argument('headless') 
		driver = webdriver.Chrome(executable_path=chromedriver,options=options)
		driver.get(url_product)
		try:
			title = driver.find_element_by_class_name('product-title').text
		except:
			return 'Please, using VPN'
		try:
			quality = driver.find_element_by_class_name('overview-rating-average').text
		except:
			quality = '0.0'
		price = driver.find_element_by_class_name('product-price-value').text
		data_product = {'url_img': self.img_url, 'url_product': url_product, 'title':title, 'quality':quality, 'price':price}
		return data_product


if __name__ == '__main__':
	al = Ali_parser()
	url_product = al.get_url()
	print(url_product)
	data = al.get_data_product(url_product)
	print(data['url_img'])
