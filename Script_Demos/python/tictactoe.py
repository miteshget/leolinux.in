#!/usr/local/bin/python3
# Author : LEOxian 
# License: GPLv2
# Description: Tic Tac Toe Game
# Date : 23-March-2013


from asyncio import run_coroutine_threadsafe
import os
import re

cell=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
default_players = [{"id": 0, "name": "Player-1", "symbol": "\33[91mX\33[0m"},{"id": 1, "name": "Player-2", "symbol": "\33[92mO\33[0m"}]
board_input_msg = "Enter the one number as appeared in the board"
run_count = 0 
error_msg = ""

def board():
    os.system("clear")
    print("\n")
    for i in range(1,9,3):
        print("\t %s | %s | %s" % (cell[i], cell[i+1], cell[i+2]))
        if i < 6:
            print("\t___________")
    # print("\n")

def winning_algorithm(id):
    for i in range(1,9,3):
        if cell[i] == default_players[id]["symbol"] and cell[i+1] == default_players[id]["symbol"] and  cell[i+2] == default_players[id]["symbol"]:
            board()
            quit("\33[32mCongratulation! " + default_players[id]["name"] +", You won the game\33[0m\n" )
    for i in range(1,4):
        if cell[i] == default_players[id]["symbol"] and cell[i+3] == default_players[id]["symbol"] and  cell[i+6] == default_players[id]["symbol"]:
            board()
            quit("\33[32mCongratulation! " + default_players[id]["name"] +", You won the game\33[0m\n" )
    if cell[1] == default_players[id]["symbol"] and cell[5] == default_players[id]["symbol"] and  cell[9] == default_players[id]["symbol"]:
        board()
        quit("\33[32mCongratulation! " + default_players[id]["name"] +", You won the game\33[0m\n" )
    if cell[3] == default_players[id]["symbol"] and cell[5] == default_players[id]["symbol"] and  cell[7] == default_players[id]["symbol"]:
        board()
        quit("\33[32mCongratulation! " + default_players[id]["name"] +", You won the game\33[0m\n" )
        
def update_default_players():
    print("Enter player's name - ")
    print("_____________________")
    for pid in range(0,2):
        pname = input("\t" + default_players[pid]["name"] + " enter name: ")
        if len(pname) != 0:
            default_players[pid]["name"] = pname         

def validate_board_input(cellno):
    global error_msg
    if len(cellno) == 0:
        error_msg = "\33[91mError: Null is invalid \33[0m" 
        return False
    if len(cellno) > 2:
        error_msg = "\33[91mError: Invalid input \33[0m" 
        return False
    # special_char = re.compile('[@_!$%^&*()<>?/\|}{~:]#`"\'')
    # if special_char.search(cellno) != None:
    #     error_msg = "\33[91mError: Special Characters are not allowed\33[0m"
    #     return False
    if cellno.isalpha():
        error_msg = "\33[91mError: Alpha is invalid \33[0m"
        return False
    if int(cellno) not in cell:
        error_msg = "\33[91mError: Wrong number provided \33[0m"
        return False
    error_msg = ""
    return True
    
def update_board(id):
    global run_count
    run_count += 1
    if run_count > 3:
        exit("\n\33[91mNo of attempts exceeded\33[0m\n")
    print("\n" + error_msg)
    cellno = input("[ " + board_input_msg + " ]\n" + "|-> " + "\33[36m" + default_players[id]["name"] +" \33[0m" + " [Type and Press Enter] >> ")
    if bool(validate_board_input(cellno)):
        cell[int(cellno)] = default_players[id]["symbol"]
        run_count = 0
        winning_algorithm(id)
        return True
    else:
      update_board(id)

def main():
    # board()
    os.system("clear")
    print("\33[36m\nWelcome to Tic Tac Toe Game")
    print("This is two players cli game")
    print("Kindly follow the instructions to play\33[0m\n")
    update_default_players()
    while True:
        for i in range(2):
            board()
            update_board(i)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        os.system("clear")
        print("\33[96m\nThanks you for playing Tic Tac Toe Game\nSee you soon!\n\n\t-Mitesh The Mouse\33[0m\n")
