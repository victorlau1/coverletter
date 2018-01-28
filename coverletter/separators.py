class Separators(self):

  #Separators to find where to input configuration
  separators = [
    "[]",
    "{}",
    '//'
  ]

    def __init__(self):
      chosen_selector = True

      while chosen_selector:
        selector = input('What selctor would you like to use?')
        if selector in separators:
          chosen_selector = False
          return selector
          

