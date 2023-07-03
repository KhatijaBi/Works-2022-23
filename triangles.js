class Triangle {
    constructor(base, height) {
      this.base = base;
      this.height = height;
    }
  
    area() {
      return 0.5 * this.base * this.height;
    }
  }
  
  class NTriangles {
    constructor() {
      this.triangles = [];
    }
  
    addTriangle(triangle) {
      this.triangles.push(triangle);
    }
  
    sumOfAreas() {
      return this.triangles.reduce((sum, triangle) => sum + triangle.area(), 0);
    }
  }
  
  const n = 3;  
  
  const nTriangles = new NTriangles();
  
  for (let i = 0; i < n; i++) {
    const base = parseFloat(prompt("Enter the base of the triangle: "));
    const height = parseFloat(prompt("Enter the height of the triangle: "));
    const triangle = new Triangle(base, height);
    nTriangles.addTriangle(triangle);
  }
  
  const totalArea = nTriangles.sumOfAreas();
  
  console.log("The sum of the areas of the triangles is:", totalArea);