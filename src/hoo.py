def csOppositeReverse(txt):
   reversed = ""
   for x in txt:
      if x.islower():
         reversed = reversed + x.upper()
         print(reversed)
      else:
         reversed = reversed + x.lower()
         print(reversed)
   return reversed[::-1]


print(csOppositeReverse("Hello World!"))
