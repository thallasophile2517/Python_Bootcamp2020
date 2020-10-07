import random

def display(board):
  print(f'''
  {board[7]}|{board[8]}|{board[9]}                                      7 | 8 | 9
  ---+---+---                                     ---+---+---
  {board[4]}|{board[5]}|{board[6]}                      Positions->     4 | 5 | 6
  ---+---+---                                     ---+---+---
  {board[1]}|{board[2]}|{board[3]}                                      1 | 2 | 3
  ''')

def valid_input():
  while True:
    pos=input("enter position: ")
    if pos !=' ':
      if int(pos) in range(1,10):
          pos=int(pos)
          break
      print('not valid Poistion')
    else:
      print("thankyou for playing TIC_TAC_TOE")
      exit()
  return int(pos)

def valid_pos(turn, board):
  print(f'{turn} chance')
  pos=valid_input()
  while True:
    if board[pos]=='   ':
      board[pos]=turn
      break
    else:
      print('cannot overwrite, plz select new location')
      pos=valid_input()

def check(board):
  check=0
  #row
  if board[1]==board[2]==board[3]!='   ' or  board[4]==board[5]==board[6]!='   ' or board[7]==board[8]==board[9]!='   ':
    check=1
  #col
  elif board[1]==board[4]==board[7]!='   ' or  board[2]==board[5]==board[8]!='   ' or board[3]==board[6]==board[9]!='   ':
    check=1
  #dig
  elif board[1]==board[5]==board[9]!='   ' or  board[3]==board[5]==board[7]!='   ' :
    check=1
  
  return check


def userInput(board,symbol):
  sym1,sym2=symbol[random.randint(0,1)]
  print(f'{sym1} is going first\n\n')
  display(board)
  for i in range(9):
    if i%2==0:
      turn=' '+sym1+' '
      valid_pos(turn,board)
    else:
      turn=' '+sym2+' '
      valid_pos(turn,board)
    display(board)
    if i>=4:
      if check(board):
        display(board)
        print(f"'{turn}' WON!")
        break;
    if i==8:
      print("none WON, Its TIE")

  



def game():
  board=["just to adjust loc",'   ','   ','   ','   ','   ','   ','   ','   ','   ']
  symbol=[('X','O'),('O','X')]
  while True:
    marker= input("\nEnter your Marker: ").upper()
    if marker ==' ':
      print("Thanks for playing! Have a good day")
      exit()
    if marker=='X' or marker=='O':
      userInput(board,symbol)
      break
    else:
      print('Wrong Marker. Please enter either X or O')
  #display(board)

def main():
  again='Y'
  while again=='Y':
    print("press [space] to stop playing")
    game()
    again= input("press 'Y/y' to play Again").upper()
  print("Thanks for playing! Have a good day")

main()