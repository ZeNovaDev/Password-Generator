#Password generator
#a string variable to store characters
#ask user what they want to involve( alphabets, numbers, special characters )
#let choose multiple options
#random alplabet or special characters from tuples
#let user choose the length of characters (1-20)
import random
print("Welcome to password generator! ")
Alphabets_uppercase =["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"] 
Alphabet_lowercase=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] 
Special_characters=["@","#","$","*","&","+","_"] 
Characters =["au" , "n" , "al" , "s"] 
password=""
  
    
    
user_choice = input("Do you want to generate random password? (Y/N):  ").upper()
len_count=int(input("How much Characters? ")) 
if user_choice == "Y":
  if user_choice=="Y":
    count = 1
    while count <= len_count:
      count+=1
      ch = random.choice(Characters)
      if ch == "au":
        AU=str(random.choice(Alphabets_uppercase)) 
        password += AU
  
      elif ch =="al":
        AL=random.choice(Alphabet_lowercase)
        password += AL

      elif ch=="n": 
        NUM=str(random.randint(1,9))
        password+=NUM
      elif ch=="s":
        SC=str(random.choice(Special_characters)) 
        password += SC   

elif user_choice == "N":
  print("Bye")
else:
  print("invalid choice! ")

print(password)


