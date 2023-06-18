import Router from "./router.js";

const $app = document.querySelector("#app");
const $nav = document.querySelector(".nav");

const render = async () => {
  const routes = [
    { path: "/", component: Router },
    { path: "/posts", component: Router },
    { path: "/settings", component: Router },
  ];

  // 페이지의 pathname과 route의 path가 같은지 확인합니다.
  let isMatch = routes.find((route) => route.path === location.pathname);

  // isMatch 여부에 따라 동적으로 렌더링 되는 component
  // 잘못된 주소를 입력할 경우 isMatch는 undefined 입니다.
  const $component = isMatch ? isMatch.component : NotFound;

  const $page = new $component();

  // 해당되는 페이지를 동적으로 삽입합니다.
  $app.innerHTML = await $page.getComponent();
};

$nav.addEventListener("click", (e) => {
  if (!e.target.matches(".nav > li > a")) return;

  // 페이지가 이동하지 않게 하기 위한 코드
  e.preventDefault();

  const path = e.target.getAttribute("href");

  if (window.location.pathname === path) return;

  // 클릭이벤트가 발생했을 때 주소를 변경하기 위한 코드
  window.history.pushState(null, null, path);

  render();
});
window.addEventListener("popstate", () => render());

document.addEventListener("DOMContentLoaded", () => render());
