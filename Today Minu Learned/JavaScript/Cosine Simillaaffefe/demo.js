var similarity = require("string-cosine-similarity");

var string1 = "daum hwameon";
var string2 = "daum hwameo";

console.log(similarity(string1, string2)); // 0.9302605094190635
