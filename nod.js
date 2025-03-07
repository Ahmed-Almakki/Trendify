// function sumTarget(arr, target) {

//     dict = {};
//     for (let i = 0; i <= arr.length; i++) {
//         const complement = target - arr[i];
//         console.log(dict);
//         if (dict.hasOwnProperty(complement)) {
//             return [dict[complement], i];
//         }
//         dict[arr[i]] = i;
//     }
//     return [];
// }
// console.log(sumTarget([11, 2, 7 ,15], 26));


class LinkedList{

    constructor(value) {
        this.head = {
            value,
            next: null
        };
        this.tail = this.head;
        this.length = 1;
    }

    append(value) {
        const node = {
            value,
            next: null
        };
        this.tail.next = node;
        this.tail = node;
        this.length++;
    }

    prepend(value) {
        const node = {
            value,
            next: null
        };
        node.next = this.head
        this.head = node;
        this.length++
    }

    insert(index, value) {
        if (index < 0 || index > this.length) {
            throw new Error("Index out of boundries");
        }
        if (index === this.length) {
            this.append(value);
            return;
        } else if (index === 0) {
            this.prepend(value);
            return;
        } else {
            const node = {
                value,
                next: null
            };
            let temp = this.head;
            let i = 1;
            while (i !== index) {
                temp = temp.next;
                i++;
            }
            node.next = temp.next;
            temp.next = node;
        }
        this.length++
    }

    printlist() {
        let current = this.head;
        let lst = '';
        while(current) {
            lst = lst + current.value;
            current = current.next;
            if (current !== null) {
                lst += '->';
            }
        }
        return lst;
    }

    reverse(node = this.head) {
        if (node === null) {
            return;
        }
        this.reverse(node.next)
        console.log(node.value)
    }

    remove(index) {
        if (index < 0 || index > this.length) {
            throw new Error("index out of boundries");
        }
        if (index === 0) {
            this.head = this.head.next;
            if (this.length === 1) {
                this.tail = null;
            }
        }
        else {
            let current = this.head;
            let count = 0;
            while (count === index - 1) {
                current = current.next;
                count++;
            }
            const nodTremove = current.next;
            current.next = nodTremove.next;
        }
        this.length--;
    }
}

const linked = new LinkedList(2);
// linked.prepend(1);
linked.append(5);
linked.append(4);
linked.append(3);
linked.insert(2, 10);
linked.insert(0, 100);
linked.insert(0, 1000);
linked.insert(5, 200)
linked.remove(2);
console.log(linked.printlist());
linked.insert(2, 10);
console.log(`----------------------------------\n${linked.printlist()}`)
console.log('-' * 10);
linked.reverse()




// class LinkedList {
//     constructor(value) {
//         this.head = {
//             value,
//             next: null
//         };
//         this.tail = this.head;
//         this.length = 1;
//     }

//     appeand(value) {
//         const node = {
//             value,
//             next: null
//         };
//         this.tail.next = node
//         this.tail = node;
//     }

//     printLinl() {
//         let curr = this.head;
//         let res = '';
//         while (curr !== null) {
//             // console.log(curr.value);
//             res += curr.value;
//             curr = curr.next;
//             if (curr) {
//                 res += '->';
//             }
//         }
//         return res;
//     }
// }

// const lst = new LinkedList(2);
// lst.appeand(4)
// lst.appeand(5)
// console.log(lst.printLinl());