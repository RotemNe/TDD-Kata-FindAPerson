


import unittest 

class Crowdmap(object):
 	def get_all_posts_for(self,param):
 		pass

class FindAPersonTestes(unittest.TestCase):
	def setUp(self):
		self.crowdmap=Crowdmap()

 	def test_getAllPostsForName(self):
 		posts=self.crowdmap.get_all_posts_for("Or")
 		self.assertFalse("Or",posts)



if __name__ == '__main__':
	unittest.main();