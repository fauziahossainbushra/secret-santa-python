import random

participants = ["Amy","Ben","Cara","Tom","Emma"]
assigned= []

for person in participants:
    chosen_person = random.choice(participants)

    while chosen_person == person or chosen_person in assigned:
        chosen_person = random.choice(participants)

    assigned.append(chosen_person)

    print(person, "->", chosen_person)

