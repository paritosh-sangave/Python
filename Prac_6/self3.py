class Car:
    pass

def add_attributes_to_Car(car, model, company, price):
    setattr(car, 'model', model)
    setattr(car, 'company', company)
    setattr(car, 'price', price)
    # object name, field/variable name, value

def print_details_of_Car(car):
    print(f"model = {getattr(car, 'model')}")
    print(f"company = {getattr(car, 'company')}")
    print(f"price = {getattr(car, 'price')}")

car1 = Car()
add_attributes_to_Car(car1, 'F175', 'Ferrari', 17)
print_details_of_Car(car1)
# model = F175
# company = Ferrari
# price = 17

car2 = Car()
add_attributes_to_Car(car2, 'RB18', "Red Bull RBPT", 19)
print_details_of_Car(car2)
# model = RB18
# company = Red Bull RBPT
# price = 19

# create an empty class for Mobile
# add attribute: model, company, price
# add functions: add_attributes, print_details, is_affordable

class Mobile:
    pass

def add_attributes_to_Mobile(mobile, model, company, price):
    setattr(mobile, 'model', model)
    setattr(mobile, 'company', company)
    setattr(mobile, 'price', price)

def print_details_of_Mobile(mobile):
    print(f"model = {getattr(mobile, 'model')}")
    print(f"company = {getattr(mobile, 'company')}")
    print(f"price = {getattr(mobile, 'price')}")

def is_affordable(mobile):
    if getattr(mobile, 'price') <= 15000:
        print(f"{getattr(mobile, 'model')} is affordable")
    else:
        print(f"{getattr(mobile, 'model')} is NOT affordable")
    
mobile1 = Mobile()
add_attributes_to_Mobile(mobile1, 'N95', 'Nokia', 8000)

mobile2 = Mobile()
add_attributes_to_Mobile(mobile2, 'iPhone 14', 'Apple', 150000)

print_details_of_Mobile(mobile1)
is_affordable(mobile1)
# model = N95
# company = Nokia
# price = 8000
# N95 is affordable

print()

print_details_of_Mobile(mobile2)
is_affordable(mobile2)
# model = iPhone 14
# company = Apple
# price = 150000
# iPhone 14 is NOT affordable
