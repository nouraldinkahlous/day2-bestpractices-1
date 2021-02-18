class Mammals:
  def __init__(self):
        self.members = []
        
  def print_harmless(self):
        self.members = ['Cow','Horse','Goat']
        print ('The members are :')
        print([member for member in self.members])

  def print_dangerous(self):
        self.members = ['Lion','Tiger','Fox']
        print ('The members are :')
        print([member for member in self.members])   
        
if __name__ == "__main__":
    Mammals()
