from Scraper import SearchObj

class User():
	"""
	Holds all preferences, as well as ways to update and find items based on these preferences.
	"""

	def __init__(self):
		self.priceRange = [0, 500]
		#General preferences
		self.preferences = {
			'item' : {},
			'color' : {},
			'style' : {},
			'price' : [],
		}
		#preferences that are item specific
		self.itemPreferences = {
			'hat' : {'color' : {}, 'style' : {}, 'price' : []},
			'shirt' : {'color' : {}, 'style' : {}, 'price' : []},
			'pants' : {'color' : {}, 'style' : {}, 'price' : []},
			'shorts' : {'color' : {}, 'style' : {}, 'price' : []},
			'shoes' : {'color' : {}, 'style' : {}, 'price' : []}

		}

	def add_pref(self, pref, prefType, item=None):
		"""
		adds to the user's preferences

		inputs:
		pref - the preference itself (ie:'blue')
		prefType - the preference type (ie:'color')
		item - if the preference is item specific, this is the item
		"""
		if item == None:
			try:
				self.preferences[prefType][pref] += 1
			except:
				try:
					self.preferences[prefType][pref] = 1
				except:
					self.preferences[prefType].append(pref)
			if prefType == 'price':
				for price in self.preferences['price']:
					if price < self.priceRange[0]:
						self.priceRange[0] = price
					if price > self.priceRange[1]:
						self.priceRange[1] = price
		else:
			try:
				self.itemPreferences[item][prefType][pref] += 1
			except:
				try:
					self.itemPreferences[item][prefType][pref] = 1
				except:
					self.itemPreferences[item][prefType].append(pref)


	def get_pref(self, prefType, item=None):
		"""
		Gets a preference from user data

		inputs:
		prefType - the preference type (ie:'color')
		item - if item specific, the item
		"""
		if item == None:
			return self.preferences[prefType]
		else:
			return self.itemPreferences[item][prefType]

	def get_recom_items(self, amount):
		"""
		Generates and displays a generic list of recommended items

		input:
		amount - how many items per specific preference combination
		"""
		finder = SearchObj()
		for testItems in self.preferences['item']:
			for testColors in self.preferences['color']:
				
				items = finder.search(testColors + " " + testItems, 'nike', amount)

				for item in items:
					price = float(item.price.replace('$',''))
					if price in range(self.priceRange[0], self.priceRange[1]+50):
						item.get_Info()
		finder.close()

	def get_recom_perItem(self, itemType, amount):
		"""
		Generates and displays an item specific list of recommended items

		input:
		itemType - the type of item to be searched
		amount - how many items to be displayed per preference combination
		"""
		finder = SearchObj()
		for testItems in self.itemPreferences[itemType]['color']:
			items = finder.search(testItems + " " + itemType, 'nike', amount)

			for item in items:
				price = float(item.price.replace('$',''))
				if price in range(self.priceRange[0], self.priceRange[1]+50):
					item.get_Info()


		finder.close()