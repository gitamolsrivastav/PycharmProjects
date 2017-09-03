import pickle

x = pickle.dumps(['a','b',1,2,3,4,5.6])

var = pickle.loads(x)

print(var)
