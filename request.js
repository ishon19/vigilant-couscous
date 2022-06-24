const https = require("https");

const apiStr = "https://coderbyte.com/api/challenges/json/age-counting";

https.get(apiStr, async (resp) => {
  let buffer = [];
  let str = "";
  for await (chunk of resp) {
    buffer.push(chunk);
    str += chunk;
  }

  const data = Buffer.concat(buffer).toString();
  const json = JSON.parse(str);
  //console.log(json);
  const dataList = json.data.split(",");
  const ageList = [];
  for (let i = 0; i < dataList.length; i++) {
    if (i % 2 !== 0) {
      ageList.push(Number(dataList[i].split("=")[1]));
    }
  }
  console.log(ageList.filter((age) => age >= 50).length);
});
