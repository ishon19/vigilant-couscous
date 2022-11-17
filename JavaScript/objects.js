function createUser(name, score) {
  // const newUser = {};
  const newUser = Object.create(functionStore);
  newUser.name = name;
  newUser.score = score;
  return newUser;
}

const functionStore = {
  // Note: Arrow functions won't work here as they handle `this` differently
  increment: function () {
    this.score++;
  },
  print: function () {
    console.log(this.name + ", your score is: ", this.score);
  },
};

const user1 = createUser("shreyans", 1);
const user2 = createUser("test", 12);
user1.increment();
user1.print();
user2.print();
