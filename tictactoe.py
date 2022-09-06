print("Welcome to Tic tac toe")

list = ["-","-","-","-","-","-","-","-","-"]
bool = True
player = "X"
num = 2
#start of methods
def board():
    print(list[0] +"|"+list[1] +"|"+list[2])
    print(list[3] +"|"+list[4] +"|"+list[5])
    print(list[6] +"|"+list[7] +"|"+list[8])

def filling(input):
    global num
    global player
    list[int(input)] = player
    num += 1
    if num % 2 == 0:
        player = "X"
    else:
        player = "O"

def current_player():
    global player
    print("current player is : {}".format(player))

def checkwin():
    global player
    winner = ""
    #check rows
    row_1 = list[0] == list[1] == list[2] != "-"
    row_2 = list[3] == list[4] == list[5] != "-"
    row_3 = list[6] == list[7] == list[8] != "-"
    #check diagonals
    row_4 = list[0] == list[4] == list[8] != "-"
    row_5 = list[2] == list[4] == list[6] != "-"
    #check columns
    row_6 = list[0] == list[3] == list[6] != "-"
    row_7 = list[1] == list[4] == list[7] != "-"
    row_8 = list[2] == list[5] == list[8] != "-"
    
    if player == "X":
        winner = "O"
    elif player == "O":
        winner = "X"
    
    if row_1 or row_2 or row_3 or row_4 or row_5 or row_6 or row_7 or row_8:
        print("player {} wins!!".format(winner))
        quit()
        
       
#this is the main    
if __name__ == "__main__":
    
    while bool:
        board()
        checkwin()
        current_player()
        print("What positions would you like filled in 0-8?")
        usernum = int(input("Position: "))
        filling(usernum)
        print()
        
        