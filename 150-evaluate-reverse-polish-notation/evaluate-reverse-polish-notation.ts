function evalRPN(tokens: string[]): number {
    const ops = {
        '+': (a,b) => a + b,
        '-': (a,b) => a - b,
        '*': (a,b) => a * b,
        '/': (a,b) => Math.trunc(a / b) 
    }

    const stack = [];

    tokens.forEach(token => {
        if(token in ops) {
          const num2 = stack.pop();
          const num1 = stack.pop();
          stack.push(ops[token](num1, num2));
        } else {
            stack.push(Number(token))
        }
    })

    return stack.pop();
};