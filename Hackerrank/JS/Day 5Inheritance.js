class Rectangle {
  constructor(h, w) {
    this.h = h;
    this.w = w;
  }
}

Rectangle.prototype.area = function () {
  return this.h * this.w;
};

class Square extends Rectangle {
  constructor(t) {
    super(3, t);
    console.log(t);
  }
}

const rec = new Rectangle(3, 4);
const squ = new Square(3);

console.log(rec.area());
console.log(squ.area());
