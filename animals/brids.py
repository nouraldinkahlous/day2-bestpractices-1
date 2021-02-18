class Brids:
  def __init__(self):
        self.members = []

  def print_harmless(self):
        self.members = ['Duck','Sparrow','Robin']
        print ('The members are :')
        print([member for member in self.members])

  def print_dangerous(self):
        self.members = ['Owl','Eagle','Crow']
        print ('The members are :')
        print([member for member in self.members])
        
if __name__ == "__main__":
    Brids()
