let arr = [23, 34, 43, 2, 32, 54, 323];
const target = 43;



function linearSearch(arr, target) {

    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === target) {
            return `Target ${target} founded in index ${i}`
        }
    }
    return 'not found'
}

console.log(linearSearch(arr, target));