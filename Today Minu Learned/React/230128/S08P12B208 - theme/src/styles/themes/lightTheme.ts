import fonts from "./fonts";
import Itheme from "./theme";
import brandColors from "./colors";

export const lightTheme: Itheme = {
  isDark: false, // 다크모드 여부
  colors: {
    brandColors: brandColors, // 브랜드 컬러 객체
    green: "#14A647",
    blue: "#1790C3",
    yellow: "#F2C619",
    red: "#F33041",
    primaryText: "#3A3948",
    seconderyText: "#75728C",
    primaryBg: "#FCFCFC",
    seconderyBg: "#FCFCFC",
    disable: "#CFCED7", // 비활성화시 표시 색깔
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
      filter: drop-shadow(2px 2px 8px rgba(67, 67, 67, 0.2)) brightness(0.95);
    }
    &:active {
      filter: drop-shadow(2px 2px 8px rgba(67, 67, 67, 0.2)) brightness(0.9);
  }`,
    card: `
    border-radius: 32px;
    filter: drop-shadow(2px 2px 8px rgba(67, 67, 67, 0.2));
    transition: all 0.2s ease-in-out;
    &:hover {
      scale: 1.02;
    }
    &:active {
      filter: drop-shadow(2px 2px 8px rgba(67, 67, 67, 0.2)) brightness(0.9);
      scale: 1;
    }`,
  },
};
