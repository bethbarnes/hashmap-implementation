//implement hashmap as array, hash function gives us array at which
// to store data, use Linked List to deal with collisions.

class HashMap {
  constructor(){
    this.hashLength = 50;
    this.hashArr = new Array(50)
  }

  addToHash(val){
    let hash = this.hash(val)
    console.log('hash is: ', hash)
  }

//very simple hashing function, will replce
  hash(val){
    return val.charCodeAt(0)%this.hashLength
  }

}


