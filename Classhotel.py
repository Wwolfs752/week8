# Make a "reservation" class
# __init__ takes name, check_in, check_out, guests, rate, room_num
class Room:
    def __init__(self, room_num, room_data):
        self.room_num = room_num

        for key, value in room_data.items():
            self.__setattr__(key, value)



# Make a "reservation" class
# __init__ takes name, check_in, check_out, guests, rate, room_num

class Date:
    def __init__(self, date):
        self.date = int(date.replace("/", ""))

    def __lt__(self, other):
        return self.date < other.date

    def __gt__(self, other):
        return self.date > other.date

    def __eq__(self, other):
        return self.date == other.date

    def __repr__(self):
        return f"{str(self.date)[0:4]}/{str(self.date)[4:6]}/{str(self.date)[6:]}"


class Reservation:
    def __init__(self, name, check_in, check_out, guests, rate, room_num):
        self.name = name
        self.check_in = Date(check_in)
        self.check_out = Date(check_out)
        self.guests = int(guests)
        self.rate = float(rate)
        self.room_num = int(room_num)

    def is_checked_in(self):
        today = Date("2022/11/17")
        if self.check_in < today < self.check_out:
            return True
        else:
            return False

    def __repr__(self):
        return f"""(Reservation)({self.name}, {self.check_in}, {self.check_out}, {self.guests}, {self.rate}, 
        {self.room_num})"""

    def __str__(self):
        return f"{self.name},{self.check_in},{self.check_out},{self.guests},{self.rate},{self.room_num}"


def addGuest(header, data):
    if len(header) != len(data):
        assert IndexError("Len of header is not equal to len of data.")

    if len(data) == 1:
        return
    name = data[0]
    check_in = data[1]
    check_out = data[2]
    guests = data[3]
    rate = data[4]
    room_num = data[5]
    guest = Reservation(name, check_in, check_out, guests, rate, room_num)
    return guest


def createGuest():
    name = input("What is the reservation name? ")
    check_in = input("What is the check in date. [yyyy/mm/dd]")
    check_out = input("What is the check out date. [yyyy/mm/dd]")
    guests = input("How many guests? ")
    rate = input("What is the rate? ")
    room_num = input("What is the room num?")
    guest = Reservation(name, check_in, check_out, guests, rate, room_num)
    return guest


def printMenu():
    print("[1] Add Guest")
    print("[2] Get checked in guests")
    print("[3] Delete Reservation")
    print("[4] Get Room Data")
    print("[q] Exit/Quit")


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


def checked_in_guests(data):
    print()
    for guest in data:
        if guest.is_checked_in():
            print(f"{guest.name} is checked in!")
    print()


def loadRooms(fileName):
    file_data = open(fileName).read()
    import json
    file_dict = json.loads(file_data)
    print(file_dict)

def main():
    data = readFile("hotel.csv", ",")
    rooms = loadRooms("rooms.json")
    while True:
        printMenu()
        selection = input("Please choose an option: ")
        if selection == "1":
            data.append(createGuest())
        elif selection == "2":
            checked_in_guests(data)
        elif selection == "3":
            assert NotImplementedError
        elif selection == "4":
            assert NotImplementedError
        elif selection == "q":
            with open("hotel.csv", "w") as file:
                file.write("Name,Start,End,Guests,Rate,Room\n")
                for guest in data:
                    file.write(f"{str(guest)}\n")
            exit()
        else:
            print("Invalid Option!")


main()