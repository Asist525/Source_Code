from Deck import Deck

class Game:
    '''
    전체 게임 흐름 제어
    '''
    
    def __init__(self):
        '''
        Deck에서 전체 카드 덱 리스트를 가져와서 self.deck에 저장
        '''
        self.deck = Deck()
        self.deck.shuffle()

    def pop(self):
        '''
        1. 전체 카드 덱에서 하나씩 pop => 리턴
        2. 리턴되는 값은 Hands에서 받음
        '''
        return self.deck.deal()