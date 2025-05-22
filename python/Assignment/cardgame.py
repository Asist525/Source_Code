from random import shuffle


class Cards:
    def __init__(self):
        self.status = ['Hearts', 'Diamonds', 'clubs', 'spades']
        self.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    


class Deck: # randow함수를 통해 카드 섞는 클래스
    def __init__(self):
        deck = Cards()
        self.status = deck.status
        self.values = deck.values
        self.mycardest = []
        for i in range(len(self.status)):
            for j in range(len(self.values)):
                self.mycardest.append(f'{self.values[j]} of {self.status[i]}')
        
    def shuffleDeck(self):
        shuffle(self.mycardest)
        return self
    def popCard(self):
        pass
    
class Player:
    def __init__(self, nickname):
        self.nickname = nickname
        deck = Deck()
        shuffled_deck = deck.shuffleDeck()
        self.deck = shuffled_deck.mycardest
    def __str__(self):
        return f"player {self.nickname} has {self.deck[:5]}"
    def add_card(self, card):
        pass
        
if __name__ == "__main__":
    deck = Deck()
    print(f"[Current Deck]\n{deck.mycardest}")
    print()
    shuffled_deck = deck.shuffleDeck()
    print(f"[Shuffled Deck]\n{shuffled_deck.mycardest}")
    print()
    
    player1 = Player('Gil Dong')
    player2 = Player('Chul Su')
    
    for _ in range(4):
        player1.add_card(shuffled_deck.popCard())
        player2.add_card(shuffled_deck.popCard())
    
    print(player1)
    print(player2)
    
    