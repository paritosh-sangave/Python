# dictionary
# - collection of key-value pairs
# - key must be of type string(single or double quotes)
# - value can be of any type

def func1():
    name = "person1"
    age = 40
    email = "person1@abc.co"
    address = "pune"
    print(f"name = {name}, age = {age}, address = {address}, email = {email}")

    name2 = "person2"
    age2 = 45
    email2 = "person2@abc.co"
    address2 = "mumbai"
    print(f"name = {name2}, age = {age2}, address = {address2}, email = {email2}")

# func1()
# name = person1, age = 40, address = pune, email = person1@abc.co
# name = person2, age = 45, address = mumbai, email = person2@abc.co

def func2():

    def print_details(person):
        print(f"name : {person['name']}")
        print(f"age : {person['age']}")
        print(f"email : {person['email']}")
        print(f"address : {person['address']}")

    def print_dictionary_details(person):
        print(person)
        print(type(person))
        print(person.keys())
        print(person.values())

    # collection of key-value pairs
    # keys: name, age, email, address
    # values: person1, 40, person1@abc.co, pune
    person1 = {
        "name": "person1",
        "age": 40,
        "email":"person1@abc.co",
        "address":"pune"
    }

    person2 = {
        "name": "person2",
        "age": 45,
        "email":"person2@abc.co",
        "address":"mumbai"
    }

    print_details(person1)
    print_dictionary_details(person1)
    print('\n')
    print_details(person2)
    print_dictionary_details(person2)

# func2()
# name : person1
# age : 40
# email : person1@abc.co
# address : pune
# {'name': 'person1', 'age': 40, 'email': 'person1@abc.co', 'address': 'pune'}
# <class 'dict'>
# dict_keys(['name', 'age', 'email', 'address'])
# dict_values(['person1', 40, 'person1@abc.co', 'pune'])


# name : person2
# age : 45
# email : person2@abc.co
# address : mumbai
# {'name': 'person2', 'age': 45, 'email': 'person2@abc.co', 'address': 'mumbai'}
# <class 'dict'>
# dict_keys(['name', 'age', 'email', 'address'])
# dict_values(['person2', 45, 'person2@abc.co', 'mumbai'])


def func3():
    mobile = {
        "model": "iPhone 13 pro max",
        "company": "Apple",
        "price": 150000,
        "can_afford": False,
        "configuration": {
            "storage": "1 TB",
            "RAM": "8 GB"
        },
        "features": [
            "very high quality display",
            "little heavy"
        ]
    }

    print(f"model: {mobile['model']}")
    print(f"company: {mobile['company']}")
    print(f"price: {mobile['price']}")    
    print(f"can_afford: {mobile['can_afford']}")
    print(f"----Configuration----")
    print(f"storage: {mobile['configuration']['storage']}")
    print(f"RAM: {mobile['configuration']['RAM']}")
    print(f"----features----")
    for feature in mobile['features']:
        print(feature)

# func3()
# model: iPhone 13 pro max
# company: Apple
# price: 150000
# can_afford: False
# ----Configuration----
# storage: 1 TB
# RAM: 8 GB
# ----features----
# very high quality display
# little heavy


def func4():
    person = {
        "name": "person1",
        "email": "person1@test.com",
        "age": 40,
        "favorite_languages": [
            "python", "C", "C++", "html", "javascript"
        ],
        "addresses": [
            {"title": "home", "city": "pune", "state": "mh", "country": "india"},
            {"title": "office", "city": "mumbai", "state": "mh", "country": "india"}
        ]
    }

    print(f"name = {person['name']}")
    print(f"email = {person['email']}")
    print(f"age = {person['age']}")

    print(f"--- favorite languages ---")
    for language in person['favorite_languages']:
        print(language)

    print(f"--- address ---")
    for address in person['addresses']:
        print(f"title = {address['title']}")
        print(f"city = {address['city']}")
        print(f"state = {address['state']}")
        print(f"country = {address['country']}")
        print()


# func4()
# name = person1
# email = person1@test.com
# age = 40
# --- favorite languages ---
# python
# C
# C++
# html
# javascript
# --- address ---
# title = home
# city = pune
# state = mh
# country = india

# title = office
# city = mumbai
# state = mh
# country = india


def func5():
    person = {
        "name": "person1",
        "address": "pune",
        "age": 40,
        "email": "person1@abc.co"
    }

    print(f"name = {person['name']}")
    print(f"address = {person['address']}")
    print(f"age = {person['age']}")
    print(f"email = {person['email']}")

    for key in person.keys():
        print(f"key = {key}, value = {person[key]}")

# func5()
# name = person1
# address = pune
# age = 40
# email = person1@abc.co
# key = name, value = person1
# key = address, value = pune
# key = age, value = 40
# key = email, value = person1@abc.coname = person1
# address = pune
# age = 40
# email = person1@abc.co
# key = name, value = person1
# key = address, value = pune
# key = age, value = 40
# key = email, value = person1@abc.co

def func6():
    # list of dictionaries
    persons = [
        {"name": "person1", "age":10},
        {"name": "person2", "age":20},
        {"name": "person3", "age":30},
        {"name": "person4", "age":40},
        {"name": "person5", "age":50}
    ]

    for person in persons:
        for key in person.keys():
            print(f"{key} = {person[key]}")
    
# func6()
# name = person1
# age = 10
# name = person2
# age = 20
# name = person3
# age = 30
# name = person4
# age = 40
# name = person5
# age = 50


def func7():
    car = {
        "model": "i20",
        "company": "hyundai",
        "price": 15
    }
    print(f"model = {car.get('model')}")
    print(f"company = {car.get('company')}")
    print(f"price = {car.get('price')}")
    print(f"fuel_type = {car.get('fuel_type')}")

# func7()
# model = i20
# company = hyundai
# price = 15
# fuel_type = None


def func8():
    # empty dictionary
    car = {}

    model = input("enter model: ")
    price = int(input("enter price: "))
    company = input("enter company: ")

    # add the values entered by user into the dictionary
    car['model'] = model
    car['company'] = company
    car['price'] = price

    print(car)

# func8()
# enter model: F175
# enter price: 15000000
# enter company: Ferrari
# {'model': 'F175', 'company': 'Ferrari', 'price': 15000000}


def func9():
    # get 5 user details (name, age, address) from user
    # and store them in list of dictionaries

    # declare empty list
    persons = []

    # run a loop 5 times
    for count in range(5):
        # get details of user
        name = input("enter name: ")
        address = input("enter address: ")
        age = int(input("enter age: "))

        # create dictionary out of the information
        person = {
            "name": name,
            "address": address,
            "age": age
        }

        # add the newly created dictionary back to the list
        persons.append(person)

    print(persons)

# func9()
# enter name: ABC
# enter address: Earth
# enter age: 64
# enter name: DEF
# enter address: Mars
# enter age: 56
# enter name: GHI
# enter address: Earth
# enter age: 38
# enter name: JKL
# enter address: Andromeda
# enter age: 61
# enter name: MNO
# enter address: Alpha Centauri
# enter age: 29
# [{'name': 'ABC', 'address': 'Earth', 'age': 64}, {'name': 'DEF', 'address': 'Mars', 'age': 56}, {'name': 'GHI', 'address': 'Earth', 'age': 38}, {'name': 'JKL', 'address': 'Andromeda', 'age': 61}, {'name': 'MNO', 'address': 'Alpha Centauri', 'age': 29}]