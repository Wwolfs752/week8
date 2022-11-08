import datetime


def add_row(header, data):
    output_dict = {}
    if len(header) != len(data):
        assert Exception
        return
    for index in range(len(header)):
        output_dict[header[index]] = data[index]
    return output_dict


def read_file(filename):
    guest_list = []
    with open(filename, 'r') as hotel_file:
        guest_data = hotel_file.readlines()
        head = guest_data[0].strip().split(',')
        for guest in guest_data[1:]:
            guest_split = guest.strip().split(',')
            row = add_row(head, guest_split)
            if row:
                guest_list.append(row)
    return guest_list


def print_checked_in(data):
    current_date = int(datetime.datetime.now().strftime("%m%d%y"))
    for guest in data:
        check_in = int(guest['Start'].replace('/', ''))
        check_out = int(guest['End'].replace('/', ''))
        if check_in <= current_date < check_out:
            print(guest['Name'])


def main():
    guest_data = read_file('hotel.csv')
    print_checked_in(guest_data)


main()
