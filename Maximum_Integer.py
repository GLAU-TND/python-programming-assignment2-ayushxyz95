a = eval(input()) 
ext = []
ans = "" 
l = len(str(max(a))) + 1
for i in a: 
    temp = str(i) * l 
    ext.append((temp[:l:], i)) 
      
 
ext.sort(reverse = True) 
      
    
for i in ext: 
    ans += str(i[1]) 
          
print(ans) 
  