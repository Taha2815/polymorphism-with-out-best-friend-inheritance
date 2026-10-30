class India():
    def capital(self):
         print("New Delhi is the capital of India")

    def language(self):
         print("Hindi is the most spoken language")

    def type(self):
             print("India is a developed country")

class USA():
    def capital(self):
         print("New Washington DC is the capital of USA")

    def language(self):
         print("Endlish is the most spoken language")

    def type(self):
             print("USA is a developed country")

obj_ind = India()
obj_USA = USA()

for country in (obj_ind, obj_USA):
      country.capital()
      country.language()
      country.type()
    
    
    


