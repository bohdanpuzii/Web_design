import itemModelList from "./model/itemModelList.js";
import itemViewList from "./view/itemViewList.js";

import controller from "./controller/controller.js";
console.log();
if (localStorage.getItem("items") == null) {
  const items = [];
  localStorage.setItem("items", JSON.stringify(items));
}
// const items = [];
// localStorage.setItem("items", JSON.stringify(items));
const ItemModelList = new itemModelList();
const ItemViewList = new itemViewList(ItemModelList);

const Controller = new controller(ItemModelList, ItemViewList);
