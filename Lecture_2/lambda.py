people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Hermione", "house": "Gryffindor"},
]


people.sort(key=lambda person: person["name"])

print(people)
