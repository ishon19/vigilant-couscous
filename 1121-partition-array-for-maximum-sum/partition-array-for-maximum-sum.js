/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
var maxSumAfterPartitioning = function(arr, k) {
    const memo = {};

    const helper = (index) => {
        if (index in memo) {
            return memo[index];
        }

        if(index >= arr.length) {
            return 0
        }

        let subarrMax = 0
        let subArrVal = 0

        for (let i = index; i<Math.min(arr.length, index + k); i++) {
            subarrMax = Math.max(subarrMax, arr[i]);
            subArrVal = Math.max(subArrVal, subarrMax * (i - index + 1) + helper(i + 1));
        }

        memo[index] = subArrVal;
        return memo[index];
    }

    return helper(0);
};