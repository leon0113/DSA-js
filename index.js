function singleNumber(nums) {
    let arr = nums.sort((a, b) => a - b);
    // console.log(arr);
    for (let i = 0; i <= nums.length - 1; i += 2) {
        // console.log(i);
        if (arr[i] !== arr[i + 1]) {
            return arr[i];
        }
    }

    return arr[arr.length - 1];
};

const result = singleNumber([4, 1, 2, 1, 2, 4, 5, 2])

console.log(result);