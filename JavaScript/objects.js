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

// same thing by using new keyword
function User(name, score) {
  this.name = name;
  this.score = score;
}

// since, functions in JS are objects as well
User.prototype.increment = function () {
  this.score++;
};

User.prototype.print = function () {
  console.log(this.name + ", your score is: ", this.score);
};

const user3 = new User("Shreyanss", 90);
user3.increment();
user3.print();

function isSame(obj1, obj2) {
  prop1 = Object.getOwnPropertyNames(obj1);
  prop2 = Object.getOwnPropertyNames(obj2);
  console.log(prop1, prop2);
  if (prop1.length !== prop2.length) {
    console.log("No match");
    return false;
  }
  
}

isSame({ a: 23 }, { a: 45 });
