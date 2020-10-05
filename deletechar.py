# Write a function delchar(s,c) that takes as input strings s and c, where c has length 1 (i.e., a single character), and returns the string obtained by deleting all occurrences of c in s. If c has length other than 1, the function should return s

def delchar(s,c):
    str_test = s
    if(len(c)>1):
        return(str_test)
    new_str = str_test.replace(c,"")
    return new_str


word = input("enter any word : ")
char = input("enter any character to delete : ")

a = delchar(word,char)
print(a)
