import block

class chain(object):
    def _init_(self):
        self.chain = []
        self.currentD = []
        self.node = set()
        self.block0()
        
    def block0(self):
        self.build_block(pn=0, phash=0)
    
    def make_block(self, pno, phash):
        block = Block(
            Sno=len(self.chain),
            pno=pno,
            phash=phash,
            data=self.currentD
        )
        self.currentD = []
        self.chain.append(block)
        return block
        
    @staticmethod
    def validity(block, pre_block):
        if pre_block.Sno + 1 != block.Sno:
            return False
        elif pre_block.Hfun != block.pre_hash:
            return False
        elif block.time <= previous_block.time:
            return False
        return True
        
    def getD(self, sender, receiver, amount):
        self.current_D.append({'Sender': sender,'Receiver': receiver,'Amount': amount})
        return True
        
    @staticmethod
    def proof_of_work(proof):
        pass
        
    @property
    def current_block(self):
        return self.chain[-1]
        
    def chain_validity(self):
        pass
        
    def Mining(self, details):
        self.getD(
            sender="0", # this node has created a new block
            receiver=details,
            quantity=1, #creating a new block is awarded with 1
        )
        last = self.current_block
        last_pno = last.pno
        pno = self.proof_of_work(last_pno)
        lastH = last.Hfun
        block = self.make_block(pno, last_hash)
        return vars(block)
        
    def make_node(self, address):
        self.node.add(address)
        return True
        
    @staticmethod
    def get_block_object(block1):
        return block(
            block1['Sno'],
            block1['pno'],
            block1['phash'],
            block1['D'],
            time=block1['time']
        )
