//implement hashmap as array, hash function gives us array at which
// to store data, use Linked List to deal with collisions.

class HashNode{
  constructor(key, val){
    this.val = val
    this.key = key
  }
}

class HashMap {
  constructor(){
    this.hashLength = 50;
    this.hashArr = new Array(50)
  }

  addToHash(key,val){
    let hash = this.hash(key)
    if (this.hashArr[hash] === undefined) {
      this.hashArr[hash] = new LinkedList()
      this.hashArr[hash].addLLNode(key, val)
    }else {
      this.hashArr[hash].addLLNode(key, val)
    }
  }

  hash(val){
    return val.charCodeAt(0)%this.hashLength
  }
}


