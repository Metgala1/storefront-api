class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * capacity
        self.size = 0
    
    def hash(self, key):
        total = 0
        
        for letter in key:
            total += ord(letter)
        
        return total % self.capacity
    
    def insert(self, key, value):
        index = self.hash(key)
        
        if self.table[index] is None:
            self.table[index] = []
        
        bucket: list = self.table[index]
        
        for item in bucket:
            if item[0] == key:
                item[1] = value
                return
        
        bucket.append([key, value])
        self.size += 1
    
    def get(self, key):
        index = self.hash(key)
        
        if self.table[index] is None:
            return 
        
        bucket = self.table[index]
        
        for item in bucket:
            if item[0] == key:
                return item[1]
        
        return
    
    def remove(self,key):
        index = self.hash(key)
        
        if self.table[index] is None:
            raise ValueError("Invalid key")
        
        bucket: list = self.table[index]
        
        for i , item in enumerate(bucket):
            if item[0] == key:
                del bucket[i]
                self.size -= 1
                return True
        
        return False
    
    def has(self, key) -> bool:
        index = self.hash(key)
        
        if self.table[index] is None:
            return
        
        return True
    
    def display(self):
        for index, bucket in enumerate(self.table):
            if bucket is not None and len(bucket) > 0:
                print(f"Index {index}:")
                for item in bucket:
                    print(f"  {item[0]}: {item[1]}")
                print() 
            
            
    

new_hashTable = HashTable(10)

new_hashTable.insert("cat", 76)
new_hashTable.insert("tac", 56)
new_hashTable.insert("rat", 90)



print(new_hashTable.display())
        