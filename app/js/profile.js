document.addEventListener("DOMContentLoaded", () => {
  idlist = ["username", "email", "tel", "birthday"];
  if (localStorage.getItem("username") != null) {
    idlist.forEach((item) => {
      document.querySelector(`#${item}`).innerHTML = localStorage.getItem(item);
    });
  } else {
    document.querySelector("#username").innerHTML = "Вы не зарегестрированы!";
  }
});
