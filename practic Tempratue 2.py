while True:
    tempratur_in_celsius = input("ride down a tempratur in celsius")
    question = input("what do you whana know")
    cast = float(tempratur_in_celsius)
    fahrenheit = (cast * 9 / 5) + 32
    kelvin = cast + 273.15
    if question=="fahrenheit":
        print(fahrenheit)
        break
    elif question=="kelvin":
        print(kelvin)
        break
    else:
        print("trey agen")
        continue


