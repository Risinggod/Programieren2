tempratur_in_celsius = input("ride down a tempratur in celsius")
tempratur_in_celsius= float(tempratur_in_celsius)
def fahrnheit(temp1):
    return (temp1*9/5)+32
def kelvin(temp2):
    return temp2+273.15
while True:
    question = input("what do you whana know f or k")
    if question=="f":
        print(fahrnheit(tempratur_in_celsius))
        break
    elif question=="k":
        print(kelvin(tempratur_in_celsius))
        break
    else:
        print("trey agen")
        continue







