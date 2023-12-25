
f = open("Data.txt", "r")
data = f.readlines()

final = 0
for line in data:
    first_digit = "a"
    last_digit = "a"
    for character in line:
        if first_digit.isdigit() == False and character.isdigit() == True:
            first_digit = character
    for character in line[::-1]:
        if last_digit.isdigit() == False and character.isdigit() == True:
            last_digit = character
    combined = f"{first_digit}{last_digit}"
    final += int(combined)
print(final)
