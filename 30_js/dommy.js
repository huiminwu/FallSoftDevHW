/*
Team MinZane -- Hui Min Wu and Zane Wang
SoftDev1 pd8
K30 -- Sequential Progression III: Season of the Witch
2018-12-20
*/

var changeHeading = function(e) {
    var h = document.getElementById("h");
    h.innerHTML = e;
};


var removeItem = function(e) {
    this.remove();
};

var lis = document.getElementsByTagName("li");

for (var i = 0; i < lis.length; i++) {
    lis[i].setAttribute('val', "item " + i);
    lis[i].addEventListener('mouseover',
			    function() {
				changeHeading(this.getAttribute("val"));
			    });
    lis[i].addEventListener('mouseout',
			    function() {
				changeHeading("Hello World!");
			    });
    lis[i].addEventListener('click', removeItem);
}

var addItem = function(e) {
    var list = document.getElementById( "thelist");
    var item = document.createElement("li");
    item.innerHTML = "WORD";
    item.setAttribute('val', "WORD");
    item.setAttribute('class', 'nofib');
    list.appendChild(item);
    console.log(item);
    let liss = document.getElementsByClassName("nofib");
    for (let i = 0; i < liss.length; i++) {
        liss[i].addEventListener('mouseover',
                    function() {
                    changeHeading(this.getAttribute("val"));
                    });
        liss[i].addEventListener('mouseout',
                    function() {
                    changeHeading("Hello World!");
                    });
        liss[i].addEventListener('click', removeItem);
    }
}

var button = document.getElementById("b");
button.addEventListener( 'click', addItem);

var fib = function(n) {
    if (n < 2) {
	return 1;
    }
    else {
	return fib(n - 1) + fib(n - 2);
    }
};

var addFib = function(e) {
    console.log(e);
    var fiblist = document.getElementById("fiblist");
    var item = document.createElement("li");
    var len = fiblist.getElementsByTagName("li").length;
    item.innerHTML = fib(len);
    fiblist.appendChild(item);
};

var addFib2 = function(e) {
    console.log(e);
    var fiblist = document.getElementById("fiblist");
    var fibitem = fiblist.getElementsByTagName("li");
    var item = document.createElement("li");
    if (fibitem.length < 2) {
	item.innerHTML = 1;
    }
    else {
	var second = parseInt(fibitem[fibitem.length - 1].innerHTML, 10);
	var first = parseInt(fibitem[fibitem.length - 2].innerHTML, 10);
	item.innerHTML = first + second;
    }
    fiblist.appendChild(item);
};

var fb = document.getElementById("fb");
fb.addEventListener( "click", addFib2);

