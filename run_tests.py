import unittest
import sys

def run_tests():
    """Run all test cases and return True if all tests pass"""
    # Discover and run tests
    loader = unittest.TestLoader()
    start_dir = 'tests'
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    # Run tests with verbosity=2 for detailed output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return True if tests passed, False otherwise
    return result.wasSuccessful()

if __name__ == '__main__':
    # Run tests and use the result as exit code
    # Exit code 0 means all tests passed
    sys.exit(not run_tests())