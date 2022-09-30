from stanfordkarel import *
from time import sleep
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
  def fic(self):
    """front is clear"""
    return front_is_clear()
  def fib(self):
    """front is blocked"""
    return not self.fic()
  def ric(self):
    """right is clear"""
    self.tr()
    if self.fic():
      self.tl()
      return True
    self.tl()
    return False
  def rib(self) -> bool:
    """right is blocked"""
    return not self.ric()
  def mazemove(self):
    """Maze Move"""
    if self.fib():
      self.tl()
    else: 
      self.m()
      if self.ric():
        self.tr()
        self.m()
        if self.ric():
          self.tr()
          self.m()
  
  pass
  def mm(self, num):
    """move multiple"""
    for number in range(0, num):
      self.m()
  def putm(self, num):
    """put multiple"""
    for i in range(num -1):
      self.put()
      self.m()
    self.put()
  def pickm(self, num):
    """pick multiple"""
    for _ in range(num - 1):
      self.pick()
      self.m()
    self.pick()
    """print h using beepers"""
  def put0(self, num):
    for number in range(0, num):
      self.o()
      
  
  def SOB(self) -> bool:
    """standing on beeper"""
    return beepers_present()
    
  def jump(self):
    """jump for 510"""
    while self.fic():
      self.m()
    self.tl()
    while self.rib():
      self.m()
    self.tr()
    self.m()
    self.tr()
    while self.fic():
      self.m()
    self.tl()
   
  def find(self):
    """find for 515"""
    while not facing_north():
      self.tl()
    self.m()
    if not self.SOB():
      self.tl()
      self.m()
      self.tl()
      self.m()
    for _ in range(2):
      if not self.SOB():
        self.m()
        self.tl()
        self.m()
        
    pass
def main():
    """ Karel code goes here! """
   
    kt = ktools()
    kt.m()
    kt.tl()
    kt.mm(4)
    while not kt.SOB():
      if kt.fib():
         kt.tr()
         kt.put()
         kt.m()

        
      if kt.fic() and kt.rib():
        if not kt.SOB():
         kt.put()
         kt.m()

    pass
  
  


if __name__ == "__main__":
    run_karel_program()