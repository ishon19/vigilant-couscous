console.log("apple".charAt(0));
console.log("Youtube".substring(1));
console.log("Youtube".substring(1, 2));
console.log("a" < "b");
console.log("Shreyans".indexOf("pat"));

function toTitleCase(str) {
  return str.replace(/\w\S*/g, function (text) {
    return text.charAt(0).toUpperCase() + text.slice(1).toLowerCase();
  });
}

console.log(toTitleCase("hello world how is it going?"));
