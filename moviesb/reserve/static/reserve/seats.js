const container = document.querySelector(".movie-seats");
const count = document.getElementById("count");
const total = document.getElementById("total");
const price = document.getElementById("price");




let ticketPrice=120;

container.addEventListener("click", (e) => {
    if (e.target.classList.contains("seat") && !e.target.classList.contains("occupied")) {
      e.target.classList.toggle("selected");
      selectedseats();
    }
  });

function selectedseats(){
    const selectedSeats = document.querySelectorAll(".row .seat.selected");
    console.log(selectedSeats);
    const selectedSeatsCount = selectedSeats.length;
    console.log(selectedSeatsCount);
    count.innerText = selectedSeatsCount;
    total.innerText = selectedSeatsCount * ticketPrice;
    price.value = selectedSeatsCount * ticketPrice;
}
// -------------------------------------------------------------------------
function sun() {
  document.getElementById("day").value = "Sunday"
  document.getElementById("sun").style.color="black"
  document.getElementById("tue").style.color="white"
  document.getElementById("thurs").style.color="white"
}
function tue() {
  document.getElementById("day").value = "Tuesday"
  document.getElementById("sun").style.color="white"
  document.getElementById("tue").style.color="black"
  document.getElementById("thurs").style.color="white"

}
function thurs() {
  document.getElementById("day").value = "Thursday"
  document.getElementById("sun").style.color="white"
  document.getElementById("tue").style.color="white"
  document.getElementById("thurs").style.color="black"
}
// -------------------------------------------------------------------------
function first() {
  document.getElementById("time").value = "3:15 PM"
  document.getElementById("first").style.color="black"
  document.getElementById("sec").style.color="white"
  document.getElementById("thir").style.color="white"
}
function sec() {
  document.getElementById("time").value = "5:30 PM"
  document.getElementById("first").style.color="white"
  document.getElementById("sec").style.color="black"
  document.getElementById("thir").style.color="white"

}
function thir() {
  document.getElementById("time").value = "7:45 PM"
  document.getElementById("first").style.color="white"
  document.getElementById("sec").style.color="white"
  document.getElementById("thir").style.color="black"
}














