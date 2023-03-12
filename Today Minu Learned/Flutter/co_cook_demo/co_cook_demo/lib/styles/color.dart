import 'package:flutter/material.dart';

class MainColors {
  const MainColors();

  static const Color redLight = Color(0xfff2e4d9);
  static const Color redTertiary = Color(0xfff3b5a8);
  static const Color redSecondary = Color(0xffd95b4f);
  static const Color redPrimary = Color(0xffd91604);
  static const Color monotoneBlack = Color(0xff2e2928);
  static const Color monotoneGray = Color(0xff78706f);
  static const Color monotoneLightGray = Color(0xffdfdddd);
  static const Color monotoneLight = Color(0xfffcfcfc);
  static const Color greenPrimary = Color(0xff3ca833);
  static const Color brownPrimary = Color(0xff866844);
}

class MainTextStyles {
  const MainTextStyles();

  TextStyle get title1 => const TextStyle(
        fontFamily: "Pretendard",
        fontSize: 24,
        decoration: TextDecoration.none,
        fontStyle: FontStyle.normal,
        fontWeight: FontWeight.w800,
        height: 24 / 24,
        letterSpacing: 0,
      );

  TextStyle get title2 => const TextStyle(
        fontFamily: "Pretendard",
        fontSize: 20,
        decoration: TextDecoration.none,
        fontStyle: FontStyle.normal,
        fontWeight: FontWeight.w800,
        height: 20 / 20,
        letterSpacing: 0,
      );

  TextStyle get subtitle1 => const TextStyle(
        fontFamily: "Pretendard",
        fontSize: 16,
        decoration: TextDecoration.none,
        fontStyle: FontStyle.normal,
        fontWeight: FontWeight.w600,
        height: 16 / 16,
        letterSpacing: 0,
      );

  TextStyle get subtitle2 => const TextStyle(
        fontFamily: "Pretendard",
        fontSize: 14,
        decoration: TextDecoration.none,
        fontStyle: FontStyle.normal,
        fontWeight: FontWeight.w600,
        height: 14 / 14,
        letterSpacing: 0,
      );

  TextStyle get body1 => const TextStyle(
        fontFamily: "Pretendard",
        fontSize: 16,
        decoration: TextDecoration.none,
        fontStyle: FontStyle.normal,
        fontWeight: FontWeight.w400,
        height: 16 / 16,
        letterSpacing: 0,
      );

  TextStyle get body2 => const TextStyle(
        fontFamily: "Pretendard",
        fontSize: 14,
        decoration: TextDecoration.none,
        fontStyle: FontStyle.normal,
        fontWeight: FontWeight.w400,
        height: 14 / 14,
        letterSpacing: 0,
      );

  TextStyle get button => const TextStyle(
        fontFamily: "Pretendard",
        fontSize: 14,
        decoration: TextDecoration.none,
        fontStyle: FontStyle.normal,
        fontWeight: FontWeight.w700,
        height: 14 / 14,
        letterSpacing: 0,
      );

  TextStyle get caption => const TextStyle(
        fontFamily: "Pretendard",
        fontSize: 12,
        decoration: TextDecoration.none,
        fontStyle: FontStyle.normal,
        fontWeight: FontWeight.w400,
        height: 12 / 12,
        letterSpacing: 0,
      );

  TextStyle get overline => const TextStyle(
        fontFamily: "Pretendard",
        fontSize: 10,
        decoration: TextDecoration.none,
        fontStyle: FontStyle.normal,
        fontWeight: FontWeight.w400,
        height: 10 / 10,
        letterSpacing: 0,
      );

  TextStyle get logo => const TextStyle(
        fontFamily: "LeagueGothic",
        fontSize: 24,
        height: 24 / 24,
        letterSpacing: 0,
      );
}
