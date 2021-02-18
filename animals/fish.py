class Fish:
  def __init__(self):
        self.members = []

  def print_harmless(self):
        self.members = ['Baby Shark','Grandma Shark','Grandpa Shark']
        print ('The members are :')
        print([member for member in self.members])
  
  def print_dangerous(self):
        self.members = ['Mommay Shark','Daddy Shark','Sister Shark']
        print ('The members are :')
        print([member for member in self.members])
        
if __name__ == "__main__":
    Fish()

