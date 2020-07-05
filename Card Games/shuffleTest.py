import random

def cutCards ( cards ):
    totalCards = len( cards )
    cutRange = totalCards // 5
    splitIndex = random.randint( cutRange, cutRange * 4 )
    topCut = cards [ :splitIndex ]
    bottomCut = cards [ splitIndex: ]
    return topCut, bottomCut


def shuffleCards ( cards ):
    shuffledCards = [ ]
    totalCards = len( cards )
    topCards, bottomCards = cutCards( cards )

    numTopCards, numBottomCards = len( topCards ), len( bottomCards )
    while numTopCards > 0 or numBottomCards > 0:
        cardSelect = random.choice( [ "top", "bottom" ] )

        if cardSelect == "top" and numTopCards > 0:
            shuffledCards.append( topCards.pop( 0 ) )
            numTopCards -= 1
        elif cardSelect == "bottom" and numBottomCards > 0:
            shuffledCards.append( bottomCards.pop( 0 ) )
            numBottomCards -= 1

    return shuffledCards


cards = [ ]
for i in range( 52 ):
    cards.append( i + 1 )

print( cards )
shuffled_Cards = shuffleCards( cards )
shuffled_Cards = shuffleCards( shuffled_Cards )
shuffled_Cards = shuffleCards( shuffled_Cards )

print( shuffled_Cards )

# topCards, bottomCards = cutCards(cards)
# print (topCards)
# print (bottomCards)
