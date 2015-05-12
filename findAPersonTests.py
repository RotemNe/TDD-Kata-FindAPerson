


import unittest 
from crowdMap import Crowdmap



class FindAPersonTestes(unittest.TestCase):
	def setUp(self):
		self.crowdmap=Crowdmap( ["I met Or A. at Chabad house Bangkok", "We found Or A. R.I.P at Langtang valley"])

 	def test_getAllPostsForName(self):
 		posts=self.crowdmap.get_all_posts_for("Or")
 		self.assertEquals( ["I met Or A. at Chabad house Bangkok", "We found Or A. R.I.P at Langtang valley"],posts)

 	def test_getAllPostsForMissingName(self):
 		posts=self.crowdmap.get_all_posts_for("Joe")
 		self.assertEquals( [],posts)


if __name__ == '__main__':
	unittest.main();
