import random

class Card:
    def __init__(self, suit, value):
        
        self.suit = suit
        self.value = value
    def __str__(self):
        return f'{self.suit} {self.value}'
    
    def get_value(self):
        if self.value in ['J', 'Q', 'K']:
            return 10
        elif self.value == 'A':
            return 11
        else:
            return int(self.value)
        
        
        
class Deck:
    def __init__(self):
        self.cards = [] 
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit,value))
    
    def shuffle(self):
        random.shuffle(self.cards)
        
    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

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

    

def main():
    cib = 100
    print("블랙잭 게임에 오신 것을 환영합니다!")
    name = input("이름을 입력해주세요: ")

    while True:
        if cib <= 0:
            print("칩이 모두 소진되었습니다. 게임 종료!")
            break

        print("\n────────── 새 게임 ──────────")
        print(f"보유 칩: {cib}")
        try:
            betting = int(input("배팅할 금액을 입력해 주세요: "))
        except ValueError:
            print("숫자로 입력해 주세요.")
            continue

        if betting > cib or betting <= 0:
            print("잘못된 금액입니다. 다시 입력해주세요.")
            continue

        cib -= betting

        game = Game()
        player = Player(game)
        dealer = Dealer(game, player.hand)

        # 출력: 딜러 카드 한 장만 공개
        visible_card = player.hand.dealer[0]
        dealer_str = f"{visible_card}, hidden"
        player_str = ', '.join(str(card) for card in player.hand.player)

        print(f"\n{name}의 카드: [{player_str}]")
        print(f"{name}의 초기 점수:", player.hand.score('player'))
        print(f"\n딜러의 카드: [{dealer_str}]")
        print("딜러 초기 점수:", visible_card.get_value())

        # 블랙잭 판정
        if player.hand.score('player') == 21:
            print("블랙잭! 이겼습니다!")
            cib += int(betting * 2.5)
        else:
            # 플레이어 턴
            while True:
                move = input("입력 (hit / stand): ").strip().lower()
                if move == 'hit':
                    score = player.Hit()
                    player_str = ', '.join(str(c) for c in player.hand.player)
                    print(f"{name}의 카드: {player_str}")
                    print("현재 점수:", score)
                    if score > 21:
                        print("버스트! 당신은 졌습니다.")
                        break
                elif move == 'stand':
                    print("턴 종료")
                    break
                else:
                    print("잘못된 입력입니다. hit 또는 stand를 입력하세요.")

            # 딜러 턴
            dealer.play()

            # 승패 판정
            player_score = player.hand.score('player')
            dealer_score = player.hand.score('dealer')

            print("\n[결과]")
            if player_score > 21:   
                print("버스트! 패배")
        
            elif dealer_score > 21 or player_score > dealer_score:
                print("이겼습니다!")
                cib += betting * 2
            
            elif player_score < dealer_score:
                print("딜러 승리!")
                # 칩 차감은 이미 됐음
            else:
                print("무승부!")
                cib += betting  # 환불

        cont = input("\n계속 하시겠습니까? (1: 계속 / 기타: 종료): ").strip()
        if cont != "1":
            print(f"게임 종료! 최종 칩: {cib}")
            break

if __name__ == "__main__":
    main()