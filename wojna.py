import random

   
class Karta:
    figura = ['AS','KROL','DAMA','JOPEK','10','9','8','7','6','5','4','3','2']
    kolor = ['kier', 'pik', 'karo', 'trefl']
    def __init__(self, figura, kolor):
        self.figura = figura
        self.kolor = kolor
        
    def __str__(self) -> str:
        x = self.figura + self.kolor
        return x

class Hand(object):
	""" reka - karty w reku gracza"""
	def __init__(self):
		self.cards = []

	def __str__(self):
		if self.cards:
			rep =""
			for card in  self.cards:
				rep += str(card) + " "
		else:
			rep = "<pusta>"
		return rep

	def clear(self):
		self.cards = []

	def add(self, card):
		self.cards.append(card)

	def give(self, card, other_hand):
		self.cards.remove(card)
		other_hand.add(card)


class Talia:
        
    def talia(self):
        for kolor in (Karta.kolor):
            for figura in Karta.figura:
                self.add(Karta(figura, kolor))
    
    def tasowanie(self):
        random.shuffle(self.talia)


talia1 = Talia()
talia1.talia()
karty = []
talia1.tasowanie()
