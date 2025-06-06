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