def __init__(self, nestedList: [NestedInteger]):
    
    def check(ins):
        res = []
        
        for i in ins:
            if i.isInteger():
                res.append(i.getInteger())
            else:
                res.extend(check(i.getList()))
        return res
    
    self.result = check(nestedList)
    self.x = 0
            
def next(self) -> int:
    ins = self.result[self.x]
    self.x += 1
    return ins

def hasNext(self) -> bool:
    return self.x < len(self.result)