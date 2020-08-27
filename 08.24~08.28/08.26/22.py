def generateParenthesis(self, n: int) -> List[str]:
    res = []
    def generate(size: int, open_p: int, close_p: int, s: str):
        if open_p == size and close_p == size:
            res.append(s)
            return
        
        if open_p < size:
            generate(size, open_p+1, close_p, s+'(')
        if open_p > close_p:
            generate(size, open_p, close_p+1, s+')')
    
    generate(n,0,0,'')
    
    return res