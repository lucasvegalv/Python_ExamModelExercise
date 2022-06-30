import random

# FUNCTIONS
# 1) Sales x Months' Matrix Creation
matrix = []
def create_matrix(n, m, value):

  for i in range(n):
    matrix.append([])
    for j in range(m):
      matrix[i].append(value)

  return matrix

# 2) Print the matrix
def show_matrix(mat):
  for row in matrix:
    for value in row:
      print("\t", value, end = " ")
    print()

# 3) Filling the Matrix
def fill_matrix():
  code = int(input("Enter the product's code: "))

  while(code != 0):
    while(code < 1 or code > 20):
      code = int(input("ALERT! Enter a valid product's code: "))

    day = int(input("Enter the sale's day: "))
    while(day < 1 or day > 31):
      day = int(input("ALERT! Enter a valid number: "))

    month = int(input("Enter the sale's month: "))
    while(month < 1 or month > 12):
      month = int(input("ALERT! Enter a valid number (1 - 12): "))

    quant = int(input("Enter the sold's quantity: "))
    while(quant < 0):
      quant = int(input("ALERT! Enter a valid quantity: "))

    matrix[0][0] = prices[0]*{quant}
    
    code = int(input("Enter the product's code: "))

# Prices Array with its prices (Product code is relative to the arr position)
prices = []
for x in range(20):
  #value = int(input(f"Enter the price of the item #{x + 1}: "))
  value = int(random.randint(100, 500))
  prices.append(value)

# Print each product code with its price
#for x in range(len(prices)):
  #print(f"The product #{x + 1} costs ${prices[x]}")

print(prices)
create_matrix(20, 12, 0)
show_matrix(matrix)
fill_matrix()
show_matrix(matrix)

# Informing: Details for each product for each month, product with more profits, quarter with less profits