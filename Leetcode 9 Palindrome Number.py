#Palindrome Number Leetcode 9

def isPalindrome(x):
    if(x<0):
        return False
    
    temp=x
    divisor=1
    while(temp>=10):
        divisor=divisor*10
        temp=temp//10
    
    while(x>0):
        right=x%10
        left=x//divisor
        
        if(right!=left):
            return False
        
        x=x%divisor
        x=x//10

        divisor=divisor//100  

    return True      
                


print(isPalindrome(1001))
