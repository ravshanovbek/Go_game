#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Othello, or Reversi (https://en.wikipedia.org/wiki/Reversi), is a board game
played by two players, playing "disks" of different colors an 8x8 board.
Despite having relatively simple rules, Othello is a game of high strategic depth.
In this homework you will need to simulate a simplified version of othello,
called Dumbothello, in which each player can capture the opponent's disks
by playing a new disk on an adjacent empty cell.
The rules of Dumbothello are:
- each player has an associated color: white, black;
- the player with black is always the first to play;
- in turn, each player must place a disk of their color in such a way
  to capture one or more opponent's disks;
- capturing one or more opponent's disks means that the disk played by the
  player changes into the player's color all the directly adjacent opponent's disks,
  in any horizontal, vertical or diagonal direction;
- after playing one's own disk, the captured opponent's disks change
  their color, and become the same color as the player who just played;
- if the player who has the turn cannot add any disk on the board,
  the game ends. The player who has the higher number of disks on the board wins
  or a tie occurs if the number of disks of the two players is equal;
- the player who has the turn cannot add any disk if there is
  no way to capture any opponent's disks with any move, or if there are no
  more free cells on the board.

Write a function dumbothello(filename) that reads the configuration of the
board from the text file indicated by the string "filename" and,
following the rules of Dumbothello, recursively generates the complete game tree
of the possible evolutions of the game, such that each leaf of the tree
is a configuration from which no more moves can be made.

The initial configuration of the chessboard in the file is stored line by
line in the file: letter "B" identifies a black disk, a "W" a white disk,
and the character "." an empty cell. The letters are separated by one or
more spacing characters.

The dumbothello function will return a triple (a, b, c), where:
- a is the total number of evolutions ending in a black victory;
- b is the total number of evolutions ending in a white victory;
- c is the total number of evolutions ending in a tie.

For example, given as input a text file containing the board:
. . W W
. . B B
W W B B
W B B W

The function will return the triple:
(2, 16, 0)

NOTICE: the dumbotello function or some other function used by it must be recursive.
I will use only recursio


    def dimention_halver(self, full_list, coordinate):
        r, c = coordinate
        print(full_list)
        index = full_list.index(coordinate)
        A , B = [full_list[:index],full_list[index+1:]]
        
        if len(A) > 1 and len(B)>w1:
            return [A.reverse(),B]
        if len(A) > 1:
            return [A.reverse()]
        if len(B) > 1:
            return [B]
        return 
        
    
    def rook_path(self, ranges, coordinate):
        """for vertical and horizontal direction"""
        r,c = coordinate
        dimentions = []
        for row in (ranges[0]):
            for col in (ranges[1]):
                dimentions.append( (row, col) )
        
        return dimentions
