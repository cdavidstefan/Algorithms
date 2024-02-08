// Coming up tomorrow.































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
        this.tail.next = newNode;
        newNode.previous = this.tail;
        this.tail = newNode;
        this.length++;
        return this;
    }

    prepend(value) {
        const newNode = new Node(value);
        newNode.next = this.head;
        this.head.previous = newNode;
        this.head = newNode;
        this.length++;
        return this;
    }

    insert(index, value) {
        if (index > this.length) {
            console.log(`The specified index (${index}) is out of range. I did append the value (${value}) to the end of the list.`)
            return this.append(value);
        }

        const newNode = new Node(value);
        const temporaryTail = this.traverseToIndex(index - 1);

        // * --> * --> *
        //    *

        let follower = temporaryTail.next;
        temporaryTail.next = newNode;
        newNode.previous = temporaryTail;
        newNode.next = follower;
        follower.previous = newNode;
        this.length++;
        return this;
    }

    remove(index) {
        if (index > this.length) {
            console.log(`The index (${index}) is out of range.`);
        }

        const temporaryTail = this.traverseToIndex(index - 1);
        let unwantedNode = temporaryTail.next;
        temporaryTail.next = unwantedNode.next;
        this.length--;
        return this;
    }

    reverse() {
        if (!this.head.next) {
            console.log("Nothing to sort. you only have one item.")
        }

        let first = this.head;
        this.tail = first;
        let second = first.next;
        while (second) {
            let temp = second.next;
            second.next = first;
            first = second;
            second = temp;
        }
        this.head.next = null;
        this.head = first;
    }

    traverseToIndex(index) {
        let counter = 0;
        let currentNode = this.head;
        while ( index >= counter) {
            currentNode = currentNode.next;
            counter++;
        }
        return currentNode;
    }

    printList() {
        let printedList = [];
        let currentNode = this.head;
        while (currentNode !== null) {
            printedList.push(currentNode.value);
            currentNode = currentNode.next;
        }
        return printedList;
    }

}



const myLinkedList = new DoublyLinkedList(5);

myLinkedList.append(13);
myLinkedList.append(17);
myLinkedList.prepend(9);
myLinkedList.prepend(22);
myLinkedList.insert(99, 1);
myLinkedList.insert(25, 99);
myLinkedList.insert(2,75);
myLinkedList.insert(1,7);
console.log(myLinkedList.printList());
myLinkedList.remove(1);
myLinkedList.remove(4);
console.log(myLinkedList);
console.log(myLinkedList.printList());
console.log(myLinkedList.traverseToIndex(3));
console.log(myLinkedList.printList());

myLinkedList.reverse();
console.log(myLinkedList.printList());








