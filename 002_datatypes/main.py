snacks = ["Roots", "Biscuits", "Chips", "Noodles", ["Ram", "Shyam"]]
print(snacks[4][1])

personal_details = {
    'name': "Ram",
    'address': ["Pokhara", "Kathmandu"]
}

print(personal_details['address'])

data = [{
    'name': "Ram Sharma",
    'hobbies': ['Coding', {
        'name': "Ayush",
        'address': [
    {
        'home': ["lekhnath", {
            'lake': "begnas"
        }]
    }
        ]
    }]
}]

print(data[0]['hobbies'][1]['address'][0]['home'][1]['lake'])
