class Bar:
  secret = 42

  def __init__(self, name):
    self.value = name
  
  def print_secret(self):
    print('%s, the answer to life and the universe is %d' % (self.value, Bar.secret))

if __name__ == '__main__':
  name = "Naveed"
  myObj = Bar(name)

  myObj.print_secret()