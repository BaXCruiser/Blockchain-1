import hashlib
class block:
  def __init__(self,Sno,time,phash,D):
    self.Sno = Sno
    self.time = time
    self.phash = phash
    self.D = D
    self.H = self.Hfun()
    
  def Hfun(self):
      Var= hashlib.sha256()
      Var.update(str(self.Sno) + 
               str(self.time) + 
               str(self.phash) + 
               str(self.D))
      """  hexdigest() :return hexadecimal digits """
      return Var.hexdigest()
