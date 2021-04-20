import game
import sys

'''
A játék menetét levezénylő algoritmus.
'''
def main():
    s1 = int(sys.argv[1]) # who starts 1-bot 0-player
    s2 = int(sys.argv[2]) # board size
    s3 = int(sys.argv[3]) # depth 
    jatek = game.Board(s2, s3)
    print("The board:")
    jatek.print_board()
    print("The positions are defined as follows:")
    for i in range(s2):
        for j in range(s2):
            print(str(i)+str(j), end = "  ")
        print()
    print("\n")
    print("You are p.")
    if s1==0:
        while(True):
            print("Your turn.")
            move = input("Enter move (format: y,x):")
            moves = move.split(',')
            movetuple = (int(moves[0]), int(moves[1]))
            jatek.update_jatekos(movetuple)
            jatek.print_board()
            akadaly = input("Exclude field (format: y,x):")
            aks = akadaly.split(',')
            akadalytup = (int(aks[0]), int(aks[1]))
            jatek.add_akadaly(akadalytup)
            jatek.print_board()

            jatek.moveBot()
            jatek.print_board()
    elif s1==1:
        while(True):
            print("Bots turn.")
            jatek.moveBot()
            jatek.print_board()
            print("Your turn.")            
            move = input("Enter move (format: y,x):")
            moves = move.split(',')
            movetuple = (int(moves[0]), int(moves[1]))
            jatek.update_jatekos(movetuple)
            jatek.print_board()
            akadaly = input("Exclude field (format: y,x):")
            aks = akadaly.split(',')
            akadalytup = (int(aks[0]), int(aks[1]))
            jatek.add_akadaly(akadalytup)
            jatek.print_board()
main()
