class Line {
    constructor(x1, y1, x2, y2) {        //constructor is a keyword within class which creates an object in class
      this.x1 = x1;                        //this is keyword in class which refers to instance of the class or object
      this.y1 = y1;
      this.x2 = x2;
      this.y2 = y2;
    }
  
    length() {                            //method of the Line class that calculates and returns the length of the line segment using the distance formula.
      return Math.sqrt((this.x2 - this.x1) ** 2 + (this.y2 - this.y1) ** 2);      //This expression calculates the length of the line segment using the distance formula 
    }
  }
  
  class Polygon {
    constructor(lines) {       //This is the constructor method for the Polygon class. It accepts an array (lines) of line segments to initialize the polygon.
      this.lines = lines;     //This line assigns the passed array of line segments to the lines property of the Polygon object being constructed.
    }
  
    perimeter() {          //This is a method of the Polygon class that calculates and returns the perimeter of the polygon.
      let perimeter = 0;      //This line initializes a variable perimeter to store the calculated perimeter of the polygon.
      for (let line of this.lines) {         //This for...of loop iterates over each line segment in the lines array of the polygon.
        perimeter += line.length();              //This line adds the length of each line segment to the perimeter variable.
      }
      return perimeter;              // This line returns the calculated perimeter of the polygon.
    }
  }
  
  // Example 
  //four line segments are created using the Line class constructor and assigned to variables line1, line2, line3, and line4. 
  //a Polygon object polygon is created by passing an array containing these line segments to the Polygon constructor. 
  //the perimeter of the polygon is calculated using the perimeter method and logged to the console using console.log().
  const line1 = new Line(0, 0, 0, 3);
  const line2 = new Line(0, 3, 4, 3);
  const line3 = new Line(4, 3, 4, 0);
  const line4 = new Line(4, 0, 0, 0);
  
  const polygon = new Polygon([line1, line2, line3, line4]);
  console.log("Perimeter of the polygon:", polygon.perimeter());
  