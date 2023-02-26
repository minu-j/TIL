import { createRoot } from "react-dom/client";
import * as THREE from "three";
import React, { useRef, useState } from "react";
import { Canvas, useFrame } from "@react-three/fiber";
import { Stats, OrbitControls, Stars } from "@react-three/drei";

function Plane(props) {
  const meshRef = useRef();
  const raycaster = new THREE.Raycaster();

  useFrame(({ camera, mouse }) => {
    raycaster.setFromCamera(mouse, camera);
  });

  const onPointerDown = (event) => {
    let intersects = raycaster.intersectObjects(event.target);
    console.log(intersects);
  };

  return (
    <mesh
      onClick={onPointerDown}
      ref={meshRef}
      position={[0, 0, 0]}
      rotation={[-Math.PI / 2, 0, 0]}
      castShadow
      receiveShadow
    >
      <planeGeometry args={[15, 15]} />
      <meshStandardMaterial color={"#ffffff"} />
    </mesh>
  );
}

function Box(props) {
  const meshRef = useRef();

  return (
    <mesh ref={meshRef} position={[0, 1, 0]} castShadow receiveShadow>
      <sphereGeometry args={[1, 32, 32]} />
      <meshStandardMaterial color={"#ffffff"} />
    </mesh>
  );
}

function App() {
  return (
    <div style={{ width: "100vw", height: "100vh" }}>
      <Canvas camera={{ position: [0, 10, 20] }}>
        <color attach="background" args={["#000000"]} />
        <OrbitControls />
        <Stars></Stars>
        <directionalLight
          position={[10, 10, 10]}
          intensity={0.7}
          castShadow
          receiveShadoww
        />
        <Box />
        <Plane />
        <Stats></Stats>
        <gridHelper args={[100, 100]} />
      </Canvas>
    </div>
  );
}

export default App;
