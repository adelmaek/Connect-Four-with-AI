from define import *
import random
import math
from boardGui import is_Winning_situation

def addPiecetoMatrixWithoutDrawing(board,col,pieceColor):
    for i in range(no_rows-1,-1,-1):
        if board[i,col] == 0:
            board[i,col] = pieceColor
            break
    return board

def getInCompleteColumns(board):
    inCompleteColumns=[]
    for c in range(no_cols):
        if board[0][c]==0 :
            inCompleteColumns.append(c)
    return inCompleteColumns

def minimax(board, level, maximizingPlayer,alpha,beta,game_level) :
    inCompleteColumns=getInCompleteColumns(board)
    if level == 0 :
        return (None, get_score(board,game_level))
    elif is_Winning_situation(board,PLAYER_PIECE)  :
        return (None, -math.inf)
    elif is_Winning_situation(board,AI_PIECE) :
        return (None, math.inf)
    elif len(getInCompleteColumns(board))==0 :
        return (None,0)
    elif maximizingPlayer :
        bestScore=-math.inf
        chosenColumn = random.choice(inCompleteColumns)
        for c in inCompleteColumns :
            temp = board.copy()
            addPiecetoMatrixWithoutDrawing(temp,c,AI_PIECE)
            newScore= minimax(temp, level-1, False, alpha, beta,game_level)[1]
            if newScore>bestScore:
                bestScore=newScore
                chosenColumn=c
            alpha=max(alpha,bestScore)
            if alpha>=beta :
                break
        return  chosenColumn , bestScore
    else  :
        bestScore=math.inf
        chosenColumn=random.choice(inCompleteColumns)
        for c in inCompleteColumns :
            temp = board.copy()
            addPiecetoMatrixWithoutDrawing(temp,c,PLAYER_PIECE)
            newScore=minimax(temp, level-1, True, alpha, beta,game_level)[1]
            if newScore<bestScore:
                bestScore=newScore
                chosenColumn=c
            beta=min(beta,bestScore)
            if alpha>=beta :
                break
        return  (chosenColumn , bestScore)

def operate_on_line(line,game_level):
    score=0
    if game_level == EASY_LEVEL:
    #Attack score
        if line.count(AI_PIECE)==4 :
            score= 70
        elif line.count(AI_PIECE)==3 and line.count(EMPTY_PLACE)==1:
            score = 30
        elif line.count(AI_PIECE)==2 and line.count(EMPTY_PLACE)==2:
            score= 20
        #Defence score
        elif line.count(PLAYER_PIECE)==4 and line.count(EMPTY_PLACE)==0:
            score= -80
        elif line.count(PLAYER_PIECE)==3 and line.count(EMPTY_PLACE)==1:
            score= -50
        elif line.count(PLAYER_PIECE)==2 and line.count(EMPTY_PLACE)==2:
            score= -30
    elif game_level == MEDIUM_LEVEL:
        if line.count(AI_PIECE)==4 :
            score= 100
        elif line.count(AI_PIECE)==3 and line.count(EMPTY_PLACE)==1:
            score = 20
        elif line.count(AI_PIECE)==2 and line.count(EMPTY_PLACE)==2:
            score= 10
        #Defence score
        elif line.count(PLAYER_PIECE)==4 and line.count(EMPTY_PLACE)==0:
            score= -120
        elif line.count(PLAYER_PIECE)==3 and line.count(EMPTY_PLACE)==1:
            score= -50
        elif line.count(PLAYER_PIECE)==2 and line.count(EMPTY_PLACE)==2:
            score = -30
    elif game_level == HARD_LEVEL:
        if line.count(AI_PIECE)==4 :
            score= 100
        elif line.count(AI_PIECE)==3 and line.count(EMPTY_PLACE)==1:
            score = 20
        elif line.count(AI_PIECE)==2 and line.count(EMPTY_PLACE)==2:
            score= 10
        #Defence score
        elif line.count(PLAYER_PIECE)==4 and line.count(EMPTY_PLACE)==0:
            score= - 100
        elif line.count(PLAYER_PIECE)==3 and line.count(EMPTY_PLACE)==1:
            score= -100
        elif line.count(PLAYER_PIECE)==2 and line.count(EMPTY_PLACE)==2:
            score = -30
    elif game_level == SUPERHARD_LEVEL:
        if line.count(AI_PIECE)==4 :
            score= 100
        elif line.count(AI_PIECE)==3 and line.count(EMPTY_PLACE)==1:
            score = 20
        elif line.count(AI_PIECE)==2 and line.count(EMPTY_PLACE)==2:
            score= 10
        #Defence score
        elif line.count(PLAYER_PIECE)==4 and line.count(EMPTY_PLACE)==0:
            score= -130
        elif line.count(PLAYER_PIECE)==3 and line.count(EMPTY_PLACE)==1:
            score= -110
        elif line.count(PLAYER_PIECE)==2 and line.count(EMPTY_PLACE)==2:
            score = -70
    else:
        print('Error in operate_on_line')
    return score

def get_score(board,game_level):
    totalScore = 0
    # horizontal
    for r in range(no_rows):
        for c in range(no_cols - 3):
            totalScore = totalScore+operate_on_line([board[r][c], board[r][c + 1], board[r][c + 2], board[r][c + 3]], game_level)
    #  vertical
    for c in range(no_cols):
        for r in range(no_rows - 3):
            totalScore = totalScore+operate_on_line([board[r][c], board[r+1][c], board[r+2][c], board[r+3][c]], game_level)
    # diagonal positive
    for c in range(no_cols - 3):
        for r in range(no_rows - 3):
            totalScore = totalScore+operate_on_line([board[r][c], board[r+1][c+1], board[r+2][c+2], board[r+3][c+3]], game_level)

    # diagonal negative
    for c in range(no_cols - 3):
        for r in range(3, no_rows):
            totalScore = totalScore+operate_on_line([board[r][c], board[r-1][c+1], board[r-2][c+2], board[r-3][c+3]], game_level)
    # center column
    if game_level != EASY_LEVEL:
        colCenter = no_cols//2
        for r in range(3, no_rows):
            if board[r][colCenter]==AI_PIECE:
                totalScore=totalScore+5
    return totalScore