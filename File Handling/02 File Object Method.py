
fo = open("demo.txt", 'w+')

fname = fo.name
print(fname)
fmode = fo.mode
print(fmode)
if fo.closed:
    print("File is Close")
else:
    print("File is Open")

fo.write("This is sample text \n")
pos = fo.tell()
print(pos)
txt = fo.read(50)
print(txt, " Before calling seek()")

fo.seek(0, 0)
txt = fo.read(15)
print(txt)

fo.seek(5, 0)     # 0 for Beginning
txt = fo.read(5)
print(txt)

fo.seek(0, 1)     # 1 for Current Position
txt = fo.read(5)
print(txt)

fo.seek(0, 2)     # 2 for End of File

fo.write("Write at End of File")
fo.seek(0, 0)
str2 = fo.read(50)
print(str2)

fdn = fo.fileno()
print("Integer File Descriptor No. : ", fdn)

fo.seek(0, 0)
print(fo.readline())
print(fo.__next__())

fo.seek(0, 0)
t = fo.truncate(1)
print(fo.readline())
print(t)

seq = [" This is 1st Line \n", "This is 2nd Line"]
fo.seek(0, 2)
fo.writelines(seq)
fo.seek(0, 0)
print(fo.__next__())
print(fo.__next__())


fo.close()
if fo.closed:
    print("File is Close")
else:
    print("File is Open")


