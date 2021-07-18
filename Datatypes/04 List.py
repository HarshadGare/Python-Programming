
# *******OPERATIONS ON LIST ************
l1 = [1, 2, 'harshad', 'python', 10]
l2 = [1, 4, 20, 'gare', 'web']
print("l1:- ", l1)
print("l2:- ", l2)
print("concatenation l1+l1 :- ", l1+l2)
print("Repetition l1*2 :- ", l1*2)
print("Indexing l1[3]:-", l1[3])
print("Slicing l1[1:3] :- ", l1[1:3])
l1[4] = 50
print("Updating l1[4] :-", l1[4])
del l1[4]
print("l1:- ", l1)

# ******* FUNCTIONS ************
print("len(l1) :- ", len(l1))
print("min([12, 2323, 34, 454]) :- ", min([12, 2323, 34, 454]))
print("max([12, 2323, 34, 454]) :- ", max([12, 2323, 34, 454]))
d = [3, 'hp', 20]
print("convert tuple into list list(d)", list(d))

# ******* METHODS ************
l1.append('harshad')
print("After Appending l1.append('kida') :- ", l1)
print("l1.count('harshad') :- ", l1.count('harshad'))
l1.extend([100, 50])
print("After l1.extend([100, 50])", l1)
print("l1.index(100) :- ", l1.index(100))
l2.insert(1, 'PYTHON')
print("After Inserting l2.insert(1, 'PYTHON') :- ", l2)
print("l1.pop() :- ", l1.pop())
print("l1.pop(2) :- ", l1.pop(2))
print("l1 :- ", l1)
l1.remove(100)
print("After l1.remove(100) :- ", l1)
l1.reverse()
print("After Reverse list l1.reverse() :- ", l1)
l3 = [98, 23, 45, 99, 2]
print("l3 :- ", l3)
l3.sort()
print("After sorting l3.sort() :- ", l3)


