users = [
    {
        'id': 1,
        'name': 'Alice',
        'gender': 'female',
        'age': 25,
        'preferred_color': 'blue'
    },
    {
        'id': 2,
        'name': 'Bob',
        'gender': 'male',
        'age': 35,
        'preferred_color': 'GREEN'
    },
    {
        'id': 3,
        'name': 'Charlie',
        'gender': 'male',
        'age': 45,
        'preferred_color': 'Red'
    },
    {
        'id': 4,
        'name': 'Danielle',
        'gender': 'female',
        'age': 30,
        'preferred_color': 'YelloW'
    },
    {
        'id': 5,
        'name': 'Evelyn',
        'gender': 'female',
        'age': 20,
        'preferred_color': 'PuRplE'
    },
    {
        'id': 6,
        'name': 'Frank',
        'gender': 'male',
        'age': 28,
        'preferred_color': 'purple'
    },
    {
        'id': 7,
        'name': 'Grace',
        'gender': 'female',
        'age': 31,
        'preferred_color': 'GREEN'
    },
    {
        'id': 8,
        'name': 'Henry',
        'gender': 'male',
        'age': 40,
        'preferred_color': 'BLUE'
    },
    {
        'id': 9,
        'name': 'Isabelle',
        'gender': 'female',
        'age': 27,
        'preferred_color': 'red'
    },
    {
        'id': 10,
        'name': 'Jack',
        'gender': 'male',
        'age': 24,
        'preferred_color': 'yellow'
    }
]

def ex1():
    for user in users:
        print(user['name'])
ex1()

def exa2():
    female = 0
    male = 0
    for user in users:
        gender = user['gender']
        if gender == 'male':
            male += 1
        elif gender == 'female':
            female += 1
        else:
            continue
    print('there are '+str(female)+' females and '+str(male)+' males.')
    print(f'there are {female} females and {male} males.')
exa2()

def find_Element_By_Id(id):
    for user in users:
        if id == user['id']:
            print(user)
            break

find_Element_By_Id(2)
find_Element_By_Id(4)