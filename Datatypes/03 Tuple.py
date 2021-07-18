
t1 = ('Harshad', 'Gare', 1998, 23, 16)
t2 = (10,)   # Note
print("t1 = ", t1)
# ***********OPERATIONS**********
# indexing
print(t1[0], ' ', t1[2])

print("Concatenation : ", t1+t2)
print("Repetition : ", t2*3)

# Slicing
print("t1[0:2] : ", t1[0:2])
print("t1[-2 : -1] : ", t1[-2:-1])

# Tuple Nesting
t3 = t1, t2
print(t3)

# Attempt to update
# t2[1] = 'Python' #it will produce an error

# delete tuple
del t3
# print(t3) # it will produce an error

# ************* FUNCTIONS ************
t3 = (10, 20, 30)
print("\nt3 = ", t3)
print("max(t3) : ", max(t3))
print("min(t3) : ", min(t3))
print("len(t3) : ", len(t3))

data = [10, 20, 'harshad']
tup = tuple(data)
print("Convert Any Sequence into Tuple tuple(sequence) : ", tup)
