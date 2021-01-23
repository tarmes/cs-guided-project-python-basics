def csAlphanumericRestriction(input_str):
   if input_str.isalpha() or input_str.isdigit():
      return True
   else:
      return False




print(csAlphanumericRestriction("Bold"))
print()
print(csAlphanumericRestriction("20202020"))
print()
print(csAlphanumericRestriction("BOBOOBO293849384"))