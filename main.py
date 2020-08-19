import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from classes.DbConn import *
# import pages 
from pages.login import *
from pages.menu import *
from pages.register import *

class JhtaMatjip(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JhtaMatjip")
        self.setGeometry(100, 100, 800, 600)
        self.show()
        
        
    def route_page(self, page_name):
        if page_name == 'login':
            self.setCentralWidget(Login(self))
        elif page_name == 'menu':
            self.setCentralWidget(Menu(self))
        elif page_name == 'register':
            self.setCentralWidget(Register(self))
        # elif page_mane == '':
        #     self.setCentralWidget()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = JhtaMatjip()
    
    # 첫 화면 실행
    main.route_page('login')

    sys.exit(app.exec_())