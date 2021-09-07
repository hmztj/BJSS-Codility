def solution(A):
    
    counters = {"Onco":0, "Ortho":0 }
    
    for i in range(0,len(A)):
        
        if(A[i] == "Onco"):
            
            counters[A[i]] +=1
            
        elif(A[i] == "Ortho"):
            
            counters[A[i]] +=1

    return max(counters.values())

A = ["Onco", "Onco", "Ortho"]

print(solution(A))