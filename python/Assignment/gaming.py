def game(player1, player2):
    game_list = ['rock', 'scissor', 'paper', 'rock']
    player1 = player1.lower()
    player2 = player2.lower()

    x = game_list.index(player1)
    y = game_list.index(player2)
    if game_list[y] == game_list[x+1]:
        return 'player1'
    elif game_list[y] == game_list[x-1]:
        return 'player2'
    else:
        return 'Draw'

        
    


def main():
    while True:
        flag = True
        print('='*10+ 'START' + '='*10)
        try:
            p1=input('Player1 [Rock, Paper, Scissor, exit]')
            p2=input('Player2 [Rock, Paper, Scissor, exit]')
            if p1.lower()=='exit' or p2.lower()=='exit':
                winner='exit'
                break
            winner = game(p1,p2)
        except ValueError:
            print('Input the wrong value')
            flag = False
        
        finally:
            if flag:
                if winner=='Draw': print('We have no winner')
                elif winner=='exit': print('Goodbye!')
                else: 
                    print(f"Winner is {winner}")
            else:
                print('Ooops, You have me the wrong input!')
        print('='*26)

if __name__ == "__main__":
    main()