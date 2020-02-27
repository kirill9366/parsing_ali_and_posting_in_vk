from vk_api import VkUpload
import requests
from parserali import Ali_parser
import vk_api

class Make_post:
	'''
	создание поста Вконтакте.
	1 аргументом передаем адрес электронной почты или номер
	2 аргументом передаем пароль
	
	есть две функции:
	1) auth - авторизация вконтакте, передавать ничего не надо
	2) create_post - создаем пост,1 аргументом 
	передаем id группы, текст по дефолту идет на русском
	2 аргументом передаем текст, который будет при постинге

	creating a Vkontakte post. 
	1 pass an email address or number as an argument 
	2 pass the password as an argument 

	there are two functions: 
	1) auth - authorization Vkontakte, you do not need to transfer anything 
	2) create_post - create a post with 1 argument 
	we pass the group id, the default text is in Russian 
	2 argument pass the text that will be when posting
	'''
	def __init__(self, username, password):
		self.username = username
		self.password = password
		
	def auth(self):
		'''
		авторизация Вконтакте

		Vkontakte authorization

		'''
		session = requests.Session()
		self.vk_session = vk_api.VkApi(self.username, self.password, api_version = 5.103)
		self.vk_session.auth()
		self.vk = self.vk_session.get_api()

	def create_post(self, group_id, message=None):
		'''
		создаем пост.
		передать id группы со знаком '-' в начале

		creating a post. 
		pass the group id with the '-' sign at the beginning
		
		'''

		session = requests.Session()
		check = ''
		while True:
			try:
				al = Ali_parser()
				url_product = al.get_url()
				data = al.get_data_product(url_product)
			except:
				continue
			attachments = []
			upload = vk_api.VkUpload(self.vk_session)
			image_url = data['url_img']
			if check != image_url:
				check = image_url
			else:
				continue

			image = session.get(image_url, stream=True)
			photo = upload.photo_wall(photos=image.raw, group_id=abs(group_id))[0]
			attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id']))
			if message==None:
				message = '{} \nЦена: {} \nОценка: {} \n{}'.format(data['title'], data['price'], data['quality'], data['url_product'])
			self.vk.wall.post(message=message, owner_id = group_id, from_group=1, attachments=','.join(attachments))
			break

if __name__=='__main__':
	post = Make_post('логин', 'пароль')
	post.auth()
	post.create_post()#Xid группы цифрами передавать типом integer со знаком минус пример: -12613781