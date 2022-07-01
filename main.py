import random

ROWS = 20
COLS = 12

# FUNCTIONS
# 1) Sales x Months' Matrix Creation
matrix = []
def create_matrix(n, m):

  for i in range(n):
    matrix.append([])
    for j in range(m):
      matrix[i].append(0)

  return matrix

# 2) Show Matrix
def show_matrix(mat):
  for row in matrix:
    for value in row:
      print("\t", value, end = " ")
    print()

# 3) Filling the Matrix
def fill_matrix():
  code = int(input("Enter the product's code: "))

  while(code != 0):
    while(code < 1 or code > ROWS):
      code = int(input("ALERT! Enter a valid product's code: "))

    day = int(input("Enter the sale's day: "))
    while(day < 1 or day > 31):
      day = int(input("ALERT! Enter a valid number: "))

    month = int(input("Enter the sale's month: "))
    while(month < 1 or month > COLS):
      month = int(input("ALERT! Enter a valid number (1 - 12): "))

    quant = int(input("Enter the sold's quantity: "))
    while(quant < 0):
      quant = int(input("ALERT! Enter a valid quantity: "))

    matrix[code - 1][month - 1] += prices[code - 1] * quant
    
    code = int(input("Enter the product's code: "))

# 4) Print sales per product, per month
def sales_x_month():
  for i in range(ROWS):
    for j in range(COLS):
      soldItems = int(matrix[i][j] / prices[i])
      print(f"The product #{i + 1} was sold {soldItems} times in the month {j + 1} ")

# 5) Print the product with the biggest profit
def max_profit():
  max = matrix[0][0]
  posRow = 0
  posCol = 0
  for i in range(ROWS):
    for j in range(COLS):
      if(matrix[i][j] > max):
        max = matrix[i][j]
        posRow = i
        posCol = j
  print(f"The product with the biggest profit was the product #{posRow + 1}, in the {posCol + 1}º month, with a total of ${max}.")

# 6) Profits per Quarter
quarterProfits = []
def quarter_profits():
  quarter = 1
  quarterFrom = 0 
  quarterTo = 3

  while(quarterTo <= COLS):
    colArr = 0
    for j in range(quarterFrom, quarterTo):
      accCol = 0
      for i in range(ROWS):
        accCol += matrix[i][j]
      colArr += accCol

    quarterProfits.append(colArr)

    print(f"The {quarter}º quarter has a total of ${colArr} per month")
    quarterFrom += 3
    quarterTo += 3
    quarter += 1

# 7) Print the quarter with less profits
def less_profit():
  min = quarterProfits[0]
  pos = 0
  for i in range(len(quarterProfits)):
    if(quarterProfits[i] < min):
      min = quarterProfits[i]
      pos = i
  print(f"The quarter with less profits is the {pos + 1}º with a total of ${min}")

# Prices Array with its prices (Product code is relative to the arr position)
prices = []
for x in range(ROWS):
  #value = int(input(f"Enter the price of the item #{x + 1}: "))
  value = int(random.randint(100, 500))
  prices.append(value)

# MAIN
create_matrix(ROWS, COLS)
fill_matrix()
show_matrix(matrix)
sales_x_month()
max_profit()
quarter_profits()
less_profit()