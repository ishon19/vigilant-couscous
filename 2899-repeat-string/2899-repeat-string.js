/**
 * @param {number} times
 * @return {string}
 */
String.prototype.replicate = function(times) {
    let str = "";
    while(times--) {
        str += this.valueOf()
    }

    return str
}