// Get the video
var video = document.getElementById("myVideo");

// Get the button
var btn = document.getElementById("myBtn");

// Pause and play the video, and change the button text
function myFunction() {
  if (video.paused) {
    video.play();
    btn.innerHTML = "Pause";
  } else {
    video.pause();
    btn.innerHTML = "Play";
  }
}

const LOGIN = document.getElementById("login-form");
const REGISTER = document.getElementById("register-form");
const BTNS = document.getElementById("buttons");
const TIMEOUT = 450;

const EMAIL_R = document.getElementById("email-r");
const USERNAME_R = document.getElementById("username-r");
const PASSWORD_R = document.getElementById("password-r");
const PASSWORD_REPEAT_R = document.getElementById("password-repeat-r");

const USERNAME_L = document.getElementById("username-l");
const PASSWORD_L = document.getElementById("password-l");

function changeForm(arg) {
  arg.classList.add("active");
  manageButtons(0);
  if (arg.innerHTML == "Register") {
    BTNS.children[1].classList.remove("active");
    LOGIN.classList.add("fadeout");
    setTimeout(() => {
      LOGIN.classList.add("hidden");
      REGISTER.classList.remove("hidden");
      REGISTER.classList.add("fadein");
      BTNS.style.marginTop = "20px";
      LOGIN.classList.remove("fadeout");
      setTimeout(() => {
        REGISTER.classList.remove("fadein");
        manageButtons(1);
      }, TIMEOUT);
    }, TIMEOUT);
  } else {
    BTNS.children[0].classList.remove("active");
    REGISTER.classList.add("fadeout");
    setTimeout(() => {
      REGISTER.classList.add("hidden");
      LOGIN.classList.remove("hidden");
      LOGIN.classList.add("fadein");
      BTNS.style.marginTop = "90px";
      REGISTER.classList.remove("fadeout");
      setTimeout(() => {
        LOGIN.classList.remove("fadein");
        manageButtons(1);
      }, TIMEOUT);
    }, TIMEOUT);
  }
}

function manageButtons(num) {
  if (num == 0) {
    BTNS.children[0].disabled = true;
    BTNS.children[1].disabled = true;
  } else {
    BTNS.children[0].disabled = false;
    BTNS.children[1].disabled = false;
  }
}

PASSWORD_REPEAT_R.addEventListener("input", () => {
  if (PASSWORD_REPEAT_R.value != PASSWORD_R.value) {
    document.getElementById("warning-passmatch").style.display = "block";
  } else {
    document.getElementById("warning-passmatch").style.display = "none";
  }
});

PASSWORD_R.addEventListener("input", () => {
  if (PASSWORD_REPEAT_R.value != PASSWORD_R.value) {
    document.getElementById("warning-passmatch").style.display = "block";
  } else {
    document.getElementById("warning-passmatch").style.display = "none";
  }
});

PASSWORD_R.addEventListener("input", () => {
  if (PASSWORD_R.value.length < 8) {
    document.getElementById("warning-passlength").style.display = "block";
  } else {
    document.getElementById("warning-passlength").style.display = "none";
  }
});

USERNAME_R.addEventListener("focusout", () => {
  if (USERNAME_R.value == "") {
    document.getElementById("warning-usernameempty").style.display = "block";
  } else {
    document.getElementById("warning-usernameempty").style.display = "none";
  }
});

EMAIL_R.addEventListener("focusout", () => {
  if (EMAIL_R.value == "") {
    document.getElementById("warning-emailempty").style.display = "block";
  } else {
    document.getElementById("warning-emailempty").style.display = "none";
  }
});

function showPass() {
  const PASS_INPUTS = [PASSWORD_R, PASSWORD_REPEAT_R];
  for (i in PASS_INPUTS) {
    if (PASS_INPUTS[i].type == "password") PASS_INPUTS[i].type = "text";
    else PASS_INPUTS[i].type = "password";
  }
}

function showPassLogin() {
  if (PASSWORD_L.type == "password") PASSWORD_L.type = "text";
  else PASSWORD_L.type = "password";
}

function register() {
  const ERRORS = document.querySelectorAll("small");
  const R_INPUTS = document.querySelectorAll("#register-form input");
  let errorQty = 0;
  ERRORS.forEach((e) => {
    if (e.style.display == "block") errorQty++;
  });
  R_INPUTS.forEach((e) => {
    if (e.value == "") errorQty++;
  });

  if (errorQty == 0) {
    alert(
      `User ${USERNAME_R.value} registered on email ${EMAIL_R.value}\nThanks for registering`
    );
  } else {
    alert("Can't proceed, there are errors active on registration");
  }
}

function login() {
  if (PASSWORD_L.value == "12345678" && USERNAME_L.value != "") {
    alert(`Welcome back, ${USERNAME_L.value} 💎`);
  } else {
    alert("Missing username/password or wrong password");
  }
}
