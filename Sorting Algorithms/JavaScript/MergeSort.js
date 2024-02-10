// Merge sort algorithm is JavaScript
// Out-of-place algorithm - requires growing amount of memory to process the input into output.
// Stable - Two elements with equal values will appear in the same order in the sorted output as they appear in the unsorted output.

function mergeSort(arr) {
    // Best case.
    if (arr.length <= 1) return arr;

    let mid = Math.floor(arr.length / 2)

    let left = arr.slice(0, mid)
    let right = arr.slice(mid)

    left = mergeSort(left);
    right = mergeSort(right);

    return merge(left, right);
}

function merge(left, right) {
    // Create an empty array:
    sortedArray = [];
    while (left.length && right.length) {
        // Insert the smallest item in the array
        if (left[0] < right[0]) {
            sortedArray.push(left.shift())
        } else {
            sortedArray.push(right.shift())
        }
    }

    return [...sortedArray, ...left, ...right]
}

array = [40,1,5,28,17,34,2]
console.log(mergeSort(array));


