"""
Question 1:


In a normal hash table, a key is hashed then linear search is performed in the bucket where the key will be found if it exists in the hash table. A successful search terminates as soon as the key is found, on average half-way through the bucket, but an unsuccessful search requires that every item in the bucket be examined.


Donald Knuth proposed that instead of keeping keys in a bucket in random order they be kept in increasing order, so that a search can stop as soon as the search passes the value of the key. That means inserts take longer; you have to find the right place in the bucket to put the key instead of just putting it at the beginning of the bucket. But lookups are quicker, as an unsuccessful search can terminate half-way through the bucket, on average. This change also means that the data type of the hash table changes, as now the comparison function is less-than rather than equal-to.


Your task is to write a small library of ordered hash tables; you should provide lookup, insert and delete functions, at least.
"""

class OrderedHashTable: 
  
  def __init__(self):      
    self.arr = [] 
    self.ordered_hash = {}  
  

  def add(self, x): 
    if x in self.ordered_hash: 
      return
    s = len(self.arr) 
    self.arr.append(x) 
    self.ordered_hash[x] = s 

  def delete(self, x): 
    index = self.ordered_hash.get(x, None) 
    if index == None: 
        return

    del self.ordered_hash[x] 
    size = len(self.arr) 
    last = self.arr[size - 1] 
    #swapped elements here
    self.arr[index], self.arr[size - 1] = self.arr[size - 1], self.arr[index]  
    del self.arr[-1]  
    self.ordered_hash[last] = index 

  def search(self, x): 
    return self.ordered_hash.get(x, None) 
  
if __name__=="__main__": 
    oht = OrderedHashTable() 
    oht.add(20) 
    oht.add(10) 
    oht.add(99) 
    oht.add(30)
    oht.add(60) 
    print(oht.search(30)) 
    oht.delete(60) 
    oht.add(50) 
    print(oht.search(50)) 