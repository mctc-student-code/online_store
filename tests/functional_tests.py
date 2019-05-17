import selenium
import re,time
from selenium import webdriver

from django.test import LiveServerTestCase

class HomePageTest(LiveServerTestCase):

    def  setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_title_shown_on_home_page(self):
        self.browser.get(self.live_server_url)
        assert 'Welcome to Z Toys Store' in self.browser.title
        assert 'Our Products Collection' in self.browser.page_source


class BrowseCategories(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)


    def tearDown(self):
        self.browser.quit()

    def test_browsing_categories(self):
        # Start on home page
        self.browser.get(self.live_server_url)
        self.browser.implicitly_wait(3)
        shop_navbar_link=self.browser.find_element_by_id('navbarDropdown')
        shop_navbar_link.click()
        categories = ['For Boys', 'For Girls']
        categories_divs = self.browser.find_elements_by_id('specific_category')
        for category, div in zip(categories,categories_divs):
            assert category in div.text
            for_boys = self.browser.find_element_by_link_text('For Boys')
            for_boys.click()
            assert '/shop/boys/' in self.browser.current_url
        all_products = self.browser.find_element_by_id('all_products')
        all_products.click()
        assert '/shop/' in self.browser.current_url



