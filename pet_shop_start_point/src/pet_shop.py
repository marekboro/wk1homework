# WRITE YOUR FUNCTIONS HERE


def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, num):
    pet_shop["admin"]["total_cash"] += num


def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]


def increase_pets_sold(pet_shop, num):
    pet_shop["admin"]["pets_sold"] += num


def get_stock_count(pet_shop):
    return len(pet_shop["pets"])


def get_pets_by_breed(pet_shop, breed):
    pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pets.append(pet)
    return pets  # First test(L118) will be OK without this line... WHY?


def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet


def remove_pet_by_name(pet_shop, pet_name):
    pet_index = -1
    for pet in pet_shop["pets"]:
        pet_index += 1
        if pet["name"] == pet_name:
            pet_shop["pets"].pop(pet_index)


def add_pet_to_stock(pet_shop, a_new_pet):
    pet_shop["pets"].append(a_new_pet)


def get_customer_cash(customers):
    return customers["cash"]


def remove_customer_cash(customer, cash):
    customer["cash"] -= cash


def get_customer_pet_count(customer):
    return len(customer["pets"])


def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)


def customer_can_afford_pet(customer, pet):
    if pet is None:
        return False
    else:
        pet_price = pet["price"]
        if get_customer_cash(customer) >= pet_price:
            return True
        else:
            return False


def sell_pet_to_customer(pet_shop, pet, customer):

    if customer_can_afford_pet(customer, pet):
        remove_customer_cash(customer, pet["price"])
        customer["pets"].append(pet)
        increase_pets_sold(pet_shop, 1)
        add_or_remove_cash(pet_shop, pet["price"])
        remove_pet_by_name(pet_shop, pet)


# WALL OF SHAME - aka - the code that was written and pondered over because I did not read the ERROR message in the terminal idicating that the problem was with cusotmer can afford pet.

# def add_or_remove_cash(pet_shop, num):
#     # get_total_cash(pet_shop) +=num
#     # WHY CANT I USE THIS ABOVE?
#     # tatal = get_total_cash(pet_shop)
#     # tatal += num
#     pet_shop["admin"]["total_cash"] += num


# #WORKS for q4 in OPTIONAL but not for q5 !
# def sell_pet_to_customer(pet_shop, pet, customer):
#     pet_found = find_pet_by_name(pet_shop, pet["name"])
#     # if find_pet_by_name(pet_shop,pet):
#     if pet_found and customer_can_afford_pet(customer, pet):
#         remove_customer_cash(customer, pet["price"])
#         customer["pets"].append(pet)
#         increase_pets_sold(pet_shop, 1)
#         add_or_remove_cash(pet_shop, pet["price"])
#         remove_pet_by_name(pet_shop, pet)

# fake pet approach:


# def sell_pet_to_customer(pet_shop, pet, customer):
#     print("")
#     print(f"Customer pet count = {get_customer_pet_count(customer)}")
#     print(f"Customer name = +{customer["name"]}")

#     if find_pet_by_name(pet_shop, pet["name"])== None:


#         pet_exists = False
#     else:
#         #pet_found = find_pet_by_name(pet_shop, pet["name"])
#         print("A")
#         #print(f" pet found =  + {pet_found}")
#         print("B")
#         # if find_pet_by_name(pet_shop,pet):
#         if pet_exists and customer_can_afford_pet(customer, pet):
#             remove_customer_cash(customer, pet["price"])
#             customer["pets"].append(pet)
#             increase_pets_sold(pet_shop, 1)
#             add_or_remove_cash(pet_shop, pet["price"])
#             remove_pet_by_name(pet_shop, pet)


# def customer_can_afford_pet(customer,pet_shop, pet_name):
#     min_pet_price = 0
#     for pet in pet_shop["pets"]:
#         if min_pet_price > pet["price"]:
#             min_pet_price = pet["price"]
#             break
#         else:
#             min_pet_price = pet["price"]

#     if get_customer_cash(customer) > min_pet_price:
#         return True


# def sell_pet_to_customer(pet_shop, pet, customer):
#     pet_found = find_pet_by_name(pet_shop, pet["name"])
#     if pet_found is not None:
#         if customer_can_afford_pet(customer, pet):
#             remove_customer_cash(customer, pet["price"])
#             customer["pets"].append(pet)
#             increase_pets_sold(pet_shop, 1)
#             add_or_remove_cash(pet_shop, pet["price"])
#             remove_pet_by_name(pet_shop, pet)

# def sell_pet_to_customer(pet_shop, pet, customer):
#     pet_found = True

#     if pet_found and customer_can_afford_pet(customer, pet):
#         remove_customer_cash(customer, pet["price"])
#         customer["pets"].append(pet)
#         increase_pets_sold(pet_shop, 1)
#         add_or_remove_cash(pet_shop, pet["price"])
#         remove_pet_by_name(pet_shop, pet)


# def find_pet_by_name(pet_shop, pet_name):
#     for pet in pet_shop["pets"]:
#         if pet["name"] == pet_name:
#             return pet

# def sell_pet_to_customer(pet_shop, pet, customer):
#     print("TEST")
#     print(f"{find_pet_by_name(pet_shop,pet)}")
#     if (find_pet_by_name(pet_shop,pet) == None):

#         print("TEST 2")
#         if customer_can_afford_pet(customer, pet):
#             print("TEST 3")
#             remove_customer_cash(customer, pet["price"])

#             customer["pets"].append(pet)
#             increase_pets_sold(pet_shop, 1)
#             add_or_remove_cash(pet_shop, pet["price"])
#             remove_pet_by_name(pet_shop, pet)


# def find_pet_by_name2(pet_shop, pet_name):
#     found = False
#     # for pet in pet_shop["pets"]:
#     #     print(pet["name"])
#     #     if found =0:
#     #         if pet["name"] == pet_name:
#     #             return pet
#     #             found +=1
#     length = len(pet_shop["pets"])
#     i = 0
#     found_pet = None
#     # Iterating using while loop
#     while i < length && !found:
#         print(list[i])
#         if pet["name"] === pet_name:
#             found_pet = pet
#             found = True
#         i += 1
#     return found_pet


# THIS is the function that fails !!!!!!
# WORKDED up until TEST 21, TEST 22 & 23 failed.
# def customer_can_afford_pet(customer, pet):
#     pet_price = pet["price"]
#     if get_customer_cash(customer) >= pet_price:
#         return True
#     else:
#         return False


# This one is broken - why?
# def find_pet_by_name(pet_shop,pet_name):
#     the_pet = {}
#     for pet in pet_shop["pets"]:
#         if pet["name"] == pet_name:
#             the_pet = pet
#             return the_pet
