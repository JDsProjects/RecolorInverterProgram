from os import system, name

# define our clear function


def clear():

    # for windows
    if name == "nt":
        _ = system("cls")

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


# Thank you https://www.geeksforgeeks.org/clear-screen-python/


complete_color_code = open("color_code.txt", "r")


# insert the color code into the color_code.txt file.

clear()

# the first digits like 8(refer to N64 usually, the only color bit is the 4 digits on the right.... - we still need to reinsert them imnto memory)

# explained to me by: https://www.youtube.com/watch?v=5lZ31AlgNzw


Inverted_color_code = []

Inverted_color_code_inverted = []

# here to check if both color codes match

lines = complete_color_code.readlines()

start_needed = ""

times_running64 = 0

while times_running64 < len(lines):

    needed_file = lines[times_running64]

    start_needed = start_needed + needed_file

    times_running64 = times_running64 + 1


# used orginally when the color code was in the main.py

times_ran_1 = 0

complete_color_code = str(start_needed)

lines = complete_color_code.split("\n")


while times_ran_1 < len(lines):

    if "" == lines[times_ran_1]:

        times_ran_1 = times_ran_1 + 1

        Inverted_color_code.append("")

        Inverted_color_code_inverted.append("")

        # it should always be correct, unless the hexcode doesn't work, right

    if not "" == lines[times_ran_1]:

        break

x = int(times_ran_1)

times_ran_program_1 = 0

# to check to make sure it doesn't go over, and sees if the first slot has a blank spot or not(and finds the first one, without a blank spot)


while x < len(lines):

    color_value = lines[x]

    color_value2 = lines[x + 1]

    colored_bit = color_value.split(" ")

    colored_bit2 = color_value2.split(" ")

    color_code_front = colored_bit[0]

    color_code_front2 = colored_bit2[0]

    color_section = colored_bit[1]

    color_section2 = colored_bit2[1]

    r = int(color_section[0:2], 16)
    g = int(color_section[2:4], 16)
    b = int(color_section2[0:2], 16)

    r = 0xFF - r
    g = 0xFF - g
    b = 0xFF - b

    # solution suggested by John10v10#5883

    bits_used998 = f"{r:0{2}x}{g:0{2}x}{b:0{2}x}"

    first_color_line = bits_used998[0:4].upper()

    second_color_line = bits_used998[4:6].upper()

    color_code_needed = color_code_front + " " + first_color_line

    color_code_needed_2 = (
        color_code_front2 + " " + second_color_line + color_section2[2:4]
    )

    Inverted_color_code.append(color_code_needed)

    Inverted_color_code.append(color_code_needed_2)

    x = x + 2

    times_ran_program_1 = times_ran_program_1 + 1

print("all", x - times_ran_1, "of the color code lines ran!")

times_ran_1 = 0


while times_ran_1 < len(Inverted_color_code):

    if "" == Inverted_color_code[times_ran_1]:

        times_ran_1 = times_ran_1 + 1

    if not "" == Inverted_color_code[times_ran_1]:

        break

z = int(times_ran_1)

while z < len(Inverted_color_code):

    color_value = Inverted_color_code[z]

    color_value2 = Inverted_color_code[z + 1]

    colored_bit = color_value.split(" ")

    colored_bit2 = color_value2.split(" ")

    color_code_front = colored_bit[0]

    color_code_front2 = colored_bit2[0]

    color_section = colored_bit[1]

    color_section2 = colored_bit2[1]

    r = int(color_section[0:2], 16)
    g = int(color_section[2:4], 16)
    b = int(color_section2[0:2], 16)

    r = 0xFF - r
    g = 0xFF - g
    b = 0xFF - b

    # solution suggested by John10v10#5883

    bits_used998 = f"{r:0{2}x}{g:0{2}x}{b:0{2}x}"

    first_color_line = bits_used998[0:4].upper()

    second_color_line = bits_used998[4:6].upper()

    color_code_needed = color_code_front + " " + first_color_line

    color_code_needed_2 = (
        color_code_front2 + " " + second_color_line + color_section2[2:4]
    )

    Inverted_color_code_inverted.append(color_code_needed)

    Inverted_color_code_inverted.append(color_code_needed_2)

    z = z + 2


if Inverted_color_code_inverted == lines:

    print("\nYour color code was succesfully inverted")

    want_it = "yes"

    want_it2 = "yes"

if not Inverted_color_code_inverted == lines:

    print("\nColor failed....")

    want_it = "yes"

    want_it2 = "yes"


j = int(times_ran_1)

test_string99 = ""


if want_it == "yes":

    print("\nInverted Color Code:")

    while j < len(Inverted_color_code):

        test_string99 = test_string99 + (Inverted_color_code[j] + "\n")

        j = j + 1

    print(test_string99)

jdjg = int(times_ran_1)

if want_it2 == "yes":

    print("\nOrginal Color Code that was inverted and was inverted back: ")

    test_string = ""

    while jdjg < len(Inverted_color_code_inverted):

        test_string = test_string + (Inverted_color_code_inverted[jdjg] + "\n")

        jdjg = jdjg + 1

    print(test_string)

    print("\nOrginal color code:")


jdjg_2 = times_ran_1

test_string998 = ""

while jdjg_2 < len(lines):

    test_string998 = test_string998 + (lines[jdjg_2] + "\n")

    jdjg_2 = jdjg_2 + 1

print(test_string998)

if test_string == test_string998:

    print("\n run 100% succesfully")

if not test_string == test_string998:

    print("\n didn't run successfully")


# Old inverters(don't work as well)

while True:

    input("\n press any button to close this window")

    break
