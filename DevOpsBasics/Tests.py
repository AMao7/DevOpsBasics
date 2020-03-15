import unittest
import subprocess


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()


package = 'git'

def query_package(package):
    status = subprocess.getstatusoutput("dpkg-query -W -f='${Status}' " + package)
    if not status[0]:
        print(status[1]) # package is installed
    else:
        print(status[1])


package2 = 'python'

def query_package(package):
    status = subprocess.getstatusoutput("dpkg-query -W -f='${Status}' " + package)
    if not status[0]:
        print(status[1]) # package is installed
    else:
        print(status[1])