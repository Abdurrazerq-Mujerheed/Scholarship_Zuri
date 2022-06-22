let input_1 = Number(prompt("Enter the first number"));
let input_2 = Number(prompt("Enter the second number"));

let operation = prompt("Choose the operator: +, -, * or /");

if (typeof input_1 == "number" && typeof input_2 == "number") {
  if (operation == "+") {
    add = input_1 + input_2;
    alert(add);
  } else if (operation == "-") {
    sub = input_1 - input_2;
    alert(sub);
  } else if (operation == "*") {
    mul = input_1 * input_2;
    alert(mul);
  } else if (operation == "/") {
    if (input_2 == 0) {
      alert("The second number is 0");
    } else {
      div = input_1 / input_2;
      alert(div);
    }
  } else {
    alert("Unknown operator");
  }
} else {
  alert("Both numbers must be a number");
}
