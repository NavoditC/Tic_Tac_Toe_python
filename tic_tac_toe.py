# -*- coding: utf-8 -*-
"""
Created on Sun May 16 15:04:46 2021

@author: Navodit
"""
def disp(ml):
    print('{}|{}|{}\n------\n'.format(ml[0],ml[1],ml[2]))
    print('{}|{}|{}\n------\n'.format(ml[3],ml[4],ml[5]))
    print('{}|{}|{}\n\n'.format(ml[6],ml[7],ml[8]))
    
def check(ml,char):
    for i in range(0,7,3):  #To check horizontal row
        if ml[i]==char and ml[i+1]==char and ml[i+2]==char:
            return True
    
    for i in range(0,3):  #To check vertical row
        if ml[i]==char and ml[i+3]==char and ml[i+6]==char:
            return True
    
    if ml[0]==char and ml[4]==char and ml[8]==char: #Diagonal elements
        return True
    if ml[2]==char and ml[4]==char and ml[6]==char:
        return True
    return False

ch='Y'
ml=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
i=1
ch1=input('Player 1 choose either O or * as the symbol\n')
while ch1!='O' and ch1!='*':
    ch1=input('Player 1 choose either O or * as the symbol\n')
ch2='O'
if ch1=='O':
    ch2='*'
print('Symbol of player 1 is {}\n'.format(ch1))
print('Symbol of player 2 is {}\n'.format(ch2))
print('Location of indices is as follows\n')
disp([1,2,3,4,5,6,7,8,9])
dup_list=[0,0,0,0,0,0,0,0,0]
    
while i<=9:
    if i%2!=0:
        index=input('Player 1: Choose an index between 1 and 9\n')
        if index.isdigit()==False:
            index=input('Enter a number between 1 and 9\n')
        if int(index) not in range(1,10):
                index=input('The index must be between 1 and 9\n')
        index=int(index)
        if dup_list[index-1]==0:
            dup_list[index-1]=1
        else:
            index=input('Choose an unchosen index between 1 and 9\n')
            index=int(index)
        ml[index-1]=ch1
    else:
        index=input('Player 2: Choose an index between 1 and 9\n')
        if index.isdigit()==False:
            index=input('Enter a number between 1 and 9\n')
        if int(index) not in range(1,10):
            index=input('The index must be between 1 and 9\n')
        index=int(index)
        if dup_list[index-1]==0:
            dup_list[index-1]=1
        else:
            index=input('Choose an unchosen index between 1 and 9\n')
            index=int(index)
        ml[index-1]=ch2
            
    disp(ml)
    if check(ml,ch1)==True:
        print('Congratulations to player 1!\n')
        break
        
    
    if check(ml,ch2)==True:
        print('Congratulations to player 2!\n')
        break
    i=i+1;
if i==10:
    print('Draw!\n')
 
        


    
    
    
    
