function subtractProductAndSum(n: number): number {
    let sum = 0, prod = 1;  
    String(n).split('').map(e => {sum+=Number(e); prod *=Number(e)});  
    return prod - sum;
  };