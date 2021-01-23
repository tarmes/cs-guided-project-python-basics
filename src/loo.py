def csWhereIsBob(names):
   for i, elem in enumerate(names):
      if elem == "Bob":
         return i
   return -1

def csWhereIsBob(names):
   bob = "Bob"
   if bob in names:
      return names.index("Bob")
   else:
      return -1



# print(csWhereIsBob(["Jimmy", "Layla", "Bob"]))
# print()
# print(csWhereIsBob(["Suzy", "Jim"]))

# def csWhereIsBob(names):
#    return names.index("Bob")

print(csWhereIsBob(["Jimmy", "Layla", "Bob"]))
print()
print(csWhereIsBob(["Suzy", "Jim"]))