import pickle

# save a json file as a pickle file
with open('data.pkl', 'wb') as f:
   pickle.dump("hello", f) # write it to the first line
   pickle.dump("world", f) # second
   pickle.dump([42,4242,{1:"hello"}], f) # different data types
   # while we interact with the file, the file pointer will move to the end of the file
   # so we need to move it back to the beginning of the file
   f.close()

with open('data.pkl', 'rb') as f:
    # we read the data line by line
    a = pickle.load(f)
    b = pickle.load(f)
    c = pickle.load(f)

print(a,b,c)
