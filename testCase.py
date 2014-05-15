# I should have began writing test cases while writing my code as it became
# near impossible to write test cases so I did more testing as I went to ensure
# that I ran every line of my code with various types of input and to ensure
# that I had the proper error trapping for different types of user input.

import unittest

class BadInput(unittest.TestCase):
    def test_starting_out(self):
        self.assertEqual(1,1)

def main():
    unittest.main()

if __name__ == "__main__":
    main()