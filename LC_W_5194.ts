// find minimum number of moves to make the number equal to target

function minMoves(target: number, maxDoubles: number): number {
  let moves: number = 0;
  let start: number = 1;
  while (start < target && maxDoubles > 0) {
    start *= 2;
    moves++;
    maxDoubles--;
  }
  if (start != target) {
    if (start < target) {
      return moves + (target - start);
    } else {
        return moves - (start - target);
    }
  }
  return moves;
}

console.log(minMoves(19, 2));
