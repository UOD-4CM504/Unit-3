x = int(input("Please enter a number:\n"))

if x % 3 == 0:
  if x % 5 == 0:
    print("Your number is divisible by 3 and 5.")
  else:
    print("Your number is divisible by 3 and NOT by 5.")
else:
  if x % 5 == 0:
    print("Your number is NOT divisible by 3 and is divisible by 5.")
  else:
    print("Your number is NOT divisible by 3 and 5.")