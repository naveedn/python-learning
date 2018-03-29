from models.Bar import *
from models.Baz import *

def create_objects(name, listOfFriends):
  mybar = Bar(name)
  mybaz = Baz(listOfFriends)
  print_secrets(mybar, mybaz)

def print_secrets(bar, baz):
    bar.print_secret()
    baz.print_secret()
  