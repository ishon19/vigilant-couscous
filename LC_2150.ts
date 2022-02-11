// Leetcode 2150 - find all lonely numbers

function findLonely(nums: number[]): number[] {
  const map: Record<number, number> = {};
  const ans: number[] = [];
  for (let i = 0; i < nums.length; i++) {
    if (map[nums[i]]) {
      map[nums[i]]++;
    } else {
      map[nums[i]] = 1;
    }
  }

  Object.keys(map).forEach((key) => {
    if (map[Number(key)] === 1) {
      if (!map[Number(key) + 1] && !map[Number(key) - 1]) {
        ans.push(Number(key));
      }
    }
  });

  return ans;
}

console.log(findLonely([10, 6, 5, 8]));
