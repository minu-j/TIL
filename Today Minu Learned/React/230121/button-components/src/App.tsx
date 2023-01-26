import React from "react";
import styled from "styled-components";

import Btn from "./Btn";
import LikeBtn from "./LikeBtn";
import ThemeBtn from "./ThemeBtn";
import ReactionBtn from "./ReactionBtn";

import { TbHandStop, TbHeart, TbFlame } from "react-icons/tb";

const JURASSIC_GREEN_50 = "#DCFAE3";
const JURASSIC_GREEN_100 = "#BCEDC6";
const JURASSIC_GREEN_200 = "#95DBA3";
const JURASSIC_GREEN_300 = "#6BCB80";
const JURASSIC_GREEN_400 = "#4CC068";
const JURASSIC_GREEN_500 = "#21B44F";
const JURASSIC_GREEN_600 = "#14A647";
const JURASSIC_GREEN_700 = "#00913A";
const JURASSIC_GREEN_800 = "#00812F";
const JURASSIC_GREEN_900 = "#00631E";
const MANGO_YELLOW_50 = "#FBF8E7";
const MANGO_YELLOW_100 = "#F8EDB9";
const MANGO_YELLOW_200 = "#F4E289";
const MANGO_YELLOW_300 = "#F2D856";
const MANGO_YELLOW_400 = "#F1CE31";
const MANGO_YELLOW_500 = "#F2C619";
const MANGO_YELLOW_600 = "#F2C619";
const MANGO_YELLOW_700 = "#F1A604";
const MANGO_YELLOW_800 = "#F39800";
const MANGO_YELLOW_900 = "#F37700";
const BASALT_GRAY_50 = "#FCFCFC";
const BASALT_GRAY_100 = "#E6E5E9";
const BASALT_GRAY_200 = "#CFCED7";
const BASALT_GRAY_300 = "#B9B7C4";
const BASALT_GRAY_400 = "#A2A0B1";
const BASALT_GRAY_500 = "#8C899F";
const BASALT_GRAY_600 = "#75728C";
const BASALT_GRAY_700 = "#615F75";
const BASALT_GRAY_800 = "#4E4C5F";
const BASALT_GRAY_900 = "#3A3948";
const DARK_INFORMATIVE = "#68C7EF";
const DARK_DANGER = "#FB4656";
const LIGHT_INFORMATIVE = "#1790C3";
const LIGHT_DANGER = "#F33041";

function App() {
  return (
    <AppContainer>
      <Btn label={"로그인"} color={"green"} type={0} disabled={false}/>
      <Btn label={"로그인"} color={"green"} type={1} disabled={false}/>
      <Btn label={"로그인"} color={"green"} type={2} disabled={false}/>
      <Btn label={"로그인"} color={"green"} type={0} disabled={true}/>
      <Btn label={"로그인"} color={"green"} type={1} disabled={true}/>
      <Btn label={"로그인"} color={"green"} type={2} disabled={true}/>
      <LikeBtn></LikeBtn>
      <ThemeBtn></ThemeBtn>
      <ReactionBtn
        label={"쓰다듬기"}
        icon={TbHandStop}
        color={"#F1A604"}
      />
      <ReactionBtn
        label={"예뻐하기"}
        icon={TbHeart}
        color={"#ff38a4"}
        />
      <ReactionBtn
        label={"응원하기"}
        icon={TbFlame}
        color={"#F33041"}
        />
    </AppContainer>
  );
}

export default App;

const AppContainer = styled.div`
  width: 100vw;
  height: 100vh;
  background-color: ${BASALT_GRAY_50};
`;
