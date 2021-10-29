#5.1
car = "ford"
assumption = "FORD"
print(f"Is car {assumption.title()}:")
print(car.lower() == assumption.lower())

car = "BMV"
assumption = "mazda"
print(f"Is car {assumption.title()}:")
print(car.lower() == assumption.lower())

car = "BMV"
assumption = "bmv"
print(f"Is car {assumption.upper()}:")
print(car.lower() == assumption.lower())

car = "KIA"
assumption = "KIA"
print(f"Is car {assumption.upper()}:")
print(car.lower() == assumption.lower())

car = "Mitsubishi"
assumption = "MITSUBISHI"
print(f"Is car {assumption.title()}:")
print(car.lower() == assumption.lower())

car = "Volga"
assumption = "Car"
print(f"Is car {assumption.title()}:")
print(car.lower() == assumption.lower())

print("\n\n")

#5.2
some_title = "Squad"
print("Is equal: " + str(some_title.lower() == "squad" + "\n"))

rand_num = 993
print(rand_num > 999)
print(rand_num < 999)
print(rand_num >= 100)
print(rand_num <= 100)
print( (rand_num > 500) and (rand_num < 1000) )
print( (rand_num < 900) or (rand_num == 993) )
print("\n")

generated_list = [var for var in range(100)]
if 20 in generated_list:
    print("20 in list")
else:
    print("List dosn't contain 20")

if 900 in generated_list:
    print("900 in list")
else:
    print("List dosn't contain 900")

if 100 not in generated_list:
    print("True 100")
if 99 not in generated_list:
    print("True 99")