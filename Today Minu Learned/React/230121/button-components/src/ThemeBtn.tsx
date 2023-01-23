import React, { useState } from "react";
import styled, { keyframes } from "styled-components";

import { TbSun, TbMoon } from "react-icons/tb";

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

function ThemeBtn() {
  const [isDark, setIsDark] = useState(false);

  return (
    <StyledThemeBtn onClick={() => setIsDark(!isDark)} isDark={isDark}>
      {isDark ? (
        <TbMoon size={24} strokeWidth={3} />
      ) : (
        <TbSun size={24} strokeWidth={3} />
      )}
    </StyledThemeBtn>
  );
}

export default ThemeBtn;

interface IStyledThemeBtn {
  isDark: boolean;
}

const sunRise = keyframes`
  from {
    -webkit-transform: rotate(180deg);
    -o-transform: rotate(180deg);
    transform: rotate(180deg);
  }
  to {
    -webkit-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
`;
const sunSet = keyframes`
  from {
    -webkit-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  to {
    -webkit-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
`;

const StyledThemeBtn = styled.button<IStyledThemeBtn>`
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  width: 48px;
  height: 48px;
  border: none;
  border-radius: 32px;
  color: ${(props) => (props.isDark ? BASALT_GRAY_50 : BASALT_GRAY_900)};
  background: ${(props) => (props.isDark ? BASALT_GRAY_900 : BASALT_GRAY_50)};
  animation: ${sunRise} 1s ease-out both;
  transition: all 0.5s ease-in-out;
  &:hover {
    color: ${MANGO_YELLOW_600};
  }
  &:active {
    background: ${(props) => (props.isDark ? BASALT_GRAY_50 : BASALT_GRAY_900)};
    animation: ${sunSet} infinite 3s linear both;
    scale: 0.95;
  }
`;
