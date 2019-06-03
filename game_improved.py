import random

# 1. Prints out a board
def display_board(board):

  print('\n'*100)
  print(" -------------")
  print(" |", board[7], "|", board[8], "|",board[9],"|")
  print(" -------------")
  print(" |", board[4], "|", board[5], "|",board[6],"|")
  print(" -------------")
  print(" |", board[1], "|", board[2], "|",board[3],"|")
  print(" -------------")

# 2. Takes in the players input and assigns their marker as 'X' or 'O'
def players_symbols():

  marker = ""
  
  while not(marker == "X" or marker == "O"):

    marker = (input("\nType X or O to choose a marker for the first player: ")).upper()
    if marker == "X":
      print("\nGreat! Player 1 will be X and Player 2 will be O!")
      return("X","O")   

    elif marker == "O":
      print("\nGreat! Player 1 will be O and Player 2 will be X")
      return("O", "X")

    else:
      print("Invalid choise! Plese choose one of the symbols X or O for a marker!")


# 3. Takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board
def place_marker(board, marker, position):
  if position >= 1 and position <= 9:
    board[position] = marker
  else:
    "Wrong choise, please choose a number between 1 and 9!"
  
  return(board)

#  4. Takes in a board and a mark (X or O) and then checks to see if that mark has won
def win_check(board, mark):

  if board[1:4] == [mark]*3 or \
    board[4:7] == [mark]*3 or \
    board[7:10] == [mark]*3 or \
    board[1] == board[4] == board[7] == mark or \
    board[2] == board[5] == board[8] == mark or \
    board[3] == board[6] == board[9] == mark or \
    board[1] == board[5] == board[9] == mark or \
    board[3] == board[5] == board[7] == mark:

    return True
  else:
    return False

# 5. Uses random to decide which player goes first
def choose_first():
  
  if random.randint(0,1) == 0:
    print("\nThe game will randomly choose which player goes first. \n\n")
    return 0
  else:
    print("\nThe game will randomly choose which player goes first. \n\n")
    return 1

# 6. Returns a boolean indicating whether a space on the board is freely available
def space_check(board, position):
  if board[position] == " ":
    return True
  else:
    return False

# 7. Checks if the board is full and returns a boolean: True if full, False otherwise
def full_board_check(board):
  
  checker = []

  for space in board:
    if space == " ":
      checker.append("NF")
    else:
      checker.append("F")
  
  if "NF" in checker:
    return False
  else:
    return True
  
# 8. Asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.

def player_choice(board):

  correct_choise = True

  while correct_choise:
    
    next_choise = int(input("Choose a number between 1 and 9: "))

    if space_check(board, next_choise):
      return next_choise
    else: 
      print("Position taken! Please choose a free position!")


# 9. Asks the player if they want to play again and returns a boolean True if they do want to play again.
def replay():
  play_again = (input("Do you want to play again? (y/n):")).lower()

  while play_again != "y" or play_again != "n":
      
    if play_again == "y":
      print("Resetting the game!\n")
      return True
    elif play_again == "n":
      return False

    print("Invalid answer! Please answer with y or n!")
    play_again = (input("Do you want to play again? (y/n):")).lower()

# 10. Running the game

game_on = True

#print(full_board_check(board),win_check(board, p1_sym), win_check(board, p2_sym) )
while game_on:

  board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

# Play while the bord is full or somebody wins

  print('\n'*100)
  print("Welcome to my Tic Tac Toe game! \nLet's choose the player's markers! \n")
  p1_sym, p2_sym = players_symbols()
  active_player = choose_first()

  while not(full_board_check(board) or win_check(board, p1_sym) or win_check(board, p2_sym)):

    if active_player == 0:
      print("Player 1's turn - playing with {}: ".format(p1_sym))
      choise = player_choice(board)
      place_marker(board, p1_sym, choise)
      display_board(board)
      active_player = 1
        
    else:
      print("Player 2's turn - playing with {}: ".format(p2_sym))
      choise = player_choice(board)
      place_marker(board, p2_sym, choise)
      display_board(board)
      active_player = 0

  if full_board_check(board):
    print("\nThe board is full! Nobody wins!\n")
  elif win_check(board, p1_sym):
    print("\nCongratulations Player 1 ({})! You won the game!\n".format(p1_sym))
  else:
    print("\nCongratulations Player 2 ({})! You won the game!\n".format(p2_sym))

  if not(replay()):
    print("\n\nThank you for playing! Goodbye!\n")
    game_on = False
