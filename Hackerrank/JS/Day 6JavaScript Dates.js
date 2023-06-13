let a = "11/10/2010";

const date = new Date(a);

const dayDict = {
  1: "Monday",
  2: "Tuesday",
  3: "Wednesday",
  4: "Thursday",
  5: "Friday",
  6: "Saturday",
  0: "Sunday",
};
console.log(dayDict[date.getDay()]);
