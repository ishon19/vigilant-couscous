function topKFrequent(nums: number[], k: number): number[] {
  const numMap: Record<number, number> = {};
  const ans: number[] = [];
  nums.map((e) => {
    if (!numMap[e]) numMap[e] = 1;
    else numMap[e] += 1;
  });
  const sorted = Object.entries(numMap).sort((a, b) => b[1] - a[1]);
  // console.log("The sorted object list", sorted);
  for (let i = 0; i < k; i++) {
    ans.push(parseInt(sorted[i][0]));
  }
  // console.log("The answer", ans);
  return ans;
}

topKFrequent([6, 6, 6, 6, 3, 3, 3, 3, 3, 3, 3, 5], 2);
