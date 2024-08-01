function countSeniors(details: string[]): number {
   return details.map(detail => Number(detail.substring(detail.length-4, detail.length-2))).filter(age => age > 60).length
};