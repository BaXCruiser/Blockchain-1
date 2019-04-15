from block import block
from chain import chain

if __name__=="__init__":        
    Blockchain=chain()
    print("Mining about to start ...............")
    print(Blockchain.getchain())
   last = Blockchain.current_block
   last_pno = last.pno
   pno = Blockchain.proof_of_work(last_pno)
   Blockchain.get_D(Sender="0",Receiver="pikachu",Amount=1)
   lastH = last.Hfun
   Block = Blockchain.make_block(pno, lastH)
   print("Mining sucessfull")
   print(Blockchain.chain)
© 2019 GitHub, Inc.
