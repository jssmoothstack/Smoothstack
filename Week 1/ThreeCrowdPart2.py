#Three is a Crowd
people = ['Adam', 'Felix', 'David', 'Edward']

def crowd_test():
    if len(people) > 3:
        print("The room is crowded!")
    else:
        print("The room is not very crowded.")
crowd_test()
people.remove("Felix")
people.remove("Edward")
crowd_test()

