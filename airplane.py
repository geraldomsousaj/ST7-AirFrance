airplane = dict()

airplane['xmax'] = 28
airplane['ymax'] = 7
airplane['corridor_y'] = 4
airplane['max_transition_row'] = 13
airplane['exit'] = 12

airplane['seats'] = dict()

# considering there is only business class
real_seats = []
corridor_seats = []
transition_seats = []
business = [[1,1], [1,3]]

for x in range(1, airplane['xmax']+1):
    for y  in range(1, airplane['ymax']+1):
        if y != airplane['corridor_y']:
            real_seats.append([x, y])
        if y == airplane['corridor_y']:
            corridor_seats.append([x, y])
        if x <= airplane['max_transition_row'] and y != airplane['corridor_y']:
            transition_seats.append([x, y])

for x in range(2, 10):
    for y in range(1, 8, 2):
        business.append([x, y])

exit_seats = list()
for y in range(1, 8):
    if x!=4:
        exit_seats.append([12, y])

# economic class
econo_class = list()
for x in range(10, airplane['xmax']+1):
    for y in range(1, airplane['ymax']+1):
        if y!= airplane['corridor_y']:
            econo_class.append([x, y])


airplane['seats']['real'] = real_seats
airplane['seats']['corridor'] = corridor_seats
airplane['seats']['transition_possible_seats'] = transition_seats
airplane['seats']['business_class'] = business
airplane['seats']['exit_seats'] = exit_seats
airplane['seats']['econo_class'] = econo_class

del real_seats, corridor_seats, transition_seats, business, exit_seats, econo_class

print(airplane)