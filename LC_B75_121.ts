function maxProfit(prices: number[]): number {
  let profit = 0;
  let minPrice = prices[0];

  for (let i = 1; i < prices.length; i++) {
    if (prices[i] < minPrice) {
      minPrice = prices[i];
    } else {
      profit = Math.max(profit, prices[i] - minPrice);
    }
  }

  return profit;
}


console.log(maxProfit([7, 1, 5, 3, 6, 4]));
