import React from "react";
import styled from "styled-components";

import ThemeBtn from "../button/ThemeBtn";
import { MdAccountCircle } from "react-icons/md";
import { ReactComponent as TextLogo } from "../logo/TextLogo.svg";
import { NavLink } from "react-router-dom";

interface Iprops {
  // 테마 버튼 props type
  themeMode: string;
  toggleTheme: () => void;
}

function Nav(props: Iprops) {
  return (
    <Navbar>
      <NavContainer>
        <NavLink to={"/"}>
          <NavLogo>
            <TextLogo width={140} height={50}></TextLogo>
          </NavLogo>
        </NavLink>
        <NavbarRSide>
          <NavBtn>로그인</NavBtn>
          <NavBtn>
            <MdAccountCircle size={30}></MdAccountCircle>
          </NavBtn>
          <ThemeBtn themeMode={props.themeMode} toggleTheme={props.toggleTheme}></ThemeBtn>
        </NavbarRSide>
      </NavContainer>
    </Navbar>
  );
}

export default Nav;

const Navbar = styled.nav`
  position: sticky;
  top: 0px;
  width: 100vw;
  height: 60px;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: all 0.1s;
  border-bottom: 1px solid ${(props) => props.theme.colors.disable};
  background-color: ${(props) => props.theme.colors.primaryBg};
  color: ${(props) => props.theme.colors.primaryText};
`;

const NavContainer = styled.div`
  width: 90%;
  max-width: 1056px;
  display: flex;
  justify-content: space-between;
  align-items: center;
`;

const NavLogo = styled.div`
  ${(props) => props.theme.styles.button}
  border: none;
  padding-inline: 10px;
  padding-top: 4px;
  height: 48px;
  filter: none;
  background-color: ${(props) => props.theme.colors.primaryBg};
  font: ${(props) => props.theme.fonts.mainContentBold};
  color: ${(props) => props.theme.colors.primaryText};
  &:hover {
    filter: ${(props) => (props.theme.isDark ? "brightness(1.1)" : "brightness(0.95)")};
  }
  &:active {
    filter: ${(props) => (props.theme.isDark ? "brightness(1.2)" : "brightness(0.9)")};
  }
`;

const NavbarRSide = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  font: ${(props) => props.theme.fonts.mainContentBold};
`;

const NavBtn = styled.button`
  ${(props) => props.theme.styles.button}
  display: flex;
  justify-content: center;
  align-items: center;
  border: none;
  padding-inline: 10px;
  height: 48px;
  filter: none;
  background-color: ${(props) => props.theme.colors.primaryBg};
  font: ${(props) => props.theme.fonts.subContentBold};
  color: ${(props) => props.theme.colors.primaryText};
  &:hover {
    filter: ${(props) => (props.theme.isDark ? "brightness(1.1)" : "brightness(0.95)")};
  }
  &:active {
    filter: ${(props) => (props.theme.isDark ? "brightness(1.2)" : "brightness(0.9)")};
  }
`;
