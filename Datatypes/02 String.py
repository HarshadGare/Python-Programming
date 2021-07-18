str1 = "harshad"
str2 = "web Developer"

print("str1: "+str1)
print("str2: "+str2)

# *********** STRING OPERATION ************
print("Concatenated String : "+str1+str2)

print("Repetation of String: "+(str1 * 2))

print("String Indexing str1[1]: "+str1[1])
print("String Indexing str1[-1]: "+str1[-1])

print("String Slicing str1[2:5]: "+str1[2:5])
print("String Slicing str1[2:-1]: "+str1[2:-1])
print("String Slicing str1[5:]: "+str1[5:])
print("String Slicing str1[:3]: "+str1[:3])
print("String Slicing str1[-2:]: "+str1[-2:])

# ************** ESCAPE CHARACTER **************
string = "Hi, I Am Harshad.           I Am Learning Python For Web Development"
print(string)

escape_char = "Hi, I Am Harshad.          \b I Am \t Learning Python \n For Web Development"
print(escape_char)

# *********** FORMAT SPECIFIER ***********
# s , c , i , d , u , f , o , x or X , e or E
print(" Hi I Am %s Gare" % "Harshad")
print(" %c is Character " % 'c')
print("Name: %s \t Mob No. : %i" % ('harshad', 9665289181))

# *********** STRING FUNCTIONS ************

print("Str1 Length :", len(str1))
print("max (str1) : "+max(str1))
print("min (str1) : "+min(str1))

# *********** STRING METHODS ************

s1 = "i am learning python for Web Development"
s2 = "     I am learning python for stand alon application"
print(s1)
print(s2)

print("s1.count('e',0,len(s1) : ", s1.count('e', 0, len(s1)))
print("s1.capitalize() : "+s1.capitalize())
print("s1.title() : "+s1.title())
print("s2.lstrip() : "+s2.lstrip())
print("s2.rstrip() : "+s2.rstrip())
print("s2.strip() : "+s2.strip())
print("s1.index('e') : ", s1.index('e'))
print("s1.index('e',8,40) : ", s1.index('e', 8, 40))
print("s1.find('earn') : ", s1.find('earn'))
print("s1.find('earn',7,50) : ", s1.find('earn', 7, 50))     # Not Found
print("s1.replace('e','THE') : "+s1.replace('e', 'THE'))
print("s1.replace('e','THE',2) : "+s1.replace('e', 'THE', 2))
print("s1.split() : ", s1.split())
print("s1.split('e') : ", s1.split('e'))
print("s1.split('e',2) : ", s1.split('e', 2))

print("'python'.isalnum() : ", 'python'.isalnum())
print("'python '.isalnum() : ", 'python '.isalnum())
print("'python'.isalpha() : ", 'python'.isalpha())
print("'python123'.isalpha() : ", 'python123'.isalpha())
print("'123'.isdigit() : ", '123'.isdigit())
print("'123ab'.isdigit() : ", '123ab'.isdigit())
print("'python'.islower() : ", 'python'.islower())
print("'Python'.islower() : ", 'Python'.islower())
print("'PYTHON'.isupper() : ", 'PYTHON'.isupper())
print("'PYThON'.isupper() : ", 'PYThON'.isupper())
print("'   '.isspace() : ", '   '.isspace())
print("'  123'.isspace() : ", '  123'.isspace())
print("'This Is String'.istitle() : ", 'This Is String'.istitle())
print("'This is String'.istitle() : ", 'This is String'.istitle())
