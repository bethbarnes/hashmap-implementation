// Implementing singly linked list to store data at a each hash.
// If there is a collision, the new data will be added to the beginning of the linked list.

function Node(val){
  this.val = val
  this.next = null
}

class LinkedList {
  constructor(){
    this.head = null
  }

  addNode(val){
    let newNode = new Node(val)

    if (this.head === null) {
      this.head = newNode
    } else {
      let previousHead = this.head
      this.head = newNode
      newNode.next = previousHead
    }
  }
}
