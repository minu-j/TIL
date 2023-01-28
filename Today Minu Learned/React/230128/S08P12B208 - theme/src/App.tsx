import React from "react";
import "./App.css";

import styled, { ThemeProvider } from "styled-components";

import { darkTheme } from "./styles/themes/darkTheme";
import { lightTheme } from "./styles/themes/lightTheme";
import useTheme from "./styles/themes/useTheme";
import Itheme from "./styles/themes/theme";
import ThemeBtn from "./components/common/button/ThemeBtn";
import LikeBtn from "./components/common/button/LikeBtn";
import ReactionBtn from "./components/common/button/ReactionBtn";

import { TbHandStop, TbHeart, TbFlame } from "react-icons/tb";
import Btn from "./components/common/button/Btn";

function App() {
  const [themeMode, toggleTheme] = useTheme();
  const theme: Itheme = themeMode === "light" ? lightTheme : darkTheme;

  return (
    <ThemeProvider theme={theme}>
      <Main>
        <h1>제목</h1>
        <Box>TEXT</Box>
        <ThemeBtn themeMode={themeMode} toggleTheme={toggleTheme}></ThemeBtn>
        <LikeBtn></LikeBtn>
        <ReactionBtn label={"쓰다듬기"} icon={TbHandStop} color={"#F1A604"} />
        <ReactionBtn label={"예뻐하기"} icon={TbHeart} color={"#ff38a4"} />
        <ReactionBtn label={"응원하기"} icon={TbFlame} color={"#F33041"} />
        <Btn label={"로그인"} type={0} isDisable={false} />
        <Btn label={"로그인"} type={1} isDisable={false} />
        <Btn label={"로그인"} type={2} isDisable={false} />
        <Btn label={"로그인"} type={0} isDisable={true} />
        <Btn label={"로그인"} type={1} isDisable={true} />
        <Btn label={"로그인"} type={2} isDisable={true} />
      </Main>
    </ThemeProvider>
  );
}

export default App;

const Main = styled.div`
  color: ${(props) => props.theme.colors.primaryText};
  background-color: ${(props) => props.theme.colors.primaryBg};
  font: ${(props) => props.theme.fonts.display1};
  width: 100vw;
  height: 100vh;
  transition: all 1s;
`;

const Box = styled.div`
  color: ${(props) => props.theme.colors.yellow};
  background-color: ${(props) => props.theme.colors.green};
  font: ${(props) => props.theme.fonts.mainContentBold};
  width: 100px;
  height: 100px;
  ${(props) => props.theme.styles.card}
`;