'''

class Game:
    def __init__(self, board = [], next_move= 'B'):
        self.board = board
        self.children = []
        self.next_move = next_move
       
    
    def __str__(self):
        string = [' '.join(row) for row in self.board]
        return '\n'.join(string)
    def __repr__(self):
        string = [' '.join(row) for row in self.board]
        return '\n'.join(string)
    

    
    def turn_converter(self, string):
        if string == "W":
            return 'B'
        return "W"
    
    def empty_space(self):
        empty_list = [(r, c) for r, row in enumerate(self.board)
                 for c, col in enumerate(row)
                 if col == '.']
        new = []
        for r, c in empty_list:
            if self.empty_that_adjacent((r,c)):
                new.append((r,c))
        return new
    
    def empty_that_adjacent(self,coordinate):
        r,c = coordinate
        x =  [ (r-1,c-1),(r-1,c), (r-1,c+1),
                (r,c-1),            (r,c+1),
                (r+1,c-1), (r+1,c), (r+1,c+1) ]
        new_x = x.copy()
        for row in x:
            if row[0] < 0 or row[1] < 0:
                new_x.remove(row)
        
        for a_tuple in new_x:
            if self.board[a_tuple[0]][a_tuple[1]] != ".":
                return coordinate
        return None
        
        

            
    def queen_path_aux(self, direction,coordinate):
        """for diagonal direction"""
        r,c  = coordinate
        #diagonals = ((-1,-1),(1,1),(-1,1),(1,-1))
        list_diagonals = []
        for row, col in direction:
            temporary = []
            r,c  = coordinate
            while 0 <= r+ row < len(self.board) and \
                0 <= c+col < len( self.board[0] ):
                    r += row
                    c += col
                    temporary.append( (r,c) )
                    #if self.board[r][c] == '.':
                    #   break
            if len(temporary) > 1:
                list_diagonals.append(temporary)
                
        return list_diagonals
                    
                    
                
    
    def queen_path(self, coordinate):
        """vertical, horizontal and diagonals"""
        r, c = coordinate
        #path to take according to coordinate
        diagonal_direction = ((-1,-1),(1,1),(-1,1),(1,-1))
        vertical_direction = ((-1,0),(1,0))
        horizontal_direction = ((0,-1),(0,1))
        
        diagonal = self.queen_path_aux (diagonal_direction,coordinate)
        horizontal = self.queen_path_aux (horizontal_direction,coordinate)
        vertical = self.queen_path_aux (vertical_direction, coordinate)
        
        queen = []
        queen = [x for x in (horizontal , vertical, diagonal) if len(x)!=0]
        return queen
    
    def change_color_aux(self, by_letter, player):
        if player in by_letter:
            index = by_letter.index(player)
            if index > 0:
                another_player = self.turn_converter(player)
                if '.' in by_letter[:index]:
                    return 0
                if another_player in by_letter[:index]:
                    return 1
        return 0
        
    
    def change_color(self,X, player, coordinate):
        coloured = None
        new_board = [row.copy() for row in self.board]
        for dimention in X:
            for path in dimention:
                by_letter = str()
                for single_path in path:
                    by_letter += new_board[single_path[0]][single_path[1]]
                print('the ditections:',f'{by_letter: >5}')
                if self.change_color_aux(by_letter, player):
                    index = by_letter.index(player)
                    for single_path in path[:index]:
                        new_board[single_path[0]][single_path[1]] = player
                        new_board[coordinate[0]][coordinate[1]] = player
                    coloured = new_board
                    return new_board
                    print('path : ',single_path,f'  to {player}  -> ',f'{by_letter}')
                    print(self.__repr__())
                    print('+++++++++')
        
        return coloured
                
    
    
    def define_winner(self):
        dct = {'W':0,'B':0}
        for row in self.board:
            for el in row:
                if el == "W" or el == "B":
                    dct[el] += 1
        print('Winner!: ', (dct))
        if dct["B"] > dct["W"]:
            return (1,0,0)
        elif dct["W"] > dct["B"]:
            return (0,1,0)
        elif dct["W"] == dct["B"]:
            return (0,0,1)
        return None
    
    
    def game_stopper(self):
        
        if not self.empty_space():
            return self.define_winner()
        return None
      
    def allow_to_run(self, coordinate):
        return True
        
    
    def main(self):
        """ a - black, b - white, c- tie"""
        print(self.__repr__())
        print('+++++++++')
        if self.game_stopper():
            return self.game_stopper()
        player = self.next_move
        A = B = C = 0
        turns = 0
        for r,c in self.empty_space():
            print('point of (',r,c,')',f'turn of the {player: >10}')
            coloured = self.change_color(self.queen_path((r,c)), player, (r,c))
            if coloured:
                turns = 1
                new_board = [row.copy() for row in self.board]
                new_board = coloured
                print( self.__repr__() )
                print('+++++++++')
                child = Game ( new_board, self.turn_converter(player) )
                self.children.append( child )
                a, b, c = child.main()
                x,y,z = self.define_winner()
                A+= a+x
                B+= b+y
                C+= c+z
                
        if not turns:
            print('HHHHHHHHHHHHHH')
            player = self.turn_converter(player)
            for r,c in self.empty_space():
                print('point of (',r,c,')',f'turn of the {player: >10}')
                coloured = self.change_color(self.queen_path((r,c)), player, (r,c))
                if coloured:
                    turns = 1
                    new_board = [row.copy() for row in self.board]
                    new_board= coloured
                    print( self.__repr__() )
                    print('+++++++++')
                    child = Game ( new_board, self.turn_converter(player) )
                    self.children.append(child)
                    a, b, c = child.main()
                    x,y,z = self.define_winner()
                    A+= a+x
                    B+= b+y
                    C+= c+z
        
        if not turns:
            a, b, c = self.define_winner()
            A+= a
            B+= b
            C+= c
        return A,B,C
        
            
#b- 1    w- 1          

def returns_list(file):
    a = []
    if type(file) is str and file:
        a = file.split()
    if type(file) is not str:
        for line in file.readlines():
            a.append( returns_list(line))
    return a          

def dumbothello(filename : str) -> tuple[int,int,int] :
    board_list = returns_list(open(filename, 'r'))
    empty_spaces = sum([row.count('.') for row in board_list])
    #result = Game(board_list)
    return board_list
    

if __name__ == "__main__":
    R = dumbothello("boards/01.txt")

game = Game(dumbothello("boards/01.txt"))
