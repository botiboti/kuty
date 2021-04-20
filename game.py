import numpy as np


'''
A játékhoz tartozó class.
'''
class Board:
    
    def __init__(self, size, depth):
        self.size = size
        self.board = [['_' for c in range(size)] for r in range(size)]
        self.botpoz = (0,size//2)
        self.jatekospoz = (size-1, size//2)
        self.akadalyok = []
        self.depth = depth
        self.times = 0

    '''
    Helper függvények
    '''
    def update_jatekos(self, s):
        if s in self.neighboring_squares("jatekos"):
            self.jatekospoz = s
        else:
            raise Exception('Bad move. You can only move to neighboring squares. Give it another try.')

    def add_akadaly(self, sp):
        if sp in self.empty_squares():
            self.akadalyok.append(sp)
        else:
            raise Exception('Not a valid field to be excluded')

    def moveBot(self):
        move = self.find_best_move()
        self.botpoz = move[0]
        self.akadalyok.append(move[1])

    '''
    Vizuális reprezentáció a tábla aktuális állásáról            
    '''
    def print_board(self):
        self.board[self.botpoz[0]][self.botpoz[1]] = 'b'
        self.board[self.jatekospoz[0]][self.jatekospoz[1]] = 'p'
        for i in self.akadalyok:
            self.board[i[0]][i[1]] = 'x'
        for i in self.empty_squares():
            self.board[i[0]][i[1]] = '_'
        for i in self.board:
            for j in i:
                print(j, end = "  ")
            print()
        print("\n")

    '''
    Visszatéríti a kért játékoshoz tartozó szomszédos, aktív játékmezőket
    '''
    def neighboring_squares(self, player):
        result = []
        if player == "bot":
            for i in range(max(0,self.botpoz[0]-1), min(self.size, self.botpoz[0]+2)):
                for j in range(max(0, self.botpoz[1]-1), min(self.size, self.botpoz[1]+2)):
                    if (i,j) != self.botpoz and (i,j) != self.jatekospoz and not (i,j) in self.akadalyok:
                        result.append((i,j))
        else:
            for i in range(max(0,self.jatekospoz[0]-1), min(self.size, self.jatekospoz[0]+2)):
                for j in range(max(0, self.jatekospoz[1]-1), min(self.size, self.jatekospoz[1]+2)):
                    if (i,j) != self.jatekospoz and (i,j) != self.botpoz and not (i,j) in self.akadalyok:
                        result.append((i,j))
        return result

    '''    
    Visszatéríti az összes szabad helyet
    '''
    def empty_squares(self):
        result = []
        for i in range(self.size):
            for j in range(self.size):
                if (i,j) != self.botpoz and (i,j) != self.jatekospoz and not (i,j) in self.akadalyok:
                    result.append((i,j))
        return result

    '''
    Heurisztikus függvény
    '''
    def heuristic(self, a):
        return len(self.neighboring_squares("bot"))-a*len(self.neighboring_squares("jatekos"))

    '''
    Játék végét ellenörző függvény
    '''
    def game_status(self):
        if self.neighboring_squares("bot") == []:
            return -np.inf
        elif self.neighboring_squares("jatekos") == []:
            return np.inf
        else:
            return self.heuristic(2)

    '''
    Minimax algoritmusok
    '''
    def minimax(self, alpha, beta, depth, isBot):
        if depth == 0 or self.game_status() == np.inf or self.game_status() == -np.inf:
           return self.game_status()
        if (isBot):
            value = -np.inf
            oldpoz = self.botpoz
            for s in self.neighboring_squares("bot"):
                self.botpoz = s
                for sp in self.empty_squares():
                    self.akadalyok.append(sp)
                    value = max(value, self.minimax(alpha, beta, depth-1, False))
                    self.akadalyok.pop()
                    alpha = max(alpha, value)
                    if alpha >= beta:
                        break
            self.botpoz = oldpoz
            return value
        else:
            value = np.inf
            oldpoz = self.jatekospoz
            for s in self.neighboring_squares("jatekos"):
                self.jatekospoz = s
                for sp in self.empty_squares():
                    self.akadalyok.append(sp)
                    value = min(value,self.minimax(alpha, beta, depth-1, True))
                    self.akadalyok.pop()
                    beta = min(beta, value)
                    if beta <= alpha:
                        break
            self.jatekospoz = oldpoz
            return value

    '''
    Legjobb lépést megkereső algoritmus
    '''
    def find_best_move(self):
        bestVal = -np.inf
        oldpoz = self.botpoz
        for s in self.neighboring_squares("bot"):
            self.botpoz = s
            for sp in self.empty_squares():
                self.akadalyok.append(sp)
                moveVal = self.minimax(-np.inf, np.inf, self.depth+self.times, False)
                if (moveVal > bestVal):
                    bestMove = (s, sp)
                    bestVal = moveVal
                self.akadalyok.pop()
            self.botpoz = oldpoz
        self.times += 1
        return bestMove
