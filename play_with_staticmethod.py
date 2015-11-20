#
# $ python play_with_staticmethod.py 
# bbb
#
class Foo():

  @staticmethod
  def meth(name):
    return name

  def __init__(self):
    myname = Foo.meth('bbb') 
    print  myname

Foo()

