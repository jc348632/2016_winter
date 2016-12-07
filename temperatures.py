"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
def main():
    __author__ = 'Lindsay Ward'

    MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = conv_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            # TODO: Write this section so the program converts F to C and displays the result
            # Hint: celsius = 5 / 9 * (fahrenheit - 32)
            fahrenheit = float(input("Fahrenheit: "))
            celcius = conv_celcius(fahrenheit)
            print("Result: {:.2f} F".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def conv_celcius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius

def conv_fahrenheit(celcius):
    fahrenheit = celcius * 9.0 / 5 + 32
    return fahrenheit

main()