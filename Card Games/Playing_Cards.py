import random

class Card:
    suit = None
    rank = None
    CARD_SUITS = [ "Hearts", "Diamonds", "Clubs", "Spades" ]
    CARD_RANKS = { "Ace": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9,
                   "Ten": 10, "Jack": 11, "Queen": 12, "King": 13
                   }

    def __init__ ( self, rank, suit ):
        self.rank = rank
        self.suit = suit

    def __repr__ ( self ):
        return f"Card(\"{self.rank}\",\"{self.suit}\")"

    def __str__ ( self ):
        return f"This card is the {self.rank} of {self.suit}"

    @classmethod
    def cycle_suits ( cls ):
        print ( "cycle thru suits..." )
        for this_suit in cls.CARD_SUITS:
            print ( this_suit )

    @classmethod
    def cycle_ranks ( cls ):
        print ( "cycle thru ranks..." )
        for this_rank in cls.CARD_RANKS:
            print ( f"The {this_rank} is valued at {cls.CARD_RANKS [ this_rank ]}" )


class Deck:
    card_deck = [ ]

    def __init__ ( self ):
        pass

    def build_deck ( self, num_of_decks = 1 ):
        print ( "build the deck..." )

        while num_of_decks > 0:
            for the_suit in Card.CARD_SUITS:
                for the_rank in Card.CARD_RANKS:
                    this_card = Card ( the_rank, the_suit )
                    self.card_deck.append ( this_card )
            num_of_decks -= 1
        return self.card_deck

    def print_deck ( self ):
        print ()
        print ( "print the deck..." )

        for this_card in self.card_deck:
            print ( this_card )

    def cards_in_deck ( self ):
        print ( "Number of cards in deck:" )
        return len ( self.card_deck )

    def splitDeck ( self ):
        num_in_stack = len(self.card_deck)
        return num_in_stack

    def shuffle_deck( self ):
        shuffled_deck = random.shuffle(self)
        return shuffled_deck


x = Card ( "Ten", "Hearts" )
y = Card ( "Ace", "Spades" )
z = Card ( "Five", "Diamonds" )

print ()

poker = Deck ()

print ()
poker.build_deck ( 1 )

poker.print_deck ()
print ()
print ( poker.cards_in_deck () )

shuffled = poker

print ()
print ( "shuffling..." )
#shuffled = random.shuffle(poker)

random.shuffle(shuffled)
shuffled.print_deck()
# print ( poker.splitDeck ( ) )
# print ()
# print ( x )
# print ( y )
# print ( z )
# print ()
# Card.cycle_suits ()
# print ()
# Card.cycle_ranks ()
