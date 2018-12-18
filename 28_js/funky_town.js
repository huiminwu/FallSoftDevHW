var fibonacci = function(n) {
    if (n == 0) {
        return 0;
    } else if (n <= 2) {
        return 1;
    } else {
        return fibonacci(n-2) + fibonacci(n-1);
    }
}

var gcd = function(a, b) {
    if (a < b) {
        return function(b,a);
    } else if (a == 0) {
        return a
