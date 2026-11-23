class HashTable {
  constructor(capacity = 10) {
    this.capacity = capacity;
    this.table = Array(capacity);
    this.size = 0;
  }

  hash(key) {
    let total = 0;

    for (let i = 0; i < key.length; i++) {
      total += key.charCodeAt(i);
    }

    return total % this.capacity;
  }

  insert(key, value) {
    const index = this.hash(key);

    if (!this.table[index]) {
      this.table[index] = [];
    }
    const bucket = this.table[index];

    for (let i = 0; i < bucket.length; i++) {
      if (bucket[i][0] === key) {
        bucket[i][1] = value;
        return;
      }
    }

    bucket.push([key, value]);
    this.size += 1;
  }

  get(key) {
    const index = this.hash(key);
    const bucket = this.table[index];

    if (!bucket) return undefined;

    for (let i = 0; i < bucket.length; i++) {
      if (bucket[i][0] === key) {
        return bucket[i][1];
      }
    }

    return undefined;
  }

  remove(key) {
    const index = this.hash(key);
    const bucket = this.table[index];

    if (!bucket) return undefined;

    for (let i = 0; i < bucket.length; i++) {
      if (bucket[i][0] === key) {
        bucket.splice(i, 1);
        this.size -= 1;

        if (bucket.length === 0) {
          this.table[index] = undefined;
        }
      }

      return true;
    }

    return false;
  }

  has(key) {
    const index = this.hash(key);
    const bucket = this.table[index];

    if (!bucket) return false;

    for (let i = 0; i < bucket.length; i++) {
      if (bucket[i][0] === key) {
        return true;
      }
    }

    return false;
  }

  display() {
    for (let i = 0; i < this.capacity; i++) {
      console.log(i, this.table[i]);
    }
  }
}

const users = new HashTable(10);

users.insert("apple", 100);
users.insert("banana", 200);
users.insert("orange", 300);

users.insert("apple", 150);

console.log(users.get("apple")); // 150
console.log(users.has("banana")); // true

users.remove("orange");

console.log(users.size); // 2
users.display();

class HashMap {
  constructor(capacity) {
    this.capacity = capacity
    this.table = []
    this.size = 0
  }

  hash(key) {
    const total = 0

    for(let i = 0; i < key.length; i++) {
        total += key.charCodeAt(i)
    }

    return total % this.capacity
  }
}
