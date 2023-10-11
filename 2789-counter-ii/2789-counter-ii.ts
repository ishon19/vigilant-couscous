type ReturnObj = {
    increment: () => number,
    decrement: () => number,
    reset: () => number,
}

function createCounter(init: number): ReturnObj {
    const initialVal = init;
	return {
        increment: () => {
            return ++init;
        },
        decrement: () => {
            return --init; 
        },
        reset: () => {
            init = initialVal;
            return initialVal;
        }
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */