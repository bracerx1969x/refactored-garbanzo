from Card import *


class Poker_Card ( Card ):
    _suit = None
    _rank = None
    CARD_SUITS = [ "Hearts", "Diamonds", "Clubs", "Spades" ]
    CARD_RANKS = { "Ace": 14, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9,
                   "Ten": 10, "Jack": 11, "Queen": 12, "King": 13
                   }

    CARD_SPECIALS = { "Little Joker": 15, "Big Joker": 16 }

    def __init__ ( self, rank, suit ):
        super().__init__(rank, suit)

    def __repr__ ( self ):
        return f"Card(\"{self._rank}\",\"{self._suit}\")"

    def __str__ ( self ):
        return f"The {self._rank} of {self._suit}"

    def __eq__ ( self, other ):
        if self._rank == other._rank and self._suit == other._suit:  return True

    def __ne__ ( self, other ):
        return not self.__eq__( other )

    def __gt__ ( self, other ):
        return self._rank > other._rank

    def __ge__ ( self, other ):
        return self._rank >= other._rank

    def __lt__ ( self, other ):
        return self._rank < other._rank

    def __le__ ( self, other ):
        return self._rank <= other._rank

    @classmethod
    def show_suits ( cls ):
        print( "\nPoker Cards have these suits..." )
        for this_suit in cls.CARD_SUITS:
            print( this_suit )

    @classmethod
    def show_ranks ( cls ):
        print( "\nPoker Cards have these ranks..." )
        for this_rank in cls.CARD_RANKS:
            print( f"The {this_rank} is valued at {cls.CARD_RANKS [ this_rank ]}" )

        print( "\nThey also have these special cards..." )
        for this_special in cls.CARD_SPECIALS:
            print( f"The {this_special}" )

    @classmethod
    def get_suits ( cls ):
        return Poker_Card.CARD_SUITS

    @classmethod
    def get_ranks ( cls ):
        return Poker_Card.CARD_RANKS

    @classmethod
    def get_specials ( cls ):
        return Poker_Card.CARD_SPECIALS

if __name__ == "__main__":
    x = Poker_Card ( "Seven", "Diamonds" )
    y = Poker_Card ( "Six", "Clubs" )
    z = Poker_Card ( "Five", "Spades" )
    v = Poker_Card ( "Seven", "Diamonds" )

    if x.__le__( y ): print( "x is less than y" )
    if x.__ne__( z ): print( "x is not equal to z" )
    if x.__eq__( z ): print( "x is equal to z" )

    Poker_Card.show_suits()
    Poker_Card.show_ranks()
    print("\nCard Suits...")
    print(Poker_Card.get_suits())
