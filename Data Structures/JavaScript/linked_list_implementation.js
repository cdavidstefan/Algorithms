//# Garbage collection in js. - memory is/python managed automatically

//obj1 = { a: true};
//obj2 = obj1;
//obj1.a = "booooo";
//delete obj1;
//
//console.log('2', obj2)

// Linked list implementation in JS

// 10-->5-->16

class Node {
    constructor(value) {
        this.previous = null;
        this.value = value;
        this.next = null;
    }
}

class DoublyLinkedList {
    constructor(value) {
        this.head = new Node(value);
        this.tail = this.head;
        this.length = 1;
    }


    append(value) {
        const newNode = new Node(value);
        newNode.previous = this.tail;
        this.tail.next = newNode;
        this.tail = newNode;
        this.length++;
        return this;
    }


    prepend(value) {
        const newNode = new Node(value);
        this.head.previous = newNode;
        newNode.next = this.head;
        this.head = newNode;
        this.length++;
        return this;
    }


    printList() {
        const array = [];
        let currentNode = this.head
        while (currentNode !== null) {
            array.push(currentNode.value);
            currentNode = currentNode.next;
        }
        return array;
    }


    insert(index, value) {
        // Check parameters
        if (index >= this.length) {
            console.log('The inserted index is out of range. I did append the value to the end of the linked list.')
            return this.append(value);
        }
        const newNode = new Node(value);
        const leader = this.traverseToIndex(index - 1)

        // * --> *
        //    *

        const follower = leader.next;
        leader.next = newNode;
        newNode.previous = leader;
        newNode.next = follower;
        follower.previous = newNode;
        this.length++;
        return this.printList();
    }


    traverseToIndex(index) {
        // Check parameters again (to see if the index is a legitimate value)
        let counter = 0;
        let currentNode = this.head;
        while (counter !== index) {
            currentNode = currentNode.next;
            counter++;
        }
        return currentNode;
    }


    remove(index) {
    // Check parameters index > 0 ? .......
    // Because of garbage collection in JS,
    // once we remove the pointer to the element, it gets deleted

        if (index >= this.length) {
            console.log("The index of the node you are trying to delete is out of range.")
        }

        const temporaryTail = this.traverseToIndex(index - 1);
        unwantedNode = temporaryTail.next;
        temporaryTail.next = unwantedNode.next;
        this.length--;
        return this.printList();
    }

    reverse() {
        if (!this.head.next) {
            return this;
        }

        let first = this.head;
        this.tail = this.head;
        let second = first.next;
        while(second) {
            const temp = second.next;
            second.next = first;
            first = second;
            second = temp;
        }
        this.head.next = null;
        this.head = first;
        return this;
    }
}

const myLinkedList = new DoublyLinkedList(10);

myLinkedList.append(5);
myLinkedList.append(16);
myLinkedList.prepend(1);
myLinkedList.insert(2, 9000);
myLinkedList.insert(222, 12345);
myLinkedList.insert(4, 50);
console.log(myLinkedList.printList());
console.log(myLinkedList.reverse().printList());








//class Node {
//    constructor(value) {
//        this.previous = null;
//        this.value = value;
//        this.next = null;
//    }
//}
//
//class DoublyLinkedList {
//    constructor(value) {
//        this.head = new Node(value);
//        this.tail = this.head;
//        this.length = 1;
//    }
//
//    append(value) {
//        const newNode = new Node(value);
//        this.tail.next = newNode;
//        newNode.previous = this.tail;
//        this.tail = newNode;
//        this.length++;
//        return this;
//    }
//
//    prepend(value) {
//        const newNode = new Node(value);
//        newNode.next = this.head;
//        this.head.previous = newNode;
//        this.head = newNode;
//        this.length++;
//        return this;
//    }
//
//    insert(index, value) {
//        if (index > this.length) {
//            console.log(`The specified index (${index}) is out of range. I did append the value (${value}) to the end of the list.`)
//            return this.append(value);
//        }
//
//        const newNode = new Node(value);
//        const temporaryTail = this.traverseToIndex(index - 1);
//
//        // * --> * --> *
//        //    *
//
//        let follower = temporaryTail.next;
//        temporaryTail.next = newNode;
//        newNode.previous = temporaryTail;
//        newNode.next = follower;
//        follower.previous = newNode;
//        this.length++;
//        return this;
//    }
//
//    remove(index) {
//        if (index > this.length) {
//            console.log(`The index (${index}) is out of range.`);
//        }
//
//        const temporaryTail = this.traverseToIndex(index - 1);
//        let unwantedNode = temporaryTail.next;
//        temporaryTail.next = unwantedNode.next;
//        this.length--;
//        return this;
//    }
//
//    reverse() {
//        if (!this.head.next) {
//            console.log("Nothing to sort. you only have one item.")
//        }
//
//        let first = this.head;
//        this.tail = first;
//        let second = first.next;
//        while (second) {
//            let temp = second.next;
//            second.next = first;
//            first = second;
//            second = temp;
//        }
//        this.head.next = null;
//        this.head = first;
//    }
//
//    traverseToIndex(index) {
//        let counter = 0;
//        let currentNode = this.head;
//        while ( index >= counter) {
//            currentNode = currentNode.next;
//            counter++;
//        }
//        return currentNode;
//    }
//
//    printList() {
//        let printedList = [];
//        let currentNode = this.head;
//        while (currentNode !== null) {
//            printedList.push(currentNode.value);
//            currentNode = currentNode.next;
//        }
//        return printedList;
//    }
//
//}
//
//
//
//const myLinkedList = new DoublyLinkedList(5);
//
//myLinkedList.append(13);
//myLinkedList.append(17);
//myLinkedList.prepend(9);
//myLinkedList.prepend(22);
//myLinkedList.insert(99, 1);
//myLinkedList.insert(25, 99);
//myLinkedList.insert(2,75);
//myLinkedList.insert(1,7);
//console.log(myLinkedList.printList());
//myLinkedList.remove(1);
//myLinkedList.remove(4);
//console.log(myLinkedList);
//console.log(myLinkedList.printList());
//console.log(myLinkedList.traverseToIndex(3));
//console.log(myLinkedList.printList());
//
//myLinkedList.reverse();
//console.log(myLinkedList.printList());