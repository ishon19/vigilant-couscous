/**
 * @param {number[]} target
 * @param {number} n
 * @return {string[]}
 */
var buildArray = function(target, n) {
  const res = [];
  const stack = [];

    const checkIfArraysAreEqual = (arr1, arr2) => {
    if (arr1.length !== arr2.length) return false;

    for (let i = 0; i < arr1.length; i++) {
      if (arr1[i] !== arr2[i]) return false;
    }

    return true;
  };

  for (let i = 1; i < n + 1; i++) {
    if (checkIfArraysAreEqual(target, stack)) {
      break;
    }

    if (target.includes(i)) {
      // repeatedly pop elements which do not exist in target
      while (stack.length && !target.includes(stack[stack.length - 1])) {
        stack.pop();
        res.push('Pop');
      }

      // push the current element
      stack.push(i);
      res.push('Push');
    } else {
      stack.push(i);
      res.push('Push');
    }
  }

  return res;
};