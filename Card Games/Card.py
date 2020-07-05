class Card:
    """ This is the basic card class that will be
    extended to use for more specific card types.
    """
    __suit = None
    __rank = None

    def __init__ ( self, rank, suit ):
        self._rank = rank
        self._suit = suit

    def __repr__ ( self ):
        return f"Card(\"{self._rank}\",\"{self._suit}\")"

    def __str__ ( self ):
        return f"This card is the {self._rank} of {self._suit}"

    def __eq__ ( self, other ):
        if self._rank == other._rank and self._suit == other._suit:
            return True
        else:
            return False

    def __ne__ ( self, other ):
        return not self.__eq__( other )

    def __gt__( self, other ):
        pass

    def __ge__( self, other ):
        pass

    def __lt__( self, other ):
        pass

    def __le__( self, other ):
        pass


