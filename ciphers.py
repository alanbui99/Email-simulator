# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 23:56:15 2019

@author: Bui Thang
"""    
def scramble2Encrypt(plainText):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:            
        if charCount % 2 == 0:          
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
        charCount = charCount + 1
    cipherText = oddChars + evenChars
    return cipherText

def scramble2Decrypt(cipherText):
    if len(cipherText) % 2 == 0:
        halfLength = len(cipherText) // 2
        oddChars = cipherText[:halfLength]      
        evenChars = cipherText[halfLength-1:]     
        plainText = ""
    
        for i in range(halfLength):             
            plainText = plainText + evenChars[i]
            plainText = plainText + oddChars[i]
        plainText = plainText[:-1]
    else:
        halfLength = len(cipherText) // 2
        oddChars = cipherText[:halfLength]      
        evenChars = cipherText[halfLength:]     
        plainText = ""
    
        for i in range(halfLength):             
            plainText = plainText + evenChars[i]
            plainText = plainText + oddChars[i]

            
    return plainText
        



