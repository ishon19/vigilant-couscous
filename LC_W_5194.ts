// find minimum number of moves to make the number equal to target

function minMoves(target: number, maxDoubles: number): number {
  let moves: number = 0;
  while (target && maxDoubles) {
    moves += 1 + (target % 2);
    target = Math.floor(target / 2);
    maxDoubles--;
  }
  return moves + target - 1;
}

console.log(minMoves(19, 2));
