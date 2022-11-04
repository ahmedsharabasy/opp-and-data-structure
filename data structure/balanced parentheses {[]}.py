def areBracketsBalanced(expretion):
    stack=[]
    for char in expretion:
        if char in ["[","{","("]:
            stack.append(char)
        else:
            if not stack:
                return False   #كده انتهينا من الاقواس فى الستاك
            current_stack=stack.pop()
            if current_stack=="(":
                if char !=")":
                    return False
            if current_stack=="[":
                if char !="]":
                    return False                   
            if current_stack=="{":
                if char !="}":
                    return False

    if stack:
        return False    #  اقواس يعنى لسه موجود فيها
    return True         #مفيهاش                

if __name__=="__main__":
    if areBracketsBalanced("{[]}([{}])"):
        print('balanced')
    else:    
        print('not balanced')    


