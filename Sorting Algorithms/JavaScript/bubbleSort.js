const numbers = [1,2,5,6,23,56,21,67,34,9]

function bubbleSort(array) {
    const length = array.length()
    for (let i = 0; i < length; i++) {
        for (let j = 0; j < length; j++) {
            if array[j] > array[j + 1] {
                // Swap numbers
                let cup3 = array[j]
                array[j] = array[j + 1]
                array[j + 1] = cup3
            }
        }
    }
}

bubbleSort(numbers);
console.log(numbers);