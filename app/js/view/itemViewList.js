import itemView from "../view/itemView.js";

export default class itemViewList {
  constructor(itemModelList) {
    this.itemModelList = itemModelList;
    this.addController = null;
    this.delController = null;
    document.querySelector(".registerbtn").addEventListener("click", () => {
      const text = document.querySelector(".comment-input").value;
      if (text != "") {
        this.itemModelList.setUser();
        const date = new Date();
        let strTime = `${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`;
        this.addController(text, strTime);
      } else {
        alert("Введіть текст коментаря!");
      }
    });
    document.querySelector(".list-group").addEventListener("click", (e) => {
      if (e.target.id == "delete")
        this.delController(e.target.parentNode.parentNode.id);
    });
  }

  setAddController(add) {
    this.addController = add;
  }
  setDelController(del) {
    this.delController = del;
  }

  toHtml() {
    const items = this.itemModelList.items
      .map((item) => {
        const ItemView = new itemView(item);
        return ItemView.toHtml();
      })
      .join("");
    document.querySelector(".list-group").innerHTML = items;
  }
}
