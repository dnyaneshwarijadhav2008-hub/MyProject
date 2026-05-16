# Write python function to print the table of given user input
def table():
  num = int(input("Enter a number : "))
  for i in range(1,11):
      print(f"{num} * {i} = {num * i}")
table()

# Rewrite table function while loop
def table_new():
  num = int(input("Enter a number : "))
  i = 1
  while i <= 10:
      print(f"{num} * {i} = {num * i}")
      i += 1
table_new()