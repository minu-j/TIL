import fonts from "./fonts";
import Itheme from "./theme";
import brandColors from "./colors";

export const darkTheme: Itheme = {
  isDark: true, // 다크모드 여부
  colors: {
    brandColors: brandColors, // 브랜드 컬러 객체
    green: "#4CC068",
    blue: "#68C7EF",
    yellow: "#F2D856",
    red: "#FB4656",
    primaryText: "#FCFCFC",
    seconderyText: "#E6E5E9",
    primaryBg: "#3A3948",
    seconderyBg: "#4E4C5F",
    disable: "#615F75", // 비활성화시 표시 색깔
  },
  fonts: { ...fonts }, // 폰트 스타일 객체
  shadow: "filter: drop-shadow(2px 2px 8px rgba(67, 67, 67, 0.2));", // 기본 그림자 설정
  // 컴포넌트별 기본 스타일 지정
  styles: {
    button: `
    cursor: pointer;
    border-radius: 32px;
    filter: drop-shadow(2px 2px 8px rgba(67, 67, 67, 0.2));
    transition: all 0.1s;
    &:hover {
      filter: drop-shadow(2px 2px 8px rgba(67, 67, 67, 0.2)) brightness(1.1);
    }
    &:active {
      filter: drop-shadow(2px 2px 8px rgba(67, 67, 67, 0.2)) brightness(1.2);
  }`,
    card: `
    border-radius: 32px;
    filter: drop-shadow(2px 2px 8px rgba(67, 67, 67, 0.2));
    transition: all 0.2s ease-in-out;
    &:hover {
      scale: 1.02;
    }
    &:active {
      filter: drop-shadow(2px 2px 8px rgba(67, 67, 67, 0.2)) brightness(1.1);
      scale: 1;
    }`,
  },
};
