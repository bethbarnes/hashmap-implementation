function Node(val){
  this.val = val
  this.next = null
}

class LinkedList {
  constructor(){
    this.head = null
  }
  addNode(val){
    this.head === null ? this.head = new Node(val) : console.log('collision!')
  }
}
