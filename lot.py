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

class Slot:
    def __init__(self, id, car=None):
        self.id = id
        self.car = car
        self.empty = self.check()

    def check(self):
        return True if self.car == None else False

    def __repr__(self):
        if self.empty:
            return "None"
        else:
            return f"[{self.car.plate_no}, {self.car.color}]"
class Lot:
    def __init__(self, capacity):
        self.max_space = int(capacity)
        self.slots = {}
        self.build_lot()

    def build_lot(self):
        for slot_id in range(1, self.max_space + 1):
            empty_slot = Slot(slot_id, None)
            self.slots[slot_id] = empty_slot
        return

    def is_empty(self):
        # return a list of empty slots in ascending order
        empty = []
        for slot_id in self.slots.keys():
            if self.slots[slot_id].empty:
                empty.append(slot_id)
        return empty

    def assign_ticket(self, slot_id, car):
        if len(self.slots) > self.max_space:
            raise NotEmpty("Sorry, parking lot is full.")

        self.slots[slot_id] = Slot(slot_id, car)
        Ticket(car, slot_id)
        return

    def remove_ticket(self, car):
        self.slots[car.slot_no] = ""
        car.ticket = None
        return

def enter(lot, car):
    """Process the entry of a car"""
    if not lot.is_empty():
        raise NotEmpty("Sorry, parking lot is full.")

    free_lot = lot.is_empty()[0]
    lot.assign_ticket(free_lot, car)

def exit(lot, car):
    """Process the exit of a car."""
    lot.remove_ticket(car)

def find_plate_nos(lot, color):
    """Find the registration numbers of all cars of a particular color."""
    plate_nos = []
    for slot in lot.slots.values():
        if not slot.empty:
            if slot.car.color.lower() == color.lower():
                plate_nos.append(slot.car.plate_no)

    if plate_nos:
        return plate_nos
    else:
        return None

def find_slot_no(lot, plate_no):
    """Find the slot number in which a car with a given registration number is parked"""
    for slot in lot.slots.values():
        if not slot.empty:
            if slot.car.plate_no.lower() == plate_no.lower():
                return slot.id

    return None

def find_slot_nos(lot, color):
    """Find the slot numbers where cars of a particular color are parked."""
    slot_nos = []
    for slot in lot.slots.values():
        if not slot.empty:
            if slot.car.color.lower() == color.lower():
                slot_nos.append(slot.id)

    if slot_nos:
        return slot_nos
    else:
        return None

green_lot = Lot(6)
car = Car("axs0989", "black")

enter(green_lot, car)
enter(green_lot, Car("afs5689", "yellow"))
enter(green_lot, Car("sds5689", "yellow"))
enter(green_lot, Car("dfs5689", "green"))

print(find_slot_nos(green_lot, "yellow"))
exit(green_lot, car)