tempratur_in_celsius=input("ride down a tempratur in celsius")
tempratur_in_celsius=float(tempratur_in_celsius)
#its the conversion from celsius in fahrnheit
def fahrnheit(temp1):
    return (temp1*9/5)+32
#its the conversion from celsius in fahrnheit
def kelvin(temp2):
    return temp2+273.15
print("fahrenheit:", fahrnheit(tempratur_in_celsius), "Kelvin:", kelvin(tempratur_in_celsius))

