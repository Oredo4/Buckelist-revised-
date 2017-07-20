# test_bucketlist.py

import unittest

class BucketlistTests(unittest.TestCase):

    def test_bucketlist_add_new_bucketlist(self):
	"""Tests whether a new bucketlist can be added"""
        response = self.bucketlist('Bucketlist1')
        self.assertEqual(response.status_code, 200)

    def test_bucketlist_existing_bucketlist_name(self):
	"""Tests whether bucketlist added is a duplicate"""
        response = self.bucketlist('Bucketlist1')
		self.assertEqual(response.status_code, 200)
        response = self.bucketlist('Bucketlist1')
		self.assertEqual(response.status_code, 400)

    def test_bucketlist_edit_bucketlist(self):
	"""Tests whether a bucketlist can be edited"""
        response = self.bucketlist('Bucketlist1')
        self.assertEqual(response.status_code, 200)
        response = self.bucketlist('Bucketlist2')
		self.assertEqual(response.status_code, 200)
		
	def test_bucketlist_delete_bucketlist(self):
	"""Tests whether a bucketlist can be deleted"""
        response = self.bucketlist('Bucketlist1')
        self.assertEqual(response.status_code, 200)
        response = self.bucketlist('')
		self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
