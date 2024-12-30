import unittest
import subprocess

class TestVersions(unittest.TestCase):
    def test_git_version(self):
        result = subprocess.run(['git', '--version'], stdout=subprocess.PIPE, text=True)
        self.assertIn('git version', result.stdout)

    def test_python_version(self):
        result = subprocess.run(['python', '--version'], stdout=subprocess.PIPE, text=True)
        self.assertIn('Python', result.stdout)

if __name__ == '__main__':
    unittest.main()