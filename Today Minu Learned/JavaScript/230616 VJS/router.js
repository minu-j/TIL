export default class {
  constructor() {
    this.path = location.pathname;

    switch (this.path) {
      case "/":
        this.title = "Home";
        break;
      case "/posts":
        this.title = "Post";
        break;
      case "/settings":
        this.title = "Setting";
    }
  }

  async getComponent() {
    return `<h1>${this.title} 슈웅</h1>`;
  }
}
