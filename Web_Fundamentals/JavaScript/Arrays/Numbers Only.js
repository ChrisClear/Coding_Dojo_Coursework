function numbersOnly(arr) {
  var placeHolder = [];
  for(var i = 0; i < arr.length; i++) {
    if (typeof arr[i] === "number"){
      placeHolder.push(arr[i]);
    }
  }
  return placeHolder;
}
var tests = numbersOnly([1, "apple", -3, "orange", 0.5]);
console.log(tests);