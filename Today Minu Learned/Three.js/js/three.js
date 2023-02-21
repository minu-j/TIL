import * as THREE from "../node_modules/three/build/three.module.js";

// scene
const scene = new THREE.Scene();
scene.background = new THREE.Color(0xcccccc);

// camera
const camera = new THREE.PerspectiveCamera(
  75,
  window.innerWidth / window.innerHeight,
  0.1,
  1000
);
camera.position.z = 10;

// renderer
const renderer = new THREE.WebGLRenderer({
  antialias: true,
});

renderer.setSize(window.innerWidth, window.innerHeight);

let X = 0;
let Y = 0;
window.addEventListener("mousemove", (e) => {
  X = window.innerWidth / 2 - e.pageX;
  Y = window.innerHeight / 2 - e.pageY;
});

document.body.appendChild(renderer.domElement);

// 조명
const light = new THREE.PointLight(0xffffff, 1);
light.position.set(1, 1, 1);
const lightHelper = new THREE.PointLightHelper(light, 1);
scene.add(light);
scene.add(lightHelper);

// 텍스쳐
const textureLoader = new THREE.TextureLoader();
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
cube1.position.x = -4;

const cube2 = new THREE.Mesh(
  new THREE.BoxGeometry(1, 1, 1),
  new THREE.MeshStandardMaterial({
    color: 0x999999,
    metalness: 0.5,
    roughness: 0.3,
  })
);
cube2.position.x = -2;

const cube3 = new THREE.Mesh(
  new THREE.BoxGeometry(1, 1, 1),
  new THREE.MeshStandardMaterial({ color: 0x999999 })
);

const cube4 = new THREE.Mesh(
  new THREE.BoxGeometry(1, 1, 1),
  new THREE.MeshPhysicalMaterial({
    color: 0x999999,
    clearcoat: 1,
  })
);
cube4.position.x = 2;

const cube5 = new THREE.Mesh(
  new THREE.BoxGeometry(1, 1, 1),
  new THREE.MeshStandardMaterial({ color: 0x999999, wireframe: true })
);
cube5.position.x = 4;

scene.add(cube1);
scene.add(cube2);
scene.add(cube3);
scene.add(cube4);
scene.add(cube5);

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

  renderer.render(scene, camera);

  requestAnimationFrame(render);
}

render();

function onWindowResize() {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
}

window.addEventListener("resize", onWindowResize);
