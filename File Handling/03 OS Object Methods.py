
import os

# os.rename("demo.txt", "try.txt")
# os.remove("try.txt")
os.mkdir("harsh")

cw = os.getcwd()
print(cw)
os.chdir("harsh")
cw = os.getcwd()
print(cw)
fo = open("demo.exe", "w")
fo.close()
os.remove("demo.exe")
os.chdir("../")
cw = os.getcwd()
print(cw)
os.rmdir("harsh")

