import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import urllib
import platform



class ClothingItem:
	"""
	Stores the name, description,price, and link to an image for an item, as well as a method that prints all of this information.
	"""
	def __init__(self, name, description, price, picture):
		self.name = name
		self.description = description
		self.price = price
		self.picture = picture

	def get_Info(self):
		"""
		Prints item's info
		"""
		print(self.description + " " + self.name + " " + self.price + " " + self.picture)



class SearchObj:
	"""
	Serves as a tool for searching through html and creating a list of products with the html
	"""
	def __init__(self):
		if platform.system() == 'Windows':
			cDriver = './chromedriver.exe'
		else:
			cDriver = './chromedriver'
		op = webdriver.ChromeOptions()
		op.add_argument('headless')
		self.driver = webdriver.Chrome(cDriver, options=op)
		self.imgdriver = webdriver.Chrome(cDriver)

	def find_items(self, text,images, amount):
		"""
		Creates a list of ClothingItem objects

		inputs:
		text - the html
		images - list of image objects created by Beautiful soup
		amount - amount of items to be created in the list

		ouput:
		The list of ClothingItem objects
		"""
		item_list = []
		more_items = True
		last_index = 0
		while more_items and len(item_list) < amount:
			cardIndex = text.find('product-card css-pm7x6j css-z5nr6i css-11ziap1 css-zk7jxt css-dpr2cn product-grid__card', last_index)

			#finds the name
			nameStart = text.find('product-card__subtitle\">',cardIndex+1)
			nameEnd = text.find('<', nameStart)
			name = text[(nameStart + 24): nameEnd]
	
			#finds the description
			descriptionI = text.find('\"product-card__title\"', cardIndex+1)
			descriptionStart = text.find('>', descriptionI)
			descriptionEnd = text.find('<', descriptionStart)
			description = text[descriptionStart+1 : descriptionEnd]
	
			#finds the price
			priceI = text.find('\"product-price\"', cardIndex+1)
			priceStart = text.find('>', priceI)
			priceEnd = text.find('<', priceStart)
			price = text[priceStart+1 : priceEnd]
	
			#finds the image
			picture = "not found"
			for image in images:
				if image.get_attribute('alt') == description + ' ' + name:
					picture = image.get_attribute('src')
	
			item = ClothingItem(name, description, price, picture)
			item_list.append(item)
	
			last_index = cardIndex + 1
			cardIndex = text.find('product-card css-pm7x6j css-z5nr6i css-11ziap1 css-zk7jxt css-dpr2cn product-grid__card', last_index)
			if cardIndex == -1:
				more_items = False
		return item_list
	
	def search(self, text, store, amount):
		"""
		Creates a link to the Nike website, to be parsed by Beautiful soup, creates and displays the image of each item found with the search method

		inputs:
		text - search criteria
		store - what store to be searched, will always be Nike
		amount - amount of items to be found per search

		output:
		The list of items
		"""
		if store == "nike":
			URL = 'https://www.nike.com/w?q=' + text.replace(' ', '%20') + '&vst=' + text.replace(' ', '%20')
		page = requests.get(URL)
	
		soup = BeautifulSoup(page.text, 'html.parser')
	
		text_html = str(soup)
		self.driver.get(URL)
		
		images = self.driver.find_elements_by_tag_name('img')
		
		items = self.find_items(text_html,images, amount)
		for item in items:
			#item.get_Info()
			self.imgdriver.get(item.picture)
		return items


	def close(self):
		"""
		closes the instances of chromedriver
		"""
		self.imgdriver.quit()
		self.driver.quit()