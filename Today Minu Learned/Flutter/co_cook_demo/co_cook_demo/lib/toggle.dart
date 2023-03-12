import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'styles/color.dart';

class Toggle extends StatefulWidget {
  const Toggle(
      {super.key,
      required this.label,
      required this.isToggleOn,
      required this.onPressed});
  final String label;
  final bool isToggleOn;
  final Function onPressed;

  @override
  State<Toggle> createState() => _ToggleState();
}

class _ToggleState extends State<Toggle> {
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
