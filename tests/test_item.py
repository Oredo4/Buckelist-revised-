# test_item.py

import unittest

class ItemTests(unittest.TestCase):

    def test_item_add_new_item(self):
	"""Tests whether adding item is successful"""
        response = self.item('item1')
        self.assertEqual(response.status_code, 200)

    def test_item_existing_item_name(self):
	"""Tests whether the added item is a duplicate"""
        response = self.item('item1')
		self.assertEqual(response.status_code, 200)
        response = self.item('item1')
		self.assertEqual(response.status_code, 400)

    def test_item_edit_item(self):
	"""Tests whether the items can be edited"""
        response = self.item('item1')
        self.assertEqual(response.status_code, 200)
        response = self.item('item2')
		self.assertEqual(response.status_code, 200)
		
	def test_item_delete_item(self):
	"""Tests whether items can be deleted"""
        response = self.item('item1')
        self.assertEqual(response.status_code, 200)
        response = self.item('')
		self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
