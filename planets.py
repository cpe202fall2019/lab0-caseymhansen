def weight_on_planets():
   # write your code here
   earth_weight = float(input("What do you weigh on earth? "))
   # Converts user's earth weight into their equivalent mars weight
   mars_weight = earth_weight * 0.38
   # Converts user's earth weight into their equivalent jupiter weight
   jupiter_weight = earth_weight * 2.34
   text = "\nOn Mars you would weigh", mars_weight, "pounds.\nOn Jupiter you would weigh", jupiter_weight, "pounds."
   print(text[0], text[1], text[2], text[3], text[4])


if __name__ == '__main__':
   weight_on_planets()
