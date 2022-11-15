# Make a "reservation" class
# __init__ takes name, check_in, check_out, guests, rate, room_num
class Date:
    def __init__(self, date):
        self.date = date

    def __lt__(self, other):
        return self.date < other.date

class reservation:
    def __init__(self, name, check_in, check_out, guests, rate, room_num):
        self.name = name
        self.check_in = Date(int(check_in.replace('/', '')))
        self.check_out = Date(int(check_out.replace('/', '')))
        self.guests = int(guests)
        self.rate = float(rate)
        self.room_num = int(room_num)

    def is_checked_in(self):
        date = Date(2022_11_15)
        if self.check_in < date < self.check_out:
            return True
        else:
            return False

    def __repr__(self):
        return f"(Reservation)({self.name}, {self.check_in}, {self.check_out}, {self.guests}, {self.rate}, {self.room_num})"


def addGuest(header, data):
    if (len(header) != len(data)):
        assert IndexError("Len of header is not equal to len of data.")
    if(len(data) == 1):
        return
    name = data[0]
    check_in = data[1]
    check_out = data[2]
    guests = data[3]
    rate = data[4]
    room_num = data[5]
    guest = reservation(name, check_in, check_out, guests, rate, room_num)
    return guest


def readFile(fileName, deliminator):
    guests = []
    with open(fileName, 'r') as file:
        data = file.readlines()
        header = data[0].strip().split(deliminator)
        for guest in data[1:]:
            guest_split = guest.strip().split(deliminator)
            guest = addGuest(header, guest_split)
            if guest:
                guests.append(guest)
    return guests


def main():
    data = readFile("hotel.csv", ",")
    for guest in data:
        is_checked_in = guest.is_checked_in()
        if is_checked_in:
            print(f"{guest.name} is checked in!")


main()
