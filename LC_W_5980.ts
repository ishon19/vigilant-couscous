// Divide string in groups of n characters

function divideString(s: string, k: number, fill: string): string[] {
  const ans: string[] = [];
  let i = 0;
  while (i <= s.length) {
    if (s.substring(i, i + k).length > 0) ans.push(s.substring(i, i + k));
    i += k;
  }
  if (ans[ans.length - 1].length < k) {
    ans[ans.length - 1] = ans[ans.length - 1].padEnd(k, fill);
  }
  return ans;
}

console.log(divideString("abcdefghij", 3, "x"));
