class Baz:
  secret = {
    'Bruno': 1,
    'Brian': 2,
    'Jun': 3,
    'Simon': 4,
    'Rei': 5,
    'Paul': 6,
    'Adam': 7,
    'Joe': 8,
    'Vipin': 9,
    'Rathi': 10,
    'Jude': 11
  }

  def __init__(self, listOfFriends):
    self.value = listOfFriends
  
  def print_secret(self):
    for (name, idx) in self.secret.items():
      print('%d => %s' % (idx, name))
    
    for friend in self.value:
      print(friend)


if __name__ == '__main__':
  listOfFriends = ['Ani', 'Zill', 'Omar']
  bazz = Baz(listOfFriends)
  bazz.print_secret()
