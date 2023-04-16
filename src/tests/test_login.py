from src import settings
from src.tests.base_test import BaseTest
from src.utility import xlReader


class TestLogin(BaseTest):

    def test_valid_login(self):
        xlReader.load_excel()
        username = xlReader.get_cell_data(14, 5)
        password = xlReader.get_cell_data(15, 5)
        # launch url
        self.loginPage.login(username, password)          
                    
    def test_invalid_login(self):
        xlReader.load_excel()
        username = xlReader.get_cell_data(17, 5)
        password = xlReader.get_cell_data(18, 5)
        self.loginPage.login(username, password)
        # self.homePage.wait_for_product_text()
        assert "Thông tin đăng nhập không hợp lệ." \
            in self.loginPage.get_locked_error_text()
                
    def test_invalid_email(self):
        xlReader.load_excel()
        username = xlReader.get_cell_data(17, 5)
        password = xlReader.get_cell_data(18, 5)
        self.loginPage.login(username, password)
        # self.homePage.wait_for_product_text()
        assert "Yêu cầu không hợp lệ, hoặc quá hạn, phiền bạn thử lại" \
            in self.loginPage.get_locked_error_text()
        
    def test_invalid_phone(self):
        xlReader.load_excel()
        username = xlReader.get_cell_data(17, 5)
        password = xlReader.get_cell_data(18, 5)
        self.loginPage.login(username, password)
        # self.homePage.wait_for_product_text()
        assert "Số điện thoại không hợp lệ." \
            in self.loginPage.get_locked_error_text()
