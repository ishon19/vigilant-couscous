// find k distant indices from a given index
function findKDistantIndices(nums: number[], key: number, k: number): number[] {
  const keyIndices: number[] = [];
  const finalIndices: number[] = [];

  nums.forEach((e, i) => {
    if (e === key && !keyIndices.includes(i)) {
      keyIndices.push(i);
    }
  });
  // console.log(keyIndices);
  nums.forEach((_e, i) => {
    keyIndices.forEach((e2) => {
      if (
        Math.abs(i - e2) <= k &&
        nums[e2] === key &&
        !finalIndices.includes(i)
      ) {
        finalIndices.push(i);
      }
    });
  });

  return finalIndices.sort((a, b) => a - b);
}

console.log(findKDistantIndices([3, 4, 9, 1, 3, 9, 5], 9, 1));
