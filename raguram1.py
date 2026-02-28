'''a="success"
ch='s'
print (a.count(ch))
print()'''
'''a="computer"
count=0
vovels= ['a','o','i','e','u']
found_vovels=[]
for ch in a :
    if ch in vovels:
      count+=1
      found_vovels.append(ch)

  print ("no of vovels" ,append)
  print("the vovels are",)'''
'''s="livewire"
print(s)
print(s[0])
print(s[:])
print(s[0:8])
print(s[4:8])
print(s[-1])
print(s[2])
print(s[::-1])
print(s[:8])
print(s[0:8])
print(s[0:4])
print(s[-6])
print(len (s))'''
#for reverse string in for loops
'''s="livewire"
t=""
n=len(s)
for i in range (n-1,-1,-1):
    t=t+s[i]
print (t)'''
'''s="tenet"
t=""
n=len(s)
for i in range (n-1,-1,-1):
    t=t+s[i]
if s==t:
    print("palindrome")
else:
    print("not palindrome")'''
# case changing
'''a="this is python"
print(a.lower())
print(a.upper())
print(a.capitalize())
print(a.title())
print(a.swapcase())'''
#testing
'''print("python".isalpha())
print("12345".isdigit())
print (" " .isspace())
print("python" .islower())
print ("python". isupper())
print("python language".istitle())
'''
n="@,$,^,*,*,*,@,:,;,;,;,:,python is the language"
symbols=0
upper=0
lower=0
space=0
number=0
for i in n:
    if (i.isupper):
        upper+=1
  elif (i.issymbol):
        symbol+=1
   elif (i.islower):
        lower+=1
elif(i.isspace):
        space+=1
elif (i.isnumber):
        number+=1
    print("uppercase":,upper)
    print("lowercase":,lower)
    print("symbols":,sumbols)
    print("numbers":,numbers)
    print("space":,space)
