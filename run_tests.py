import unittest

#run all tests at once
def run_all_tests():
    loader = unittest.TestLoader()

    suite = loader.discover('test')

    runner = unittest.TextTestRunner()

    runner.run(suite)

if __name__ == '__main__':
    run_all_tests()
