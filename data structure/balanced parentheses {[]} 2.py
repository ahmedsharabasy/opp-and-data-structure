opened_parentheses=['(','{','[']
closed_parentheses=[')','}',']']

def check(expersion):
    stack=[]
    for i in expersion:
        if i in opened_parentheses:
            stack.append(i)
        elif i in closed_parentheses:
            popped= stack.pop()
            if ((popped+i !='()')and(popped+i!='{}')and(popped+i!='[]')):
                return "unbalanced"
    if stack==[]:
        return 'balanced'
    else:
        return 'unbalanced'    

strr='[]{kk(jkkl)}'
print(strr+"  "+check(strr))                    
