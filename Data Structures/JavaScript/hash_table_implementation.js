// Coming up tomorrow.

//let user = {
//    age: 27,
//    name: 'Pumba',
//    magic: true,
//    awesome: true,
//    scream: function() {
//        console.log('aaaaaaaaaaah!');
//    }
//}

//console.lof(user.age); // O(1)
//user.spell = "abracadabra"; // O(1)
//user.scream(); // O(1)

//const a = new Map();
//const b = new Set();




class HashTable {
    constructor(size) {
        this.data = new Array(size);
    }

    _hash(key)= {
        let hash = 0;
        for (let i = 0; i < key.length; i++) {
            hash = (hash + key.charCodeAt(i) * i) % this.data.length
        }
        return hash;
    }

    set(key, value) {

    }

    get(key) {

    }
}

const myHashTable = new HashTable(50);
myHashTable.set('grapes', 10000);
myHashTable.get('grapes');