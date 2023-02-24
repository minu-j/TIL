import * as THREE from "three";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader";

const fogColor = 0xffffff;
const lightColor = 0xffffff;
const objColor = 0x999999;
const floorColor = 0xcccccc;

// scene
const scene = new THREE.Scene();
scene.background = new THREE.Color(fogColor);

// fog
// scene.fog = new THREE.Fog(fogColor, 6, 16);
// scene.fog = new THREE.FogExp2(fogColor, 0.01);

// camera
const camera = new THREE.PerspectiveCamera(
  75,
  window.innerWidth / window.innerHeight,
  0.1,
  2000
);
camera.position.z = 10;

// renderer
const renderer = new THREE.WebGLRenderer({
  antialias: true,
});
renderer.shadowMap.enabled = true;

renderer.setSize(window.innerWidth, window.innerHeight);

let X = 0;
let Y = 0;
window.addEventListener("mousemove", (e) => {
  X = window.innerWidth / 2 - e.pageX;
  Y = window.innerHeight / 2 - e.pageY;
});

document.body.appendChild(renderer.domElement);
const controls = new OrbitControls(camera, renderer.domElement);
controls.update();

// // 조명
// const light = new THREE.PointLight(lightColor, 0.2);
// light.position.set(0, 10, 10);
// const lightHelper = new THREE.PointLightHelper(light, 1);
// scene.add(light);
// scene.add(lightHelper);
// light.castShadow = true;
// light.shadow.mapSize.width = 2048;
// light.shadow.mapSize.height = 2048;
// light.shadow.radius = 10;
// 조명2
const light2 = new THREE.DirectionalLight(lightColor, 0.2);
light2.position.set(3, 8, -8);
const lightHelper2 = new THREE.DirectionalLightHelper(light2, 1);
scene.add(light2);
scene.add(lightHelper2);
light2.shadow.mapSize.width = 2048;
light2.shadow.mapSize.height = 2048;
light2.shadow.radius = 10;
light2.castShadow = true;

const light3 = new THREE.AmbientLight(lightColor, 0.6);
scene.add(light3);

const textureLoader = new THREE.TextureLoader();

// 배경 텍스쳐
const skyTextureFt = textureLoader.load("img/humble_ft.jpg");
const skyTextureBk = textureLoader.load("img/humble_bk.jpg");
const skyTextureDn = textureLoader.load("img/humble_dn.jpg");
const skyTextureLf = textureLoader.load("img/humble_lf.jpg");
const skyTextureRt = textureLoader.load("img/humble_rt.jpg");
const skyTextureUp = textureLoader.load("img/humble_up.jpg");
const skyTextureList = [
  skyTextureFt,
  skyTextureBk,
  skyTextureUp,
  skyTextureDn,
  skyTextureRt,
  skyTextureLf,
];
const skyMaterialList = skyTextureList.map((texture) => {
  return new THREE.MeshBasicMaterial({
    map: texture,
  });
});
for (let mat = 0; mat < 6; mat++) {
  skyMaterialList[mat].side = THREE.BackSide;
}
console.log(skyMaterialList);

// 배경
const skyGeometry = new THREE.BoxGeometry(2000, 2000, 2000);
const sky = new THREE.Mesh(skyGeometry, skyMaterialList);
scene.add(sky);

// 도형 텍스쳐
const textureBaseColor = textureLoader.load("img/Blue_Ice_001_COLOR.jpg");
const textureBaseNormalMap = textureLoader.load("img/Blue_Ice_001_NORM.jpg");
const textureBaseHeightMap = textureLoader.load("img/Blue_Ice_001_DISP.png");
const textureBaseRoughnessMap = textureLoader.load(
  "img/Blue_Ice_001_ROUGH.jpg"
);
const textureBaseAoMap = textureLoader.load("img/Blue_Ice_001_OCC.jpg");

// 도형
const cube1 = new THREE.Mesh(
  new THREE.SphereGeometry(0.8, 32, 16),
  new THREE.MeshPhysicalMaterial({
    map: textureBaseColor,
    normalMap: textureBaseNormalMap,
    displacementMap: textureBaseHeightMap,
    displacementScale: 0.1,
    roughnessMap: textureBaseRoughnessMap,
    roughness: 0,
    aoMap: textureBaseAoMap,
  })
);
cube1.castShadow = true;
cube1.receiveShadow = true;
cube1.position.x = -4;

