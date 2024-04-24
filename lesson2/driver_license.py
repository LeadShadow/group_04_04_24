name = 'Sasha'
age = 18
has_driver_license = True
contact = '+380937316043'
money = 1000
# has_driver_license == True -> True, False
if name and age >= 18 and has_driver_license and contact and money >= 1000:
    print(f'User {name} can rent a car')

if name:
    if age >= 18:
        if has_driver_license:
            if contact:
                if money >= 1000:
                    print(f'User {name} can rent a car')
