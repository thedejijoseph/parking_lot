# this module contains functions pertaining to the
# parking lot.

class NotEmpty(Exception):
    pass

class Car:
    def __init__(self, plate_no, color):
        self.plate_no = str(plate_no).upper()
        self.color = str(color).title()
        self.slot_no = None
        self.ticket = None

    def __repr__(self):
        return f"[{self.plate_no}, {self.color}]"

class Ticket:
    def __init__(self, car, slot_no):
        self.car = car
        self.slot_no = slot_no
        self.car.slot_no = slot_no
        self.car.ticket = self

    def __repr__(self):
        return f"Ticket for [{self.car.plate_no}, {self.car.color}]"

class Lot:
    def __init__(self, capacity):
        self.max_space = int(capacity)
        self.slots = {}
        self.build_lot()

    def build_lot(self):
        for lot in range(1, self.max_space + 1):
            self.slots[lot] = ""
        return

    def is_empty(self):
        # return a list of empty slots in ascending order
        empty = []
        for slot_no in self.slots.keys():
            if self.slots[slot_no] == "":
                empty.append(slot_no)
        return empty

    def assign_ticket(self, slot_no, car):
        if len(self.slots) > self.max_space:
            raise NotEmpty("This parking lot is fully occupied.")

        self.slots[slot_no] = car
        Ticket(car, slot_no)
        return

    def remove_ticket(self, car):
        self.slots[car.slot_no] = ""
        car.ticket = None
        return

def enter(lot, car):
    """Process the entry of a car"""
    if not lot.is_empty():
        raise NotEmpty("This parking lot is fully occupied.")

    free_lot = lot.is_empty()[0]
    lot.assign_ticket(free_lot, car)

def exit(lot, car):
    """Process the exit of a car."""
    lot.remove_ticket(car)

green_lot = Lot(6)
car = Car("axs0989", "matte black")

enter(green_lot, car)
exit(green_lot, car)