#Three is a Crowd
people = ['Adam', 'Felix', 'David', 'Edward', 'Alex', 'Izzy']

def crowd_test():
    if len(people) == 0:
        print("The room is empty!")
    elif len(people) < 3:
        print("The room is not very crowded.")
    elif len(people) < 6:
        print("The room is crowded.")
    else:
        print("There is a mob in the room!")
crowd_test()
people.remove("Felix")
people.remove("Edward")
crowd_test()

