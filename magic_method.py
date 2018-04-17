# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 19:52:08 2018

@author: Administrator
"""

import collections

Card = collections.namedtuple('Card',['rank','suit'])

class FrechDeck(object):
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()    
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
    def __repr__(self):
        return '{0}'.format([x for x in self._cards])

if __name__ == "__main__":
    beer_card = Card('7', 'diamonds')
    deck = FrechDeck()
    
    print deck[0]
    
    for i in deck:
        print(i)