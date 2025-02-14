#Balanced ()
#(((())(())()((()))))(((())(())()((()))))(((())(())()((()))))()(((())(())()((()))))
### 
#(((())(())()((()))))(((())(())()((())))))((((())(())()((()))))(((())(())()((()))))

def string2list(string):
    list_ = []
    for i in string:
        list_.append(i)
    return list_
    
def check_input(string):
    work_list = string2list(string)
    while len(work_list) !=0 :
        if work_list[0]== ")":
            return False
        else:
            if not work_list.index(")") and len(work_list) > 0:
                return False
            else:
                index = work_list.index(")")
                work_list.pop(index)
                work_list.pop(index - 1)
    return True
    

        
def main():
    str1 = "(((())(())()((()))))(((())(())()((()))))(((())(())()((()))))()(((())(())()((()))))"
    str2 = "(((())(())()((()))))(((())(())()((())))))((((())(())()((()))))(((())(())()((()))))"
    if check_input(str2):
        print("True")
    else:
        print("False")

if __name__ == "__main__" :
    main()
