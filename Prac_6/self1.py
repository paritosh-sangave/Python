def func1():
    # dictionary
    #- collectin of key - value pairs

    car = {
        "model": "F499",
        "company": "Ferrari",
        "price":15
    }

    # get all keys
    print(f"keys = {car.keys()}")

    # get all values
    print(f"values = {car.values()}")

    # check if key is present or not
    print(f'fuel type = {car.get("fuel Type")}')

    # add key if a key is not present in dictionary
    if car.get('fuel type') == None:
        car['fuel type'] = "petrol"

    print(car)

    # you can still add non-string key in dictionary
    # but it is discouraged to have a non-string key
    # car[10] = "test"
    # print(car)

# func1()
# keys = dict_keys(['model', 'company', 'price'])
# values = dict_values(['F499', 'Ferrari', 15])
# fuel type = None
# {'model': 'F499', 'company': 'Ferrari', 'price': 15, 'fuel type': 'petrol'}

def func2():
    # write a function check if person is eligible for voting
    def can_vote(person):
        if person['age']>=18:
            print(f"{person['name']} is eligible for voting")
        else:
            print(f"{person['name']} is NOT eligible for voting")
        
    
    # write a function to print all details of a person
    def print_person_details(person):
        print(f"name = {person['name']}")
        print(f"address = {person['address']}")
        print(f"age = {person['age']}")

    # person data
    person1 = {
        'name': "Baburao",
        'age': 62,
        'address': "mumbai"
    }

    print_person_details(person1)
    can_vote(person1)

# func2()
# name = Baburao
# address = mumbai
# age = 62
# Baburao is eligible for voting

