
d1 = {1: 34, 2: 37, 's1': 5, 'lang': 'python',  (1, 2, 3): 'harsh', 50: [10, 20], 2: 500}
print("d1 :- ", d1)
print("d1['s1'] :- ", d1['s1'])
print("d1[(1, 2, 3)] :- ", d1[(1, 2, 3)])
print("d1[50][0] :- ", d1[50][0])
print("d1[2] :- ", d1[2])  # Return Last item When key is Duplicated

d2 = {}  # Empty Dictionary
print("Empty Dictionary :- ", d2)

d1['s1'] = 100  # Updating Value
print("After Updating :- ", d1)

del d1[2]
print("After Deleting d1[2]", d1)
# ************* FUNCTIONS **************
print("Length of d1 :- ", len(d1))
print("Dictionary Convert into String str(d1) :- " + str(d1))

# ************** METHODS ****************
d2 = d1.copy()
print("d2 :- ", d2)
print("Only Keys d1.key() :- ", d1.keys())
print("Return All items(key,value) d1.items() :- ", d1.items())
print("d1.get(1, hi) :- ", d1.get(1, 'hi'))
print("d1.get(2, hi) :- ", d1.get(2, 'hi'))
print("return removed item d1.pop(50) :- ", d1.pop(50))
print(d1)
print("removed & return last item d1.popitem() :- ", d1.popitem())
print(d1)

d3 = {}
tup = ['name', 'rollno']
d3 = d3.fromkeys(tup)
print(d3)

d3 = d3.fromkeys(tup, 10)
print(d3)
