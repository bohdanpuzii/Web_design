document.addEventListener("click", (e) => {
  if (e.target.id == "adduser") {
    const username = document.querySelector("#username").value;
    const tel = document.querySelector("#tel").value;
    const email = document.querySelector("#email").value;
    const birthday = document.querySelector("#birthday").value;
    localStorage.setItem("username", username);
    localStorage.setItem("tel", tel);
    localStorage.setItem("email", email);
    localStorage.setItem("birthday", birthday);
  }
});
