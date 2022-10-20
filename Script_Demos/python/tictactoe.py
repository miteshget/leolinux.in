#!/usr/local/bin/python3
# Author : LEOxian 
# License: GPLv2
# Description: Tic Tac Toe Game
# Date : 23-March-2013


from asyncio import run_coroutine_threadsafe
import os
import re
from time import sleep

code_normal = "\33[0m"
code_red = "\33[31m"
code_green = "\33[32m"
code_yellow = "\33[33m"
code_blue = "\33[34m"
code_pink = "\33[35m"
code_megenta= "\33[36m"

cell=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
default_players = [
    {
        "id": 0,
        "name": code_pink + "Player-1" + code_normal,
        "symbol": "X" },
    {
        "id": 1,
        "name": code_megenta + "Player-2" + code_normal,
        "symbol": "O"}
    ]
board_input_msg = code_yellow + "Enter the one number as appeared in the board" + code_normal
run_count = 0 
error_msg = ""
win_msg = code_green + " Congratulation!, You won the game\n" + code_normal
welcome_msg =  code_yellow + '''
____________________________________________________
|                                                   |
 |      Welcome to Tic Tac Toe Game\t\t     |
  |     This is two players cli game\t\t      |
   |    Kindly follow the instructions to play\t       |
    |                                                   |
     ----------------------------------------------------
''' + code_normal

exit_msg = code_yellow + "\nThanks you for playing Tic Tac Toe Game\nSee you soon!\n\n\t-Mitesh The Mouse\n" + code_normal

def board():
    os.system("clear")
    print("\n")
    for i in range(1,9,3):
        if cell[i] == "X":
            cell1 = code_pink + cell[i] + code_normal
        elif cell[i] == "O":
            cell1 = code_megenta + cell[i] + code_normal
        else:
            cell1 = cell[i]
        if cell[i+1] == "X":
            cell2 = code_pink + cell[i+1] + code_normal
        elif cell[i+1] == "O":
            cell2 = code_megenta + cell[i+1] + code_normal
        else:
            cell2 = cell[i+1]
        if cell[i+2] == "X":
            cell3 = code_pink + cell[i+2] + code_normal
        elif cell[i+2] == "O":
            cell3 = code_megenta + cell[i+2] + code_normal
        else:
            cell3 = cell[i+2]
        print("\t %s | %s | %s" % ( cell1, cell2, cell3))
        if i < 6:
            print("\t___________")

def winning_algorithm(id):
    for i in range(1,9,3):
        if cell[i] == default_players[id]["symbol"] and cell[i+1] == default_players[id]["symbol"] and  cell[i+2] == default_players[id]["symbol"]:
            board()
            print("\n" + default_players[id]["name"] + win_msg )
            quit(exit_msg)
    for i in range(1,4):
        if cell[i] == default_players[id]["symbol"] and cell[i+3] == default_players[id]["symbol"] and  cell[i+6] == default_players[id]["symbol"]:
            board()
            print("\n" + default_players[id]["name"] + win_msg )
            quit(exit_msg)
    if cell[1] == default_players[id]["symbol"] and cell[5] == default_players[id]["symbol"] and  cell[9] == default_players[id]["symbol"]:
        board()
        print("\n" + default_players[id]["name"] + win_msg )
        quit(exit_msg)
    if cell[3] == default_players[id]["symbol"] and cell[5] == default_players[id]["symbol"] and  cell[7] == default_players[id]["symbol"]:
        board()
        print("\n" + default_players[id]["name"] + win_msg )
        quit(exit_msg)
        
def draw_algorithm():
    check_numbers = re.compile('[123456789]')
    print(cell)
    if check_numbers.search(''.join(cell)) == None:
        board()
        print("\n" + code_red + "Game Over! No one won." + code_normal)
        quit(exit_msg)
    
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
    if cellno.isalpha():
        error_msg = "\33[91mError: Alpha is not allowed \33[0m"
        return False
    check_numbers = re.compile('[123456789]')
    if check_numbers.search(cellno) == None:
        error_msg = "\33[91mError: Characters are not allowed \33[0m"
        return False
    if cellno not in cell:
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
        draw_algorithm()
        return True
    else:
      update_board(id)

def main():
    # board()
    os.system("clear")
    print(welcome_msg)
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
        print(exit_msg)
