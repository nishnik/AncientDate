""" Test AncientDate"""

import unittest
from AncientDate import *

class TestAncientDate(unittest.TestCase):
	"""Class for unittest"""
	def test_single_date1(self):
		""" Single Date Format #1"""
		d = AncientDate()
		d.parse("A.D. 3")
		self.assertTrue(d.year_first.isAD)
		self.assertFalse(d.year_first.isBC)
		self.assertFalse(d.year_first.isPost)
		self.assertFalse(d.year_first.isAnte)
		self.assertFalse(d.year_first.isProblematical)
		self.assertEqual(d.year_first.val, "3")
		self.assertFalse(d.isRange)

	def test_single_date2(self):
		""" Single Date Format #2"""
		d = AncientDate()
		d.parse("3 B.C.")
		self.assertFalse(d.year_first.isAD)
		self.assertTrue(d.year_first.isBC)
		self.assertFalse(d.year_first.isPost)
		self.assertFalse(d.year_first.isAnte)
		self.assertFalse(d.year_first.isProblematical)
		self.assertEqual(d.year_first.val, "3")

	def test_multiple_date1(self):
		""" Multiple Date Format #1"""
		d = AncientDate()
		d.parse("A.D. 2/3")
		self.assertTrue(d.isRange)
		self.assertTrue(d.year_first.isAD)
		self.assertFalse(d.year_first.isBC)
		self.assertFalse(d.year_first.isPost)
		self.assertFalse(d.year_first.isAnte)
		self.assertFalse(d.year_first.isProblematical)
		self.assertEqual(d.year_first.val, "2")

		self.assertTrue(d.year_second.isAD)
		self.assertFalse(d.year_second.isBC)
		self.assertFalse(d.year_second.isPost)
		self.assertFalse(d.year_second.isAnte)
		self.assertFalse(d.year_second.isProblematical)
		self.assertEqual(d.year_second.val, "3")

	def test_multiple_date2(self):
		""" Multiple Date Format #2"""
		d = AncientDate()
		d.parse("2 B.C.-A.D. 4")
		self.assertTrue(d.isRange)
		self.assertFalse(d.year_first.isAD)
		self.assertTrue(d.year_first.isBC)
		self.assertFalse(d.year_first.isPost)
		self.assertFalse(d.year_first.isAnte)
		self.assertFalse(d.year_first.isProblematical)
		self.assertEqual(d.year_first.val, "2")

		self.assertTrue(d.year_second.isAD)
		self.assertFalse(d.year_second.isBC)
		self.assertFalse(d.year_second.isPost)
		self.assertFalse(d.year_second.isAnte)
		self.assertFalse(d.year_second.isProblematical)
		self.assertEqual(d.year_second.val, "4")

	def test_poste_ante(self):
		""" Poste and Ante dates"""
		d = AncientDate()
		d.parse("p. 4 B.C./a. A.D. 2 ")
		self.assertTrue(d.isRange)
		self.assertFalse(d.year_first.isAD)
		self.assertTrue(d.year_first.isBC)
		self.assertTrue(d.year_first.isPost)
		self.assertFalse(d.year_first.isAnte)
		self.assertFalse(d.year_first.isProblematical)
		self.assertEqual(d.year_first.val, "4")

		self.assertTrue(d.year_second.isAD)
		self.assertFalse(d.year_second.isBC)
		self.assertFalse(d.year_second.isPost)
		self.assertTrue(d.year_second.isAnte)
		self.assertFalse(d.year_second.isProblematical)
		self.assertEqual(d.year_second.val, "2")

	def test_problematical(self):
		""" Problematical Dates"""
		d = AncientDate()
		d.parse("A.D. 12?")
		self.assertTrue(d.year_first.isAD)
		self.assertFalse(d.year_first.isBC)
		self.assertFalse(d.year_first.isPost)
		self.assertFalse(d.year_first.isAnte)
		self.assertTrue(d.year_first.isProblematical)
		self.assertEqual(d.year_first.val, "12")
		self.assertFalse(d.isRange)