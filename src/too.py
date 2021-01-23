def csSquareAllDigits(n):
   newNum = ""
   for x in str(n):
      newNum = newNum + str(int(x)**2)
   return int(newNum)

print(csSquareAllDigits(943))   