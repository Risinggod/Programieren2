with open("Tempratur.txt", "w") as file:
    tempratur_in_celsius=input("ride down a tempratur in celsius")
    cast=float(tempratur_in_celsius)
    fahrenheit=(cast*9/5)+32
    kelvin=cast+273.15
    solution=print("Fahrenheit:", fahrenheit, "kelvin:", kelvin)
    cast2=str(solution)
    file.write(cast2)












