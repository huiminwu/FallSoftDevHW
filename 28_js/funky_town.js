//MinZane -- Hui Min Wu, Zane Wang
//SoftDev1 pd8
//K28 -- Sequential Progression
//2018-12-18

var fibonacci = function(n) {
    if (n == 0) {
        return 0;
    } else if (n <= 2) {
        return 1;
    } else {
        return fibonacci(n-2) + fibonacci(n-1);
    };
};

var gcd = function(a, b) {
    if (a < b) {
        return gcd(b, a);
    } else if (b == 0) {
        return a;
    } else if (a == 0) {
        return 0;
    } else {
        return gcd(b, a % b);
    };
};

var arrayName = ["Hui Min", "Zane", "Johnny"];

var randomStudent = function() {
    return arrayName[Math.floor(Math.random() * arrayName.length)];
}
