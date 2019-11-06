import random

черви = ['Aч', '2ч', '3ч', '4ч', '5ч', '6ч', '7ч', '8ч', '9ч', '10ч', 'Jч', 'Qч', 'Kч']
буби  = ['Aб', '2б', '3б', '4б', '5б', '6б', '7б', '8б', '9б', '10б', 'Jб', 'Qб', 'Kб']
трефы = ['Aт', '2т', '3т', '4т', '5т', '6т', '7т', '8т', '9т', '10т', 'Jт', 'Qт', 'Kт']
пики  = ['Aп', '2п', '3п', '4п', '5п', '6п', '7п', '8п', '9п', '10п', 'Jп', 'Qп', 'Kп']

class DectCards:
    def __init__(self, deck = []):
        self.deck = deck

    def mix(self):
        self.deck = random.shuffle(self.deck)
        return deck

deck = черви + буби + трефы + пики

mixdeck = DectCards(deck)
print(mixdeck.mix())
