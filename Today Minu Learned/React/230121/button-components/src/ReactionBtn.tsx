import React, { useState } from "react";
import styled, { keyframes } from "styled-components";

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

function ReactionBtn(props: any) {
  const Icon = props.icon;

  return (
    <StyledReactionBtn background={props.color}>
      <Icon size={30} strokeWidth={2}></Icon>
      <StyledBtnLabel>{props.label}</StyledBtnLabel>
    </StyledReactionBtn>
  );
}

export default ReactionBtn;

const StyledReactionBtn = styled.button<any>`
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  width: 56px;
  height: 56px;
  border: none;
  border-radius: 32px;
  color: ${BASALT_GRAY_50};
  background: ${(props) => props.background};
  transition: all 0.2s;
  &:hover {
    width: 117px;
    color: ${(props) => props.background};
  }
  &:active {
    filter: brightness(0.9);
    scale: 0.95;
  }
`;

const StyledBtnLabel = styled.a`
  position: absolute;
  overflow: hidden;
  white-space: nowrap;
  width: 56px;
  height: 56px;
  border-radius: 32px;
  margin-inline: 20px;
  font-family: "NanumSquareNeo-Variable";
  font-weight: 700;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 20px;
  font-weight: bold;
  word-break: break-all;
  transition: all 0.2s;
  opacity: 0;
  &:hover {
    width: 117px;
    opacity: 100;
    color: ${BASALT_GRAY_50};
  }
`;
