import React from "react";
import styled, { keyframes } from "styled-components";

import { TbThumbUp } from "react-icons/tb";

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

function LikeBtn() {
  const thumbUpIconAnimate = function () {
    const thumbUpIcon: Element | null =
      document.querySelector(".thumb-up-icon");
    thumbUpIcon?.animate(
      [
        { transform: "translateY(0px) rotate(0deg)" },
        { transform: "translateY(-15px) rotate(-17deg) scale(220%)" },
        { transform: "translateY(18px) rotate(17deg) scale(220%)" },
        { transform: "translateY(-8px) rotate(-12deg) scale(180%)" },
        { transform: "translateY(5px) rotate(10deg) scale(150%)" },
        { transform: "translateY(-3px) rotate(-6deg) scale(120%)" },
        { transform: "translateY(0px) rotate(0deg)" },
      ],
      {
        duration: 1000,
        easing: "ease-out",
      }
    );
  };

  return (
    <StyledLikeBtn
      onClick={() => {
        thumbUpIconAnimate();
      }}
    >
      <ThumbUpIcon className="thumb-up-icon">
        <TbThumbUp size={32} />
      </ThumbUpIcon>
      <StyledLikeBtnLabel>좋아요</StyledLikeBtnLabel>
    </StyledLikeBtn>
  );
}

export default LikeBtn;

const StyledLikeBtn = styled.button`
  display: flex;
  align-items: center;
  justify-content: space-around;
  cursor: pointer;
  width: 140px;
  height: 48px;
  background: ${BASALT_GRAY_50};
  border: none;
  border-radius: 32px;
  padding-inline: 24px;
  padding-block: 10px;
  color: ${JURASSIC_GREEN_600};
  filter: drop-shadow(2px 2px 8px rgba(67, 67, 67, 0.2));
  transition: background 0.1s;
  font-size: 20px;
  font-weight: bold;
  word-break: break-all;
  transition: all 0.2s;
  &:hover {
    background: ${JURASSIC_GREEN_50};
  }
  &:active {
    background: ${JURASSIC_GREEN_100};
    scale: 0.95;
  }
`;

const ThumbUpIcon = styled.div``;

const StyledLikeBtnLabel = styled.a`
  font-family: "NanumSquareNeo-Variable";
  font-weight: 700;
  display: flex;
  align-items: center;
  font-size: 20px;
  font-weight: bold;
  word-break: break-all;
`;
