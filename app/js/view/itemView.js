export default class itemView {
  constructor(itemModel) {
    this.itemModel = itemModel;
  }

  toHtml() {
    return `  <li class="list-group-item" id='${this.itemModel.id}'>
    <div class="text d-flex flex-row"><a href="profile.html">${this.itemModel.username}</a>: ${this.itemModel.text}  
        <button style="padding: 0px; margin-left: 10px;" id='delete'>×</button>
    </div>
    <div style="font-size:10px">${this.itemModel.time}</div>
    
</li>`;
  }
}
