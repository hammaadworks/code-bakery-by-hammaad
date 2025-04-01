class Calculator {
  add(a: number, b: number): number {
    return a + b;
  }

  subtract(a: number, b: number): number {
    return a - b;
  }

  multiply(a: number, b: number): number {
    return a * b;
  }

  divide(a: number, b: number): number {
    if (b === 0) {
      throw new Error("Division by zero is not allowed.");
    }
    return a / b;
  }
}

const calculator = new Calculator();

console.log("Add: ", calculator.add(10, 5));
console.log("Subtract: ", calculator.subtract(10, 5));
console.log("Multiply: ", calculator.multiply(10, 5));
console.log("Divide: ", calculator.divide(10, 5));
