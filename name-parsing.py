with open('first-names.txt') as f:
    first_names = f.readlines()

with open('oliver-twist.txt') as f:
    oliver_twist = f.read()

with open('occurrences.txt', 'a') as f:
    for name in first_names:
        if name in oliver_twist:
            f.write(name)