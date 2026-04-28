'''Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.'''

celsius = float(input('Informe a temperatura em °C: '))

fahrenheit = (celsius * 1.8) + 32 #Fórmula de Celsius para Fahrenheit

print('A temperatura de {}°C corresponde a {}°F!'.format(celsius, fahrenheit))



