(async function test() {
  const p1 = () =>
    new Promise((resolve, reject) => {
      console.log("here");
      resolve(4);
    });

  //console.log(p1());
  p1()
    .then(
      (res, err) =>
        new Promise((a, b) => {
          setTimeout(() => {
            a("timeout complete");
          }, 2000);
        })
    )
    .then((res) => console.log("next one", res));

  const p2 = async () =>
    new Promise((resolve, reject) => {
      console.log("here");
      resolve(4);
    });

  //console.log(p1());
  const res = await p2();
  console.log("res", res);

})();
