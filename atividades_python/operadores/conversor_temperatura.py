# Conversor de temperaturas: escreva um programa que converta uma temperatura digitada em ºC para ºF e vice-versa.

#ºC para ºF = (ºC * 9/5) + 32
#ºF para ºC = (ºF - 32) * 5/9

temperatura_celsius = float(input("Digite a temperatura em ºC: "))
temperatura_fahrenheit = float(input("Digite a temperatura em ºF: "))

conversor_celsius_fahrenheit = (temperatura_celsius * 9/5) + 32
conversor_fahrenheit_celsius = (temperatura_fahrenheit - 32) * 5/9

print("A temperatura",temperatura_celsius,"º convertida em fahrenheit é:",conversor_celsius_fahrenheit,"ºF")
print("A temperatura",temperatura_fahrenheit,"ºF convertida em celsius é:",conversor_fahrenheit_celsius,"ºC")