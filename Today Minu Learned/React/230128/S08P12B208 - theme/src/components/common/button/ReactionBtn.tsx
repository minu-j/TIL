import React from "react";
import styled from "styled-components";

interface Iprops {
  label: string;
  icon: React.ElementType;
  color: string;
}

function ReactionBtn(props: Iprops) {
  const Icon = props.icon;

  return (
    <StyledReactionBtn background={props.color}>
      <Icon size={30} strokeWidth={2}></Icon>
      <StyledBtnLabel>{props.label}</StyledBtnLabel>
    </StyledReactionBtn>
  );
}

export default ReactionBtn;

interface IStyledReactionBtn {
  background: string;
}

const StyledReactionBtn = styled.button<IStyledReactionBtn>`
  ${(props) => props.theme.styles.button}
  display: flex;
  justify-content: center;
  align-items: center;
  width: 56px;
  height: 56px;
  border: none;
  color: ${(props) => props.theme.colors.brandColors.basaltGray[50]};
  background: ${(props) => props.background};
  &:hover {
    width: 117px;
    color: ${(props) => props.background};
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
    color: ${(props) => props.theme.colors.brandColors.basaltGray[50]};
  }
`;
