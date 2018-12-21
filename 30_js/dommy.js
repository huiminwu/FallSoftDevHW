var changeHeading = function(e) {
    var h = document.getElementById("h");
    h.innerHTML = e;
};

var removeItem = function(e) {
    e.remove();
}

var lis = document.getElementsByTagName("li");

for(var i=0; i < lis.length; i++) {
    //need to set attribute because i will go to 8 and stay there since
    //it's the last value that meets the condition and this for loop
    //can't go backwards
    lis[i].setAttribute('val', i);
    lis[i].addEventListener('mouseover', 
        function() {
            changeHeading("Item " + this.getAttribute("val"));
        });
    lis[i].addEventListener('mouseout', 
        function() {
            changeHeading("Hello World!");
        });
    lis[i].addEventListener('click',
        function() {
            removeItem(this);
        });
}

var addItem = function(e) {
    var list = document.getElementById( "thelist");
    var item = document.createElement("li");
    item.innerHTML = "WORD";
    list.appendChild(item);
};

var button = document.getElementById("b");
button.addEventListener( 'click', addItem);

var fib = function(n) {
    if (n < 2) {
        return 1;
    } else {
        return fib(n-1) + fib(n-2);
    }
};

var addFib = function(e){
    console.log(e);
    var flist = document.getElementById("fiblist");
    var item = document.createElement("li");
    var len = flist.getElementsByTagName("li").length;
    item.innerHTML = fib(len);
    flist.appendChild(item);
};

var fb = document.getElementById("fb");
fb.addEventListener("click", addFib);
