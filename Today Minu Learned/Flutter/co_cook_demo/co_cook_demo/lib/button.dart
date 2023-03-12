import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'styles/color.dart';

// 버튼 타입
enum ButtonType { red, green, none }

class Button extends StatefulWidget {
  const Button(
      {super.key,
      required this.label,
      required this.color,
      required this.isActive,
      required this.onPressed});
  final String label;
  final ButtonType color;
  final bool isActive;
  final Function onPressed;

  @override
  State<Button> createState() => _ButtonState();
}

class _ButtonState extends State<Button> {
  @override
  Widget build(BuildContext context) {
    Color buttonColor;
    Color labelColor =
        widget.isActive ? MainColors.monotoneLight : MainColors.monotoneGray;
    switch (widget.color) {
      case ButtonType.red:
        buttonColor = widget.isActive
            ? MainColors.redPrimary
            : MainColors.monotoneLightGray;
        break;
      case ButtonType.green:
        buttonColor = widget.isActive
            ? MainColors.greenPrimary
            : MainColors.monotoneLightGray;
        break;
      case ButtonType.none:
        buttonColor = Colors.transparent;
        labelColor = widget.isActive
            ? MainColors.redPrimary
            : MainColors.monotoneLightGray;
        break;
    }

    return CupertinoButton(
      padding: const EdgeInsets.fromLTRB(24.0, 8.0, 24.0, 8.0),
      color: buttonColor,
      minSize: 40.0,
      borderRadius: BorderRadius.circular(16.0),
      onPressed: () {
        widget.isActive ? widget.onPressed() : null;
      },
      child: Text(widget.label,
          style: const MainTextStyles().button.copyWith(color: labelColor)),
    );
  }
}
