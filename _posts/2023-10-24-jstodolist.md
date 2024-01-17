---
toc: true
comments: false
layout: post
title: JS todo list
description: 
type: hacks
courses: { compsci: {week: 10} }
---
<html>
<head>
  <style>
    * {
        box-sizing: border-box;
    }

    ul {
        margin: 0;
        padding: 0;
    }

    ul li {
        cursor: pointer;
        position: relative;
        padding: 12px 8px 12px 40px;
        background: #eee;
        font-size: 18px;
        transition: 0.2s;

        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
    }

    ul li:nth-child(odd) {
        background: #f9f9f9;
    }

    ul li:hover {
        background: #ddd;
    }

    ul li.checked {
        background: #888;
        color: #fff;
        text-decoration: line-through;
    }
    ul li.checked::before {
        content: '';
        position: absolute;
        border-color: #fff;
        border-style: solid;
        border-width: 0 2px 2px 0;
        top: 10px;
        left: 16px;
        transform: rotate(45deg);
        height: 15px;
        width: 7px;
    }

   
    .close {
        position: absolute;
        right: 0;
        top: 0;
        padding: 12px 16px 12px 16px;
        cursor: pointer; 
    }

    .close:hover {
        background-color: #f44336;
        color: white;
    }

    
    .header {
        background-color: #FFA500;
        padding: 30px 40px;
        color: white;
        text-align: center;
    }

    
    .header:after {
        content: "";
        display: table;
        clear: both;
    }

    input {
        margin: 0;
        border: none;
        border-radius: 0;
        width: 75%;
        padding: 10px;
        float: left;
        font-size: 16px;
    }

    .addBtn {
        padding: 10px;
        width: 25%;
        background: #d9d9d9;
        color: #555;
        float: left;
        text-align: center;
        font-size: 16px;
        cursor: pointer;
        transition: 0.3s;
        border-radius: 0;
    }

    .addBtn:hover {
        background-color: #bbb;
    }
  </style>
</head>
<body>

<div id="myDIV" class="header">
  <h2>To Do List</h2>
  <input type="text" id="myInput" placeholder="Title...">
  <span onclick="newElement()" class="addBtn">Add</span>
</div>

<ul id="myUL">
</ul>

<script>
var list = document.querySelector('ul');
list.addEventListener('click', function(ev) {
  if (ev.target.className === 'close') {
    var div = ev.target.parentElement;
    div.style.display = "none";
  }
  else if (ev.target.tagName === 'LI') {
    ev.target.classList.toggle('checked');
  }
}, false);

function newElement() {
  var li = document.createElement("li");
  var inputValue = document.getElementById("myInput").value;
  var t = document.createTextNode(inputValue);
  li.appendChild(t);
  if (inputValue === '') {
    alert("You must write something!");
  } else {
    document.getElementById("myUL").appendChild(li);
  }
  document.getElementById("myInput").value = "";

  var span = document.createElement("SPAN");
  var txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  li.appendChild(span);
}
</script>

</body>
</html>
