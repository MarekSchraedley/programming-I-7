from stanfordkarel import *
#prog name is h

class ktools:
  def m(self):
    """Shorthand For Move"""
    move()
  def tl(self):
    """turnleft"""
    turn_left()
  def tr(self):
    """Turn Right"""
    self.tl()
    self.tl()
    self.tl()
  def ta(self):
    """Turn Around"""
    self.tl()
    self.tl()
  def pick(self):
    """Pick Beeper"""
    pick_beeper()
  def put(self):
    """Put Beeper"""
    put_beeper()
  def put2(self):
    """put 2 beepers in a line"""
    self.put()
    self.m()
    self.put()
  def put5(self):
    """5 beepers in line"""
    self.put2()
    self.m()
    self.put2()
    self.m()
    self.put()
  def h(self):
    """print h using beepers"""
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.m()
    self.m()
    self.tr()
    self.put5()
    self.ta()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.put2()
    self.tl()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.m()
    self.m()
    self.m()
  def e(self):
     self.tl()
     self.put5()
     self.tr()
     self.m()
     self.put2()
     self.tr()
     self.m()
     self.m()
     self.tr()
     self.put2()
     self.m()
     self.tl()
     self.m()
     self.m()
     self.tl()
     self.m()
     self.put2()
     self.m()
     self.m()
  def l(self):
     self.tl()
     self.put5()
     self.ta()
     self.m()
     self.m()
     self.m()
     self.m() 
     self.tl()
     self.m()
     self.put2()
     self.m()
     self.m()
  def o(self):
     self.tl()
     self.put5()
     self.tr()
     self.m()
     self.put2()
     self.m()
     self.tr()
     self.put5()
     self.tr()
     self.m()
     self.put2()
def main():
    """ Karel code goes here! """
    kt = ktools()

    kt.m()
    kt.tl()
    kt.m()
    kt.put5()
    kt.m()
    kt.put2()
    kt.m()
    kt.put()
    kt.tr()
    kt.m()
    kt.put5()
    kt.m()
    kt.put2()
    kt.tr()
    kt.m()
    kt.put5()
    kt.m()
    kt.put2()
    kt.tr() 
    kt.m()
    kt.put5()
    kt.m()
    kt.put()
   
   

    pass
  


if __name__ == "__main__":
    run_karel_program()
