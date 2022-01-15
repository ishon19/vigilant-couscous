// Codesignal - shape area

function solution(n: number): number {
  const ans: number[] = [1];
  for (let i = 1; i < n; i++) {
    ans.push(ans[i - 1] + 4 * (i));
  }
  return ans[n - 1];
}

console.log(solution(4));
