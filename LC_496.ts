// Leetcode 496. Next Greater Element I
function nextGreaterElement(nums1: number[], nums2: number[]): number[] {
    const ans = [];
     for(let i=0; i<nums1.length; i++) {
         let idx = nums2.findIndex(e=> e === nums1[i]);
         const subArray = nums2.slice(idx);
         const toPush = subArray.findIndex(e => e>nums1[i]); 
         ans.push(toPush === -1? -1: subArray[toPush]);
     }
    return ans;
};