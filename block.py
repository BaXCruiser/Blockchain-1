import hashlib
import time as t
class block:
  def __init__(self,Sno,pno,time=None,phash,D):
    self.Sno = Sno
    self.pno= pno
    self.time = time or t.time()
    self.phash = phash
    self.D = D
    self.H = self.Hfun()

  def __repr__(self):
     return "{} - {} - {} - {} - {}".format(self.Sno, self.pno, self.phash, self.time, self.D)

  def Hfun(self):
      Var= hashlib.sha256()
      Var.update(str(self.Sno) + str(self.pno) + str(self.time) + str(self.phash) + str(self.D))
      """  hexdigest() :return hexadecimal digits """
      return Var.hexdigest()
