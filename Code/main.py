import pygame
from PyQt4 import QtGui, QtCore
from boardGui import create_board_matrix
from boardGui import draw_board
from boardGui import create_Display, board_is_full
import sys
import os
import numpy as np
from PLAYER_turn import PLAYER_takes_turn
from AI_turn import AI_takes_turn
from define import *
global who_player
who_player = "AI"
class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        # Main Screen Window
        self.mainUI()
        self.vbox = QtGui.QWidget(self)
        # Buttons
        self.Buttons()
        self.center()
        self.show()
        self.resultmsg = QtGui.QMessageBox()
        self.resultmsg.setIcon(QtGui.QMessageBox.Information)
        self.resultmsg.hide()

    def Buttons(self):
        self.vbox.setGeometry(QtCore.QRect(50, 50, 600, 300))
        self.verticalLayout = QtGui.QVBoxLayout(self.vbox)
        Easy = QtGui.QPushButton("Easy",self.vbox)
        Medium = QtGui.QPushButton("Medium",self.vbox)
        Hard = QtGui.QPushButton("Hard",self.vbox)
        AI = QtGui.QPushButton("AI",self.vbox)
        You= QtGui.QPushButton("You",self.vbox)
        Save = QtGui.QPushButton("Save",self.vbox)
        Load= QtGui.QPushButton("Load",self.vbox)
        Easy.clicked.connect(self.Easy)
        Medium.clicked.connect(self.Medium)
        Hard.clicked.connect(self.Hard)
        AI.clicked.connect(self.AI)
        You.clicked.connect(self.You)
        Save.clicked.connect(self.Save)
        Load.clicked.connect(self.Load)
        l1 = QtGui.QLabel(self.vbox)
        l2 = QtGui.QLabel(self.vbox)
        l3 = QtGui.QLabel(self.vbox)
        self.verticalLayout.addWidget(l2)
        self.verticalLayout.addWidget(AI)
        self.verticalLayout.addWidget(You)
        self.verticalLayout.addWidget(l1)
        self.verticalLayout.addWidget(Easy)
        self.verticalLayout.addWidget(Medium)
        self.verticalLayout.addWidget(Hard)
        self.verticalLayout.addWidget(l3)
        self.verticalLayout.addWidget(Save)
        self.verticalLayout.addWidget(Load)
        l1.setText("Choose Level Difficulty:")
        l2.setText("Choose Who play First:")
        l3.setText("Save and Load Game:")

    def mainUI(self):
        self.resize(700, 480)
        self.setWindowTitle("Connect4")
        self.center()
    def center(self):
        frameGm = self.frameGeometry()
        screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def Save(self):
        global board
        global who_player
        global game_level
        open('connect4.txt', 'w').close()
        open('connect4_player.txt', 'w').close()
        f= open("connect4.txt","w+")
        np.savetxt('connect4.txt', board,fmt='%d')
        f.close()
        f1=open("connect4_player.txt","w+")
        f1.write(who_player+" ")
        f1.write(str(game_level))
        f1.close()
        pygame.quit()

    def Load(self):
        global board
        global who_player
        global game_level
        board = np.loadtxt('connect4.txt', dtype=int)
        f= open("connect4_player.txt","r")
        f1=f.readline().split(" ")
        who_player=f1[0]
        game_level=int(f1[1])
        print(who_player)
        print(game_level)
        if game_level == 2:
            print("yes")
        f.close()
        unique, counts = np.unique(board, return_counts=True)
        boardBackGround = create_Display(no_rows,no_cols)
        pygame.init()
        draw_board(boardBackGround, board)
        result = ""
        while True:
            try :
                board, winner_flag= PLAYER_takes_turn(board,boardBackGround)
                if winner_flag == 1:
                    result="PLAYER IS THE WINNER"
                    break
                if board_is_full(board):
                    result="Game Over with draw"
                    break
                board, winner_flag = AI_takes_turn(board,boardBackGround,game_level)
                if winner_flag == 1:
                    result="AI IS THE WINNER"
                    break
                if board_is_full(board):
                    result = "Game Over with draw"
                    break
            except:
                break        
        if result!="":
            self.show()
            self.resultmsg.setText(result)
            self.resultmsg.setWindowTitle("Result")
            self.resultmsg.exec_()
            who_player="AI"
            pygame.quit()

    def AI(self):
        global who_player
        who_player="AI"
    def You(self):
        global who_player
        who_player="you"
    def Easy(self):
        global game_level
        game_level=EASY_LEVEL
        self.initGame(EASY_LEVEL)
    def Medium(self):
        global game_level
        game_level=MEDIUM_LEVEL
        self.initGame(MEDIUM_LEVEL)
    def Hard(self):
        global game_level
        game_level=HARD_LEVEL
        self.initGame(HARD_LEVEL)


    def initGame(self,Level):
        global who_player
        global board
        # self.hide()
        board = create_board_matrix(no_rows,no_cols)
        boardBackGround = create_Display(no_rows,no_cols)
        pygame.init()
        draw_board(boardBackGround, board)
        result=""
        if who_player=="AI":
            while True:
                try:
                    board, winner_flag = AI_takes_turn(board,boardBackGround,Level)
                    if winner_flag == 1:
                        result="AI IS THE WINNER"
                        break
                    if board_is_full(board):
                        result = "Game Over with draw"
                        break
                    board, winner_flag= PLAYER_takes_turn(board,boardBackGround)
                    if winner_flag == 1:
                        result="PLAYER IS THE WINNER"
                        break
                    if board_is_full(board):
                        result="Game Over with draw"
                        break
                except:
                    break
        elif who_player=="you":
            while True:
                try:
                    board, winner_flag= PLAYER_takes_turn(board,boardBackGround)
                    if winner_flag == 1:
                        result="PLAYER IS THE WINNER"
                        break
                    if board_is_full(board):
                        result="Game Over with draw"
                        break
                    board, winner_flag = AI_takes_turn(board,boardBackGround,Level)
                    if winner_flag == 1:
                        result="AI IS THE WINNER"
                        break
                    if board_is_full(board):
                        result = "Game Over with draw"
                        break
                except:
                    break
        if result!="" :
            self.show()
            self.resultmsg.setText(result)
            self.resultmsg.setWindowTitle("Result")
            self.resultmsg.exec_()
            who_player="AI"
        pygame.quit()

def main():
    app= QtGui.QApplication(sys.argv)
    QtGui.qApp = app
    GUI= Window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
