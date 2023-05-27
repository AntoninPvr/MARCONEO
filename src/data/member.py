"""
member.py

Defines the Member class
and everything related to the member
of the BDE of Télécom Physique Strasbourg.
"""

#-------------------------------------------------------------------#

class Member:
    """
    A member of the BDE of Télécom Physique Strasbourg.
    Has a first name, a last name, a nickname, a card ID,
    a balance and a status (admin and contributor of BDE).
    """
    def __init__(self, app, member_data:dict=None) -> None:
        self.loggers = app.loggers
        self.member_data = member_data

        if member_data is None:
            self.first_name = None
            self.last_name = None
            self.nickname = None
            self.card_id = None
            self.balance = None
            self.is_admin = None
            self.is_contributor = None
            return

        self.first_name = member_data['first_name']
        self.last_name = member_data['last_name']
        self.nickname = member_data['nickname']
        self.card_id = member_data['card_id']
        self.balance = member_data['balance']
        self.is_admin = member_data['is_admin']
        self.is_contributor = member_data['is_contributor']

        print(f"Current user: {self.first_name} {self.last_name} ({self.balance}€)")
        self.loggers.log.info(f"Current user: {self.first_name} {self.last_name}")

    def __str__(self) -> str:
        if self.member_data is None:
            return "No user is logged in."
        return f"{self.first_name} {self.last_name} ({self.nickname})"

    def __repr__(self) -> str:
        return self.__str__()
