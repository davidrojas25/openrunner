def kilometers_to_miles(kilometers):
  miles = 0.00
  # conversion factor
  conv_fac = 0.621371
  # calculate miles
  miles = kilometers * conv_fac
  print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))

def miles_to_laps(miles):
    laps = 0.00
    laps = miles * 4
    return laps


kilometers_to_miles(float(input("Enter value in kilometers: ")))

miles1 = float(input("Enter the number of miles: "))
laps1 = miles_to_laps(miles1)
print("Your Track race will have " + str(laps1))          
          
          
