available_seats = [
  [None, "Pumpkin", None, None],
  ["Socks", None, "Mimi", None],
  ["Gismo", "Shadow", None, None],
  ["Smokey","Toast","Pacha","Mau"]
]

def check_seat(seats):
    for i in range(len(seats)):
        for j in range(4):
            if seats[i][j] == None:
                sit = input(f'Row {i+1} seat {j+1} is free. Do you want to sit here? [y/n] ')
                if sit == 'y':
                    name = input('What is your name? ')
                    seats[i][j] = name
                    return seats

print(check_seat(available_seats))