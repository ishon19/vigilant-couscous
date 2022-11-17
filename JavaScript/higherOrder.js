function higher(nums, callback) {
  for (let index = 0; index < nums.length; index++) {
    callback(nums[index]);
  }
}

function hello(num) {
    console.log(num * num);
}

higher([1,2], hello);