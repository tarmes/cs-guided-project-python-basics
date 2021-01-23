def csSchoolYearsAndGroups(years, groups):
   alphabet="abcdefghijklmnopqrstuvwxyz"
   groupNames = ""
   yearCount = 0
   while (yearCount < years):
      yearCount = yearCount + 1
      groupCount = 0
      while (groupCount < groups):
         groupNames = groupNames + str(yearCount) + alphabet[groupCount] + ", "
         groupCount = groupCount + 1
   return groupNames

print(csSchoolYearsAndGroups(7, 4))


string = "Hello and Goodbye!"
print(string[0:-4])