from Card import Card

class Hand:
    '''
    플레이어나 딜러가 보유한 카드 관리, 점수 계산 기능 구현
    Game의 카드를 받음 => 
    '''
    def __init__(self, game ):
        self.dealer = []
        self. player = []
        self.game = game
        for _ in range(2):
            self.dealer.append(self.game.pop())
        for _ in range(2):
            self.player.append(self.game.pop())
            
    def score(self, who):
        cards = self.player if who == 'player' else self.dealer
        total = 0
        A = 0
        for card in cards:
            score = card.get_value()
            total += score
            if card.value == 'A':
                A += 1

        while total > 21 and A > 0:
            total -= 10
            A -= 1
        return total