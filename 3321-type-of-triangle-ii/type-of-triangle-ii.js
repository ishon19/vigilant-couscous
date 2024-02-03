/**
 * @param {number[]} nums
 * @return {string}
 */
var triangleType = function(nums) {
    const a = nums[0];
    const b = nums[1];
    const c = nums[2];
    if(a+b <= c || b+c <= a || a+c <= b) return "none";
    return new Set(nums).size == 1? "equilateral" : (new Set(nums).size == 2 ? "isosceles": "scalene")
};