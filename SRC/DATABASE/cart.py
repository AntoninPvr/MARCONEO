"""
cart.py

Describes the Cart class, which is used to
store the items caracteristics bought by a member.
"""

#-------------------------------------------------------------------#


class Cart:
    """
    Cart of the member of the BDE logged on the current session.
    """
    def __init__(self, loggers, member):
        self.loggers = loggers
        self.member = member
        self.items = []
        self.total = 0

    def add_to_cart(self, item):
        """
        Adds an item to the cart.
        """
        self.items.append(item)

    def reset(self):
        """
        Resets the cart.
        """
        self.items = []
        self.total = 0

    def __str__(self):
        if self.member is None:
            return "No user is logged in."
        return f"Cart of {self.member.nickname}: {self.items.__str__()}"

    def __repr__(self):
        return self.__str__()
