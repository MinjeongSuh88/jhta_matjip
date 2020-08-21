import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import random
import cx_Oracle
from classes.DbConn import *


class Cafe(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.initUI(parent)


    def initUI(self, parent):
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.btn_random = QPushButton("랜덤뽑기 ㅋ", self)
        self.btn_back = QPushButton("뒤로가기", self)
        self.layout.addWidget(self.btn_random, 0, 0)
        self.layout.addWidget(self.btn_back, 0, 1)
        self.maketable()
        self.btn_random.clicked.connect(self.random)
        self.btn_back.clicked.connect(lambda: parent.route_page('menu'))


    def bringdata(self):
        db = DbConn()
        sql = '''
        select r_idx, r_name, site_score, site_review, distance, r_category, price, review 
        from restaurant
        where r_category like '카페%'
        '''
        rows = db.execute(sql)
        # print(rows)
        return rows


    def random(self):
        row = self.bringdata()
        # self.btn_random.setText(row[random.randint(0,len(row))][0])
        QMessageBox.question(self,'결과는 두구두구두구',row[random.randint(0,len(row))][1]+'\n가즈아',QMessageBox.Yes)


    def maketable(self):
        self.table = QTableWidget()
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
            
        row = self.bringdata()

        self.table.setColumnCount(7)
        self.table.setRowCount(len(row))

        self.table.setHorizontalHeaderLabels(['가게명','네이버평점','네이버리뷰수','거리','카테고리','가격','jhta리뷰'])
        # self.table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignRight)
        
        self.layout.addWidget(self.table, 1, 0, 1, 2)
        for i in range(len(row)):
            for j in range(len(row[i])-1):
                self.table.setItem(i,j, QTableWidgetItem(str(row[i][j+1])))
            self.btn = QPushButton('댓글보기',self)
            self.table.setCellWidget(i,6,self.btn)
            self.connect_btn(self.btn,row[i][0])    
        

    def connect_btn(self,btn,idx):
        self.btn.clicked.connect(lambda: self.parent.route_page('cafe_re', idx))
