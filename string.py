mystr="hello sir"
# for using particular letter
print(4*mystr[3])
#for using particular letter
#it will print string form 0 to 3=hel but excuding the second l.
print(mystr[0:3])#o/p=l
#for skiping the characters
print(mystr[0:5:2])
#sting length function
print(len(mystr))
#negative index
print(mystr[-10:-6])
#string functions
#str.isalnum() is for cheacking the alpha numaric number
str1="rajacooco"
print(mystr.isalnum())#true if mystr=hellosir(without spaces)
print(str1.isalnum())#false if srt1=raja cool
#str.endswith(our string to be cheacing)
print(mystr.endswith("sir"))
#for counting the letter or specfic string
print(str1.count("co"))
#for making the first letter to be capital of a string
print(str1.capitalize())
#for find the specific word form the string
print(str1.find("co"))
#for replacing a particular word
print(mystr.replace("sir","ma'am"))
print(len(str1))

while(n>=100 and n<=500):

    if(n==251):
        print("Exactly right")
        break

else:
    print("Oops! wrong, guess again")


