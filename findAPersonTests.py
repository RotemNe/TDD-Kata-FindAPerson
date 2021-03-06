


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

 	def test_existingLocationInformationReturnsTrue(self):
 		location_Exist=self.crowdmap.is_location_for_name("Or")
 		self.assertTrue(location_Exist)

 	def test_missingLocationInformationReturnsFalse(self):
 		location_exist=self.crowdmap.is_location_for_name("Lassy")
 		self.assertFalse(location_exist)

 	def test_mapInconsistenciesExistReturnsTrue(self):
 		mapInconsiste=self.crowdmap.mapInconsistenciesExist("Or")
 		self.assertTrue(mapInconsiste)

 	def test_mapInconsistenciesExistReturnsFalse(self):
 		mapInconsiste=self.crowdmap.mapInconsistenciesExist("Lassy")
 		self.assertFalse(mapInconsiste)

if __name__ == '__main__':
	unittest.main();
