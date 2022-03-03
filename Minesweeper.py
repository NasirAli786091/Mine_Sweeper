import random
import os
os.system('cls')
class Minesweeper:
      
      def __init__(self,size,bombs):
            self.size = size        # dimensions of the board
            self.bombs = bombs # Number of bombs 
            self.board = [[0 for i in range(self.size)] for j in range(self.size)] # this is the actual board to store bombs and values
            self.apparent_board = [['O' for i in range(self.size)] for j in range(self.size)] # this is the board that the player can see which will be updated by real board
            self.dug = [] # string all the places which has been dugged


      # putting randomly n number of bombs in board
      def update_board_with_bombs(self):
            number_of_bombs = 0
            while number_of_bombs < self.bombs:
                  # generating random numbers(x,y) using random module 
                  index_x = random.randint(0,self.size-1)
                  index_y = random.randint(0,self.size-1)
                  # now updating the board[index_x][index_y] with a bomb 'B'
                  if self.board[index_x][index_y] != 0: #checking if that position already has a bomb
                        continue
                  else:
                        self.board[index_x][index_y] = 'B'
                        number_of_bombs += 1

      # after planting bombs randomly in board, assigning values adjacent to bombs to a number by recursively
      def assigning_values(self):
            for row in range(len(self.board)):
                  for col in range(len(self.board[row])):
                        if self.board[row][col] == 'B':
                              continue
                        else:
      # calling a method to look for a bomb adjacent to board[row][col] position and assign value to that board[row][col] position depending on the number of bombs around it
                              value = self.adjacent_bombs(row,col)
                              self.board[row][col] = value

      def adjacent_bombs(self,x,y):
            value = 0
            for i in range(x-1,x+2):
                  for j in range(y-1,y+2):
                        # checking boundaries and if its bombs
                        if i >= 0 and i < len(self.board) and j >= 0 and j < len(self.board[i]) and self.board[i][j] == 'B':
                              value += 1
            return value


# ALL THE ABOVE METHOD WERE TO CREATE AND UPDATE THE ACTUAL BOARD WHICH IS  ---->> self.board
# BELOW METHODS ARE TO UPDATE THE PLAYER BOARD OR (self.apparent_board) WITH THEIR INPUT USING THE ACTUAL BOARD VALUES


      # this method is to take player choice positions to play or dig the board until its bomb

      def dig(self,row,col):

            self.dug.append((row,col))

            if self.board[row][col] == 'B':
                  return False
            elif self.board[row][col] > 0:
                  return True

            # else if the position is not a bomb nor greater than 0, then its Zero, * so dig until neighbouring bomb is found
            for i in range(row-1,row+2):
                  for j in range(col-1,col+2):
                        #check if the position has been dug or not
                        if (i,j) in self.dug:
                              continue
      # again checking for boundries BUT note that self.board[i][j] should not be a Bomb cause that should be hidden to the player so DONT DIG !!!
                        if i >= 0 and i < len(self.board) and j >= 0 and j < len(self.board[i]) and self.board[i][j] != 'B':
                              self.dug.append((i,j))

            return True


      # simple method to display minesweeper board
      def display(self):

            for row in range(self.size):
                  for col in range(self.size):
                        if (row,col) in self.dug:
                              self.apparent_board[row][col] = str(self.board[row][col])
                        else:
                              self.apparent_board[row][col] = ' '

            for i in range(self.size):
                  print('      ',i,end = '')

            print()
            print('  ' ,'-----------------------------------------------------------------')

            for row in range(self.size):
                  for col in range(self.size):
                        if (row,col) in [(row_x,0) for row_x in range(self.size)]:
                              print(row,' |  ',self.apparent_board[row][col],end= ' ')
                        else:
                              print('  |  ',self.apparent_board[row][col],end = ' ')
                              if col == 7:
                                    print('  | ')
                                    print('  ' ,'-----------------------------------------------------------------')


def play(size = 8,bombs = 15):
      # lets create an object for the Minesweeper class 
      mine_sweeper = Minesweeper(size,bombs)
      mine_sweeper.update_board_with_bombs()
      mine_sweeper.assigning_values()

      safe = True
      #looping the game until player hits the bomb or player wins the game
      while len(mine_sweeper.dug) < mine_sweeper.size **2 - bombs:
            mine_sweeper.display()
            user_input = input('where would you like to dig ? Input as Row Column : ')
            if len(user_input) < 2:
                  os.system('cls')
                  print('please provide both row and columns')
                  continue
                  
            row, col = int(user_input[0]), int(user_input[-1])
            if row < 0 or row >= mine_sweeper.size or col < 0 or col >= mine_sweeper.size:
                  print('Invalid Location.','\ntry again')
                  continue
            # if the user input is valid then ----->>>
            os.system('cls')
            safe = mine_sweeper.dig(row,col)
            if not safe:
                  # hit the bomb if safe == True
                  break


      if safe:
            print('congratlation')
      else:
            print('oops !!! Game Over')
            mine_sweeper.dug = [(r,c) for r in range(mine_sweeper.size) for c in range(mine_sweeper.size)]
            mine_sweeper.display()

if __name__ == '__main__':
      play()
#m = Minesweeper(8,8)
#m.display()