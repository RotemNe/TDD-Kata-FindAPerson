
from locationService import locationService

class Crowdmap(object):
	def __init__(self,init_list):
		self.list=init_list

 	def get_all_posts_for(self,name):
 		 return [post for post in self.list if post.find(name)!=-1]

 	def is_location_for_name(self,name):	
 		locations=locationService().getLocations()
 		posts= self.get_all_posts_for(name)
 		for post in posts:
 			for location in locations:
 				if location in post:
 					return True
 		return False