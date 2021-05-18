import itemModel from "../model/itemModel.js";

export default class controller {
  constructor(itemModelList, itemViewList) {
    this.itemModelList = itemModelList;
    this.itemViewList = itemViewList;
    this.itemViewList.setAddController(this.addItem);
    this.itemViewList.setDelController(this.delItem);
    this.onModelChange();
    this.itemViewList.toHtml();
  }

  addItem(text, time) {
    const item = new itemModel(text, time);
    this.itemModelList.add(item);
  }
  delItem() {
    this.itemModelList.delete();
  }

  onModelChange() {
    const handler = {
      set: (obj, prop, val) => {
        obj[prop] = val;
        this.itemViewList.toHtml();
        return true;
      },
    };
    this.itemModelList.items = new Proxy(this.itemModelList.items, handler);
  }
}
