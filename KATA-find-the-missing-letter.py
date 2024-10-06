# def find_missing_letter(chars):        
#     if chars[0].isupper():
#         up = True
#     else:
#         up = False
#     chars = [i.lower() for i in chars]
#     alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#     check = alphabet[alphabet.index(chars[0])+1:alphabet.index(chars[-1])+1]
#     return (set(check) - set(chars)).pop().upper() if up else (set(check) - set(chars)).pop()

import string  #lets import alphabet 
def find_missing_letter(chars):        
    up = chars[0].isupper()  #to print adequate
    
    chars = [char.lower() for char in chars] #to perform opertaions
    
    alphabet = string.ascii_lowercase
    
    check = alphabet[alphabet.index(chars[0])+1:alphabet.index(chars[-1])]
    missing = (set(check) - set(chars)).pop()  #get difference of full set and the one with missing letter .pop() to return 
    return missing.upper() if up else missing

