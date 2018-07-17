import random
import time

print("*"*60)
print("*"*60)
print("*"*60)
print("*"*17,"Welcome to hangman game!","*"*17)
print("*"*60)
print("*"*60)
print(" "*20,"__________")
print(" "*20,"|"," "*6,"|")
print(" "*20,"|","","*","*  ","|")
print(" "*20,"|","","___","  |")
print(" "*20,"----------")
print("                         |")
print("                         |")
print("                         |")
print(" "*22,"------")
print(">>>>>>>>>>>> :-first level -: "
      "you have 10 chances<<<<<<<<<<<<")
movie_name=['3 idiot','harry potter','hulk','robot','dhoom','race','sonu k titu ki sweety','sholay','pacific rim','infinity war','krish','ironman',
            'rustom','airlift','dangal','pk',]              #assiigning movies name in movie_name
movie=random.choice(movie_name) 							#putting random movie name in movie
length=len(movie)             									    #'length of alphabet in movie word'
list_m=list(movie)
print("You got",length,"word movie.")
time.sleep(2)
#print("i give you power to chooose how much chances you need..")
#p=int(input("Enter Number of chance you want=>"))
time.sleep(1)
print("-----------------One more thing if there is space in movie then press space too----------------")


final=[]
for b in range(0,length):
    final.append('_')
for l in range(0,10):
    new=[]#giving 5 chances to guess
    input_alphabet=input("Enter the alphabet you guess=>")                     #take alphabet from user
    print("Wait we are matching your input . . . . . . . . . . . ")
    time.sleep(1)
    g=0

    for i in range(0,length):
          if input_alphabet==list_m[g]:
              new.append(input_alphabet)
              g=g+1
          else:
              g=g+1
              new.append("_")
    #print(new)

    for x in range(0,length):

        if final[x]=='_':
            final[x]=new[x]
    del new
    print(" ".join(final))
    print("\n")
    if(list(final)==list(movie)):
        print("you won")
        break
if(list(final)!=list(movie)):
    print("you loose")
print("********  Answer is=> ",movie,"********")
    # if final[0]==list_m[0]:
    #    print("you won")








































































































































































































































































































