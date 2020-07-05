from Poker_Card import *
import random

class Card_Deck:

    __VERBOSE = True

    card_deck = []
    deck_count = 1
    use_specials = None

    def __init__ ( self, NumberOfDecks = 1, UseSpecials = True ):

        if self.__VERBOSE: print( '\ninitializing card deck...' )
        self.use_specials = UseSpecials
        self.build_deck(NumberOfDecks)

    def build_deck ( self, decks = 1 ):
        if self.__VERBOSE: print( "build the deck...\n" )

        while decks > 0:
            cardSuits = Poker_Card.get_suits()
            cardRanks = Poker_Card.get_ranks()
            cardSpecials = Poker_Card.get_specials()
            for the_suit in cardSuits:
                for the_rank in cardRanks:
                    this_card = Poker_Card( the_rank, the_suit )
                    self.card_deck.append( this_card )

            if self.use_specials:
                for this_special in cardSpecials:
                    this_card = Poker_Card( the_rank, the_suit )
                    self.card_deck.append( this_special )

            decks -= 1

        return self.card_deck

#    def print_deck ( self ):
#        if self.__VERBOSE: print ( "print the deck...\n" )
#        for this_card in self.card_deck:
#            print ( this_card )
            
    def print_deck ( self ):
        if self.__VERBOSE: print ( "print the deck...\n" )
        for index, this_card in enumerate(self.card_deck):
            print ( f"{index}: {this_card}" )


    def cards_in_deck ( self ):
        if self.__VERBOSE: print ( f"number of cards in deck: {len ( self.card_deck )}" )
        return len ( self.card_deck )


    def splitDeck ( self ):
        num_in_stack = len ( self.card_deck )
        return num_in_stack


    def shuffle_deck ( self ):
        random.shuffle(self)
        

    def cutCards ( self ):
        if self.__VERBOSE: print( "cutting the deck...\n" )
        totalCards = len( self.card_deck )
        cutRange = totalCards // 5
        splitIndex = random.randint( cutRange, cutRange * 4 )
        topCut = self.card_deck [ :splitIndex ]
        bottomCut = self.card_deck [ splitIndex: ]
        return topCut, bottomCut


if __name__ == "__main__":
    my_deck = Card_Deck(NumberOfDecks = 1, UseSpecials = True)
    my_deck.cards_in_deck()
    my_deck.print_deck()

    print("\nshuffling deck...")
    my_deck.shuffle_deck
    my_deck.print_deck()
#    top, bottom = my_deck.cutCards()
#    print( f"\ntop cards: ({len(top)} cards)")
#    print(top)
#    print( f"\nbottom cards: ({len(bottom)} cards)" )
#    print( bottom )