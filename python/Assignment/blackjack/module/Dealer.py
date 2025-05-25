from Hand import Hand
from Game import Game

class Dealer:
    '''
    딜러 행동 규칙 구현 (17 이상이면 스탠드)
    '''
    def __init__(self, game, hand):
        self.game = game
        self.hand = hand

    def play(self):
        while self.hand.score('dealer') < 17:
            card = self.game.pop()
            self.hand.dealer.append(card)
            print(f"딜러가 카드를 뽑았습니다: {card}")
            print("딜러 현재 점수:", self.hand.score('dealer'))

        print("\n딜러는 스탠드합니다.")
        print("딜러 최종 카드:", ', '.join(str(c) for c in self.hand.dealer))
        print("딜러 최종 점수:", self.hand.score('dealer'))