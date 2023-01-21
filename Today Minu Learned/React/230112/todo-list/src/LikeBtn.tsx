import React, { useState } from 'react';
import styled from 'styled-components';

const JURASSIC_GREEN_50 = '#DCFAE3';
const JURASSIC_GREEN_100 = '#BCEDC6';
const JURASSIC_GREEN_200 = '#95DBA3';
const JURASSIC_GREEN_300 = '#6BCB80';
const JURASSIC_GREEN_400 = '#4CC068';
const JURASSIC_GREEN_500 = '#21B44F';
const JURASSIC_GREEN_600 = '#14A647';
const JURASSIC_GREEN_700 = '#00913A';
const JURASSIC_GREEN_800 = '#00812F';
const JURASSIC_GREEN_900 = '#00631E';
const MANGO_YELLOW_50 = '#FBF8E7';
const MANGO_YELLOW_100 = '#F8EDB9';
const MANGO_YELLOW_200 = '#F4E289';
const MANGO_YELLOW_300 = '#F2D856';
const MANGO_YELLOW_400 = '#F1CE31';
const MANGO_YELLOW_500 = '#F2C619';
const MANGO_YELLOW_600 = '#F2C619';
const MANGO_YELLOW_700 = '#F1A604';
const MANGO_YELLOW_800 = '#F39800';
const MANGO_YELLOW_900 = '#F37700';
const BASALT_GRAY_50 = '#FCFCFC';
const BASALT_GRAY_100 = '#E6E5E9';
const BASALT_GRAY_200 = '#CFCED7';
const BASALT_GRAY_300 = '#B9B7C4';
const BASALT_GRAY_400 = '#A2A0B1';
const BASALT_GRAY_500 = '#8C899F';
const BASALT_GRAY_600 = '#75728C';
const BASALT_GRAY_700 = '#615F75';
const BASALT_GRAY_800 = '#4E4C5F';
const BASALT_GRAY_900 = '#3A3948';
const DARK_INFORMATIVE = '#68C7EF';
const DARK_DANGER = '#FB4656';
const LIGHT_INFORMATIVE = '#1790C3';
const LIGHT_DANGER = '#F33041';

  function LikeBtn() {
    return (
      <StyledLikeBtn>
          <svg width={25} height={25} viewBox="0 0 28 27">
            <ThumbIcon d="M7.38,12v12c0,.4-.15,.78-.43,1.06-.28,.28-.65,.44-1.04,.44H2.97c-.39,0-.76-.16-1.04-.44-.28-.28-.43-.66-.43-1.06V13.5c0-.4,.15-.78,.43-1.06,.28-.28,.65-.44,1.04-.44H7.38Zm0,0c1.56,0,3.06-.63,4.16-1.76,1.1-1.12,1.72-2.65,1.72-4.24v-1.5c0-.8,.31-1.56,.86-2.12,.55-.56,1.3-.88,2.08-.88s1.53,.32,2.08,.88c.55,.56,.86,1.33,.86,2.12v7.5h4.41c.78,0,1.53,.32,2.08,.88,.55,.56,.86,1.33,.86,2.12l-1.47,7.5c-.21,.92-.61,1.71-1.14,2.25-.53,.54-1.16,.8-1.8,.75H11.79c-1.17,0-2.29-.47-3.12-1.32-.83-.84-1.29-1.99-1.29-3.18"/>
          </svg>
          <StyledLikeBtnLabel>좋아요</StyledLikeBtnLabel>
      </StyledLikeBtn>
    )
  }

export default LikeBtn;

const ThumbIcon = styled.path`
  fill: none;
  stroke: #14a647;
  stroke-linecap: round;
  stroke-linejoin: round;
  stroke-width: 3px;
`

const StyledLikeBtn = styled.button<any>`
  display: flex;
  align-items: center;
  justify-content: space-around;
  cursor: pointer;
  width: 147px;
  height: 48px;
  background: ${ BASALT_GRAY_50 };
  border: none;
  border-radius: 32px;
  padding-inline: 24px;
  padding-block: 10px;
  color: ${ JURASSIC_GREEN_600 };
  filter: drop-shadow(2px 2px 8px rgba(67, 67, 67, 0.2));
  transition: background 0.1s;
  transition: scale 0.1s;
  &:hover {
    background: ${ JURASSIC_GREEN_50 };
  }
  &:active {
    background: ${ JURASSIC_GREEN_100 };
  }
  font-size: 20px;
  font-weight: bold;
  word-break:break-all;
`

const StyledLikeBtnLabel = styled.h3`
  font-family: 'NanumSquareNeo-Variable';
  font-weight: 700;
  display: flex;
  align-items: center;
  font-size: 20px;
  font-weight: bold;
  word-break:break-all;
`