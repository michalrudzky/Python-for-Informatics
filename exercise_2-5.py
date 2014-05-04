# Write a program which prompts the user for a Celsius temperature,
# convert the temperature to Fahrenheit and print out the converted temperature.

c = raw_input("Celsius temperature: ")
celsius = float(c)

fahrenheit = celsius * 9.0 / 5.0 + 32

print "Fahrenheit temperature:", fahrenheit
