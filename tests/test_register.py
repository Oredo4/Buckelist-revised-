# test_register.py

import unittest

class RegisterTests(unittest.TestCase):

    def test_register_successful(self):
        """Tests whether registration is successful"""
        response = self.register('oredo4@gmail.com', 'Harambee', 'Harambee')
        self.assertEqual(response.status_code, 201)

    def test_register_different_passwords(self):
        """Tests whether the password entered is correct"""
        response = self.register('oredo4@gmail.com', 'Harambee', 'Harambe')
        self.assertEqual(response.status_code, 400)

    def test_register_email_already_exists(self):
        """Tests whether the user exists"""
        response = self.register('oredo4@gmail.com', 'Harambee', 'Harambee')
        self.assertEqual(response.status_code, 200)
        response = self.register('oredo4@gmail.com', 'Nyayo', 'Nyayo')
        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()
