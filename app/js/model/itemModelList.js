export default class itemModelList {
  constructor() {
    this.items = JSON.parse(localStorage.getItem("items"));

    this.curentUser = null;
  }

  setUser() {
    this.curentUser = localStorage.getItem("username");
  }
  add(item) {
    if (!this.curentUser) {
      alert("Пройдите регистрацию!");
      return;
    }
    console.log(this.curentUser);
    item.setUser(this.curentUser);
    this.items.push(item);
    localStorage.setItem("items", JSON.stringify(this.items));
  }
  delete(itemId) {
    const itemIndex = this.items.findIndex((item) => item.id === itemId);
    this.items.splice(itemIndex, 1);
    localStorage.setItem("items", this.items);
  }
}
