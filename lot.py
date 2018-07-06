# this module contains functions pertaining to the
# parking lot.

class NotEmpty(Exception):
    pass

class Car:
    def __init__(self, plate_no, color):
        self.plate_no = str(plate_no).upper()
        self.color = str(color).title()
        self.parked = False
        self.lot_no = None
        self.ticket = None

    def __repr__(self):
        return f"[{self.plate_no}, {self.color}]"

class Ticket:
    def __init__(self, car, lot_no):
        self.lot_no = None

class Lot:
    def __init__(self):
        self.max_space = 6
        self.spots = {}
        self.populate()

    def populate(self):
        for lot in range(1, self.max_space + 1):
            self.spots[lot] = ""
        return

    def is_empty(self):
        # return a list of empty lots in ascending order
        empty = []
        for lot_no in self.spots:
            if self.spots[lot_no] == "":
                empty.append(lot_no)
        return empty

    def assign_ticket(self, lot_no, car):
        # assign a ticket to a car for an open space
        if len(self.spots) > self.max_space:
            return # return some sort of error
        self.spots[lot_no]= car
        ticket = Ticket(car, lot_no)
        car.parked = True

def entry(plate_no, color):
    """Process the entry of a car"""
    # assign an open space if there is, and give out a ticket
    if not Lot.is_empty():
        raise NotEmpty("This Parking Lot is fully booked.")

    car = Car(plate_no, color)

    empty_lots = Lot.is_empty()
    free_lot = empty_lots[0]
    Lot.assign_ticket(free_lot, car)

def exit(car):
    """Process the exit of a car."""
    pass

Lot = Lot()