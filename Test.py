'''
 This is the sample of use demonstration for testing windows desktop apps using:
  - Selenium webdriver with unittest test wrapper
  - Winium.Desktop.Driver standalone server that runs app on local host
  - Windows Detective and Swapy are helpers used for fetching specific app control identifiers
'''

import unittest
from selenium import webdriver


class TestDesktopApp(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Remote(command_executor='http://localhost:9999',
                                       desired_capabilities={'app': 'C:\\Windows\\System32\\notepad.exe'})

    def test(self):

        editTextField = self.driver.find_element_by_name('Edit')
        editTextField.send_keys('Text in editor input field')
        assert 'Text in editor input field' in editTextField.__getattribute__('value')

        self.driver.find_element_by_name('Cancel').click()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
