import React from "react";
import "./App.css";

import { Routes, Route } from "react-router-dom";
import { ThemeProvider } from "styled-components";

import { darkTheme } from "./styles/themes/darkTheme";
import { lightTheme } from "./styles/themes/lightTheme";
import useTheme from "./styles/themes/useTheme";
import Itheme from "./styles/themes/theme";
import ThemeBtn from "./components/common/button/ThemeBtn";

import Nav from "./components/common/Navbar/Nav";

import Test from "./pages/Test";
import HomeTest from "./pages/HomeTest";

function App() {
  const [themeMode, toggleTheme] = useTheme();
  const theme: Itheme = themeMode === "light" ? lightTheme : darkTheme;

  return (
    <ThemeProvider theme={theme}>
      <Nav themeMode={themeMode} toggleTheme={toggleTheme}></Nav>
      <Routes>
        <Route path="/" element={<HomeTest />}></Route>
        <Route path="/test" element={<Test />}></Route>
      </Routes>
    </ThemeProvider>
  );
}

export default App;