const cube2 = new THREE.Mesh(
  new THREE.BoxGeometry(1, 1, 1),
  new THREE.MeshBasicMaterial({
    color: new THREE.Color(0, 0.5, 20),
    toneMapped: false,
  })
);
cube2.castShadow = true;
cube2.position.x = -2;

const cube3 = new THREE.Mesh(
  new THREE.BoxGeometry(1, 1, 1),
  new THREE.MeshStandardMaterial({ color: objColor })
);
cube3.castShadow = true;

const cube4 = new THREE.Mesh(
  new THREE.BoxGeometry(1, 1, 1),
  new THREE.MeshPhysicalMaterial({
    color: objColor,
    clearcoat: 1,
  })
);
cube4.castShadow = true;
cube4.position.x = 2;

const cube5 = new THREE.Mesh(
  new THREE.BoxGeometry(1, 1, 1),
  new THREE.MeshStandardMaterial({ color: objColor, wireframe: true })
);
cube5.castShadow = true;
cube5.position.x = 4;

scene.add(cube1);
scene.add(cube2);
scene.add(cube3);
scene.add(cube4);
scene.add(cube5);

const loader = new GLTFLoader();

loader.load(
  "gltf/Strawberry_gltf.gltf",
  (gltf) => {
    gltf.scene.position.y = 1.5;
    gltf.scene.scale.x = 0.3;
    gltf.scene.scale.y = 0.3;
    gltf.scene.scale.z = 0.3;
    gltf.scene.traverse(function (node) {
      if (node instanceof THREE.Mesh) {
        node.castShadow = true;
        node.receiveShadow = true;
      }
    });

    scene.add(gltf.scene);
  },
  undefined,
  (error) => {
    console.error(error);
  }
);

// 움직임을 주는 함수
const moveDist = (x1, x2, y1, y2) => {
  const dist = Math.sqrt(Math.abs(x2 - x1) ** 2 + Math.abs(y2 - y1) ** 2);
  return dist;
};

// move cube
let mouse = new THREE.Vector3();
let isMove = false;
let nowPosition = { x: null, y: null };
let targetPosition = { x: null, y: null };
let dist;

window.addEventListener("mouseup", (e) => {
  let gapX = e.clientX - e.offsetX;
  let gapY = e.clientY - e.offsetY;

  mouse.x = ((e.clientX - gapX) / e.target.clientWidth) * 2 - 1;
  mouse.y = -((e.clientY - gapY) / e.target.clientHeight) * 2 + 1;
  raycaster.setFromCamera(mouse, camera);
  let intersects = raycaster.intersectObjects(scene.children);
  dist = moveDist(
    cube3.position.x,
    intersects[0].point.x,
    cube3.position.z,
    intersects[0].point.z
  );
  nowPosition = { x: cube3.position.x, y: cube3.position.z };
  targetPosition = { x: intersects[0].point.x, y: intersects[0].point.z };
  isMove = true;
  console.log(nowPosition, targetPosition);
});

const raycaster = new THREE.Raycaster();

// 바닥
const planeGeometry = new THREE.PlaneGeometry(20, 20, 1, 1);
const planeMaterial = new THREE.MeshStandardMaterial({
  color: floorColor,
});
const plane = new THREE.Mesh(planeGeometry, planeMaterial);
plane.rotation.x = -0.5 * Math.PI;
plane.position.y = -1;
scene.add(plane);
plane.receiveShadow = true;

function render(time) {
  const num = 300;
  cube1.rotation.x = Y / num;
  cube1.rotation.y = X / num;
  cube2.rotation.x = Y / num;
  cube2.rotation.y = X / num;
  cube3.rotation.x = Y / num;
  cube3.rotation.y = X / num;
  cube4.rotation.x = Y / num;
  cube4.rotation.y = X / num;
  cube5.rotation.x = Y / num;
  cube5.rotation.y = X / num;
  controls.update();

  renderer.render(scene, camera);
  if (isMove) {
    cube3.position.x += (0.3 * (targetPosition.x - nowPosition.x)) / dist;
    cube3.position.z += (0.3 * (targetPosition.y - nowPosition.y)) / dist;
    setTimeout(() => {
      cube3.position.x = targetPosition.x;
      cube3.position.z = targetPosition.y;
      isMove = false;
    }, dist * 50);
  }

  requestAnimationFrame(render);
}

render();

function onWindowResize() {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
}

window.addEventListener("resize", onWindowResize);
