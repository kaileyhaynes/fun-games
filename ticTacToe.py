
def main():
    player1 = "O";
    player2 = "X";
    currentPlayer = 1;

    board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"];
    boardTaken = [];

    while(checkBoard(board) == "none" and len(boardTaken) != 9):
        printBoard(board);
        
        stringInput = "Player ", currentPlayer, "enter where you want to mark: ";
        num = int(input(stringInput));

        while num in boardTaken or num >=9 or num < 0:
            num = int(input("That's not a valid entry. Enter another: "));

        boardTaken.append(num);
        board = changeBoard(currentPlayer, num, board);
        checkBoard(board);
        
        if currentPlayer == 1:
            currentPlayer = 2;
        else:
            currentPlayer = 1;

    printBoard(board);
    
    #determine winner
    if(checkBoard(board) == "player 1"):
        print("Player 1 is the winner!");
    elif(checkBoard(board) == "player2"):
        print("Player 2 is the winner!");
    else:
        print("No one won!");

#~~~

def changeBoard(currentPlayer, num, board):
    if(currentPlayer == 1):
        board[num] = "O";
    else:
        board[num] = "X";
    return board;

#~~~

def printBoard(board):
    count = 0;
    for i in range(len(board)):
        print(board[i], end= " | ");
        count = count + 1;
        if(count % 3 == 0):
            print("\n");
            count = 0;

#~~~

def checkBoard(board):
    #across, O
    if(board[0] == "O" and board[1] == "O" and board[2] == "O"):
        return "player 1";
    elif(board[3] == "O" and board[4] == "O" and board[5] == "O"):
        return "player 1";
    elif(board[6] == "O" and board[7] == "O" and board[8] == "O"):
        return "player 1";

    #across, X
    if(board[0] == "X" and board[1] == "X" and board[2] == "X"):
        return "player 2";
    elif(board[3] == "X" and board[4] == "X" and board[5] == "X"):
        return "player 2";
    elif(board[6] == "X" and board[7] == "X" and board[8] == "X"):
        return "player 2";

    #vertical, O
    if(board[0] == "O" and board[3] == "O" and board[6] == "O"):
        return "player 1";
    elif(board[1] == "O" and board[4] == "O" and board[7] == "O"):
        return "player 1";
    elif(board[2] == "O" and board[5] == "O" and board[8] == "O"):
        return "player 1";

    #vertical, X
    if(board[0] == "X" and board[3] == "X" and board[6] == "X"):
        return "player 2";
    elif(board[1] == "X" and board[4] == "X" and board[7] == "X"):
        return "player 2";
    elif(board[2] == "X" and board[5] == "X" and board[8] == "X"):
        return "player 2";

    #diagonal, O
    if(board[0] == "O" and board[4] == "O" and board[8] == "O"):
        return "player 1";
    elif(board[2] == "O" and board[4] == "O" and board[6] == "O"):
        return "player 1";

    #diagonal, X
    if(board[0] == "X" and board[4] == "X" and board[8] == "X"):
        return "player 2";
    elif(board[2] == "X" and board[4] == "X" and board[6] == "X"):
        return "player 2";

    return "none";

#~~~

main();
