
from locationService import locationService

class Crowdmap(object):
	def __init__(self,init_list):
		self.list=init_list

 	def get_all_posts_for(self,name):
 		 return [post for post in self.list if post.find(name)!=-1]

 	def is_location_for_name(self,name):	
 		locationsList=locationService().getLocations()
 		postList= self.get_all_posts_for(name)
 		for post in postList:
 			for location in locationsList:
 				if location in post:
 					return True
 		return False

 	def mapInconsistenciesExist(self,name):
 		postList= self.get_all_posts_for(name)
 		locationsList = locationService().getLocations()
 		appearnces =0
 		for post in postList:
 			for location in locationsList:
 				if location in post:
 					appearnces+=1

 		if appearnces >1:
 			return True
 		return False