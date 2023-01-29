import React from "react";
import styled from "styled-components";

import ThemeBtn from "../button/ThemeBtn";
import { MdAccountCircle } from "react-icons/md";
import Itheme from "../../../styles/themes/theme";
import { darkTheme } from "../../../styles/themes/darkTheme";
import { lightTheme } from "../../../styles/themes/lightTheme";
import useTheme from "../../../styles/themes/useTheme";
import { ReactComponent as TextLogo } from "../logo/TextLogo.svg";

interface Iprops {
  // 테마 버튼 props type
  themeMode: string;
  toggleTheme: () => void;
}

function Nav(props: Iprops) {
  return (
    <Navbar>
      <NavContainer>
        <TextLogo width={140} height={50}></TextLogo>
        <NavbarRSide>
          <NavLink>로그인</NavLink>
          <MdAccountCircle size={30}></MdAccountCircle>
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

const NavbarRSide = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  font: ${(props) => props.theme.fonts.mainContentBold};
`;

const NavLink = styled.div`
  ${(props) => props.theme.styles.button}
  padding-inline: 24px;
  padding-block: 10px;
  filter: none;
  background-color: ${(props) => props.theme.colors.primaryBg};
  font: ${(props) => props.theme.fonts.mainContentBold};
  color: ${(props) => props.theme.colors.primaryText};
`;
