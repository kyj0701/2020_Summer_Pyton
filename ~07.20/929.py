emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
res = []
        
for i in emails:
    a = i.find('@')
    local = i[:a]
    domain = i[a:]
            
    b = i.find('+')
            
    if b >= 0:
        local = local[:b]
        print(local)
                         
    local = local.replace(".", "")
            
    res.append(local + domain)
            
s1 = set(res)
        
res = list(s1)
        
print(res)