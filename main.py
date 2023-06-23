from math import sqrt


def pythagoras():
    x = input("Choose one of them: \n Base (a): \n Height (b): \n Hypotenuse (c): ").upper()

    if x == "A":
        try:
            height = float(input("Enter the height value: "))
            hypotenuse = float(input("Enter the hypotenuse value: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            return

        if height < 0:
            print("Height cannot be negative.")
            return

        base_squared = hypotenuse ** 2 - height ** 2
        if base_squared < 0:
            print("Invalid input. The hypotenuse value is too small.")
            return

        base = sqrt(base_squared)
        print("Base: {:.2f}".format(base))

    elif x == "B":
        try:
            base = float(input("Enter the base value: "))
            hypotenuse = float(input("Enter the hypotenuse value: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            return

        if base < 0:
            print("Base cannot be negative.")
            return

        height_squared = hypotenuse ** 2 - base ** 2
        if height_squared < 0:
            print("Invalid input. The hypotenuse value is too small.")
            return

        height = sqrt(height_squared)
        print("Height: {:.2f}".format(height))

    elif x == "C":
        try:
            base = float(input("Enter the base value: "))
            height = float(input("Enter the height value: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            return

        if height < 0 or base < 0:
            print("Height and base cannot be negative.")
            return

        hypotenuse = sqrt(height ** 2 + base ** 2)
        print("Hypotenuse: {:.2f}".format(hypotenuse))

    else:
        print("Invalid choice.")


pythagoras()
