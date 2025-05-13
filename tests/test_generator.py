"""
Tests for the test data generator module.
"""

import unittest
from snowflake_util.generator import generate_test_data, random_email

class TestGenerator(unittest.TestCase):
    """Test cases for the test data generator."""
    
    def test_generate_test_data_count(self):
        """Test that the correct number of entries are generated."""
        # Test with default count (1)
        data = generate_test_data()
        self.assertEqual(len(data), 1)
        
        # Test with specific count
        count = 5
        data = generate_test_data(count)
        self.assertEqual(len(data), count)
    
    def test_generate_test_data_structure(self):
        """Test that the generated data has the correct structure."""
        data = generate_test_data(1)[0]
        
        # Check that all required fields are present
        self.assertIn("first_name", data)
        self.assertIn("last_name", data)
        self.assertIn("email", data)
        self.assertIn("company", data)
        self.assertIn("job_title", data)
        
        # Check that fields are non-empty
        self.assertTrue(data["first_name"])
        self.assertTrue(data["last_name"])
        self.assertTrue(data["email"])
        self.assertTrue(data["company"])
        self.assertTrue(data["job_title"])
    
    def test_random_email(self):
        """Test that random email generation works correctly."""
        first_name = "Test"
        last_name = "User"
        
        # Generate multiple emails to test randomness
        emails = [random_email(first_name, last_name) for _ in range(5)]
        
        # Check that all emails are valid
        for email in emails:
            self.assertIn("@", email)
            self.assertTrue(email.endswith(".com") or 
                          email.endswith(".org") or 
                          email.endswith(".net") or 
                          email.endswith(".io") or 
                          email.endswith(".co") or 
                          email.endswith(".dev"))
            
            # Check that email contains first or last name
            self.assertTrue(
                first_name.lower() in email.split("@")[0].lower() or 
                last_name.lower() in email.split("@")[0].lower()
            )

if __name__ == "__main__":
    unittest.main()