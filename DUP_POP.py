def solution(A):
    
    ops = A.split()
    stack = []
 
    for i in range(0,len(ops)):
        
        I = 0
        if(ops[i] == "DUP"):
        
            if(len(stack) < 1): return -1           
            dup = stack.pop()
            stack.append(dup)
            stack.append(dup)
            
        elif(ops[i] == "POP"):
            
            if(len(stack) < 1): return -1          
            stack.pop()
            
        elif(ops[i] == "+"):
            
            if(len(stack) <= 1): return -1          
            I += int(stack.pop())
            I += int(stack.pop())
            stack.append(I)
            
        elif(ops[i] == "-"):
            
            if(len(stack) <= 1): return -1        
            I = int(stack.pop())
            I -= int(stack.pop())
            stack.append(I)
        
        else:
            stack.append(ops[i])
            print("single integer added:", stack, len(stack))
            
    if(len(stack) < 1 ): return -1
    else:
        return stack.pop()
    
B = "1 - + DUP POP"     

print(solution(B))
        
        
