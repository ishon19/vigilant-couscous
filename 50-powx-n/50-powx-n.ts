function myPow(x: number, n: number): number {
  const helper = (x,n) => {
      if(n==0){
          return 1
      }
      let half = helper(x,Math.floor(n/2))
      if(n%2==0) return half * half
      return half * half * x
  }
  x = n<0?1/x:x
  n = n<0?-n:n
  return helper(x,n)
};