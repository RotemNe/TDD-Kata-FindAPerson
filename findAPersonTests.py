


import unittest 
from crowdMap import Crowdmap



class FindAPersonTestes(unittest.TestCase):
	def setUp(self):
		self.crowdmap=Crowdmap()

 	def test_getAllPostsForName(self):
 		posts=self.crowdmap.get_all_posts_for("Or")
 		self.assertIn("Or",posts)

 	def test_getAllPostsForMissingName(self):
 		posts=self.crowdmap.get_all_posts_for("Or1")
 		self.assertNotIn("Or2",posts)



if __name__ == '__main__':
	unittest.main();
