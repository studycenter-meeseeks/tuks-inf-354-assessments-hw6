def get_input(input_number):
    while True:
        current_input = input(f"Stick {input_number} length: ") #This is a literal string interpolation: https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
        try:
            correct_input = int(current_input)
            return correct_input
        except ValueError:
            print("please type in an integer number")


def is_triangle(length_1, length_2, length_3):
    # Triangle Inequality Theorem: the sum of the lengths of any two sides
    # of a triangle is greater than the length of the third side.
    creates_triangle = "No"

    if((length_1 + length_2) >= length_3):
        if((length_1 + length_3) >= length_2):
            if((length_2 + length_3) >= length_1):
                creates_triangle = "Yes"

    return creates_triangle


print("Please enter three stick lengths...")

stick_1 = get_input(1)
stick_2 = get_input(2)
stick_3 = get_input(3)

print(is_triangle(stick_1, stick_2, stick_3))
