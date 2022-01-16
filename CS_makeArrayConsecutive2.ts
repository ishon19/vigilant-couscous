function consecutive(statues: number[]): number {
  const sortedList = statues.sort((a, b) => a - b);
  console.log(sortedList);
  const diff = sortedList[sortedList.length - 1] - sortedList[0] + 1;
  return Math.abs(diff - statues.length);
}

console.log(consecutive([6, 2, 3, 8]));
