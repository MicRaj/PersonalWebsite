// Selecting the image element
const image = document.getElementById("hamster");

// Add event listeners for the buttons
document.getElementById("button1").addEventListener("click", function () {
  // Change the image source when Button 1 is clicked
  image.src = "hamster_happy.jpg";
});

document.getElementById("button2").addEventListener("click", function () {
  // Change the image source when Button 2 is clicked
  image.src = "hamster_angry.jpg";
});
