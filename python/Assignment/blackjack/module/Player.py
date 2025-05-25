from Game import Game
from Hand import Hand

class Player:
    '''
    플레이어 정보 및 게임 결정(히트 또는 스탠드) 관리
    '''
    def __init__(self, game):
        self.game = game
        self.hand = Hand(game)  # 플레이어 초기 카드 2장 받음

    def Hit(self):
        card = self.game.pop()
        self.hand.player.append(card)  # 추가된 카드 저장
        return self.hand.score('player')
    def Stand(self):
        print("턴 종료")
