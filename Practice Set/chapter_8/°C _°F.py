# 2. Write a python program using function to convert Celsius to Fahrenheit((°C to °F)).
# formula
# temperature_in_Fahrenheit=(temperature_in_Celsius*1.8)+32

def Fahrenheit(C):
    F=(C*1.8)+32
    return F

Celsius=float(input("Enter temperature in Celsius(°C):"))

print("Temperature in Fahrenheit is :",Fahrenheit(Celsius))
