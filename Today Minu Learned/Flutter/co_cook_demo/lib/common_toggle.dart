import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'styles/color.dart';

class CommonToggle extends StatefulWidget {
  const CommonToggle(
      {super.key,
      required this.label,
      required this.isToggleOn,
      required this.onPressed});
  final String label; // 토글 라벨
  final bool isToggleOn; // 토글의 상태
  final Function onPressed; // 버튼이 눌렸을 경우 실행할 함수

  @override
  State<CommonToggle> createState() => _CommonToggleState();
}

class _CommonToggleState extends State<CommonToggle> {
  @override
  Widget build(BuildContext context) {
    return CupertinoButton(
      padding: const EdgeInsets.fromLTRB(24.0, 8.0, 24.0, 8.0),
      color: widget.isToggleOn
          ? MainColors.redPrimary
          : MainColors.monotoneLightGray,
      minSize: 32.0,
      borderRadius: BorderRadius.circular(16.0),
      onPressed: () {
        widget.onPressed();
      },
      child: Text(widget.label,
          style: const MainTextStyles().button.copyWith(
              color: widget.isToggleOn
                  ? MainColors.monotoneLight
                  : MainColors.monotoneGray)),
    );
  }
}
