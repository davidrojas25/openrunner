def kilometers_to_miles(kilometers):
  miles = 0.00
  # conversion factor
  conv_fac = 0.621371
  # calculate miles
  miles = kilometers * conv_fac
  print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))



kilometers_to_miles(float(input("Enter value in kilometers: ")))


