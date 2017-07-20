# test_login.py

import unittest

class LoginTests(unittest.TestCase):

	def test_login_successful(self):
		"""Tests whether the login was successful"""
		response = self.login('oredo4@gmail.com', 'Harambee')
		self.assertEqual(response.status_code, 200)
		
	def test_login_nonexistent_credentials(self):
		"""Tests whether both credentials were entered"""
		response = self.login('','')
		self.assertEqual(response.status_code, 400)
		
	def test_login_wrong_credentials(self):
		"""Tests whether the user entered correct credentials"""
		response = self.login('oredo4@gmail.com','')
		self.assertEqual(response.status_code, 400)
		
		response2 = self.login('', 'Harambee')
		self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()
