import React from "react";
import styled from "styled-components";

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

// 버튼의 설정값(props)
interface IBtn {
  label: string; // 라벨
  color: string; // 색상(green/gray)
  type: number; // 타입(0: primery, 1: secondery, 2: tertiary)
  disabled: boolean; // 비활성화 여부
}

// 각 타입별 버튼의 스타일 타입
interface IBtnStyles {
  border: string; // 테두리 색깔
  color: string; // 라벨 색깔
  background: {
    // 각 상태별 배경색
    normal: string;
    hover: string;
    active: string;
  };
}

function Btn(props: IBtn) {
  // 버튼 타입별 스타일 지정
  const btnStyles: { [key: string]: IBtnStyles } = {
    0: {
      border: `none`,
      color: props.disabled ? BASALT_GRAY_50 : BASALT_GRAY_50,
      background: {
        normal: props.disabled ? BASALT_GRAY_200 : JURASSIC_GREEN_600,
        hover: props.disabled ? BASALT_GRAY_200 : JURASSIC_GREEN_500,
        active: props.disabled ? BASALT_GRAY_200 : JURASSIC_GREEN_700,
      },
    },
    1: {
      border: `4px ${props.disabled ? BASALT_GRAY_200 : JURASSIC_GREEN_600}`,
      color: props.disabled ? BASALT_GRAY_200 : JURASSIC_GREEN_600,
      background: {
        normal: props.disabled ? BASALT_GRAY_50 : BASALT_GRAY_50,
        hover: props.disabled ? BASALT_GRAY_50 : JURASSIC_GREEN_50,
        active: props.disabled ? BASALT_GRAY_50 : JURASSIC_GREEN_100,
      },
    },
    2: {
      border: `none`,
      color: props.disabled ? BASALT_GRAY_200 : JURASSIC_GREEN_600,
      background: {
        normal: props.disabled ? BASALT_GRAY_50 : BASALT_GRAY_50,
        hover: props.disabled ? BASALT_GRAY_50 : JURASSIC_GREEN_50,
        active: props.disabled ? BASALT_GRAY_50 : JURASSIC_GREEN_100,
      },
    },
  };

  return (
    <StyledBtn btnStyles={btnStyles[props.type]} disabled={props.disabled}>
      <StyledBtnLabel>{props.label}</StyledBtnLabel>
    </StyledBtn>
  );
}

export default Btn;

// StyledBtn의 props 타입
interface IStyledBtn {
  btnStyles: IBtnStyles;
}

const StyledBtn = styled.button<IStyledBtn>`
  cursor: ${(props) => (props.disabled ? "not-allowed" : "pointer")};
  max-width: 200px;
  min-height: 48px;
  background: ${(props) => props.btnStyles.background.normal};
  border: none;
  border-radius: 32px;
  padding-inline: 24px;
  padding-block: 10px;
  box-shadow: 0 0 0 ${(props) => props.btnStyles.border} inset;
  color: ${(props) => props.btnStyles.color};
  filter: drop-shadow(2px 2px 8px rgba(67, 67, 67, 0.2));
  transition: all 0.2s;
  &:hover {
    filter: drop-shadow(2px 2px 8px rgba(67, 67, 67, 0.2)) brightness(0.9);
    // background: ${(props) => props.btnStyles.background.hover};
  }
  &:active {
    filter: drop-shadow(2px 2px 8px rgba(67, 67, 67, 0.2)) brightness(0.8);
    // background: ${(props) => props.btnStyles.background.active};
    scale: ${(props) => (props.disabled ? "none" : "0.95")};
  }
`;

const StyledBtnLabel = styled.a`
  font-family: "NanumSquareNeo-Variable";
  font-weight: 700;
  display: flex;
  align-items: center;
  font-size: 20px;
  font-weight: bold;
  word-break: break-all;
`;

