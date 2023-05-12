const container = document.querySelector(".movie-seats");
const count = document.getElementById("count");
const total = document.getElementById("total");





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
}














