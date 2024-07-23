# This program converts a numeric grade to an alpha grade

input_bool = False

while not input_bool:
  input_grade = int(input("Please enter the grade you wish to convert (0-100).\n"))
  if (input_grade >= 0) or (input_grade <= 100):
    input_bool = True

  print("ERROR: input not between 0 and 100\n")

output_grade = ""
if input_grade <= 35:
  output_grade = "F"
elif input_grade <= 40:
  output_grade = "MF"
elif input_grade <= 50:
  output_grade = "D"
elif input_grade <= 60:
  output_grade = "C"
elif input_grade <= 70:
  output_grade = "B"
elif input_grade <= 80:
  output_grade = "A-"
elif input_grade <= 90:
  output_grade = "A"
else:
  output_grade = "A+"

print(f"{input_grade} = {output_grade}.")