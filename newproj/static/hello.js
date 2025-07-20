function sayHello() {
    let name = document.getElementById("nm").value;
    if (name.trim() !== "") {
        alert("Hello " + name + "!");
    } else {
        alert("Please enter your name.");
    }
}
