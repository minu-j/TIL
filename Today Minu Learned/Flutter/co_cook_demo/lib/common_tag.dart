import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'styles/color.dart';

class CommonTag extends StatefulWidget {
  const CommonTag({super.key, required this.label, required this.onPressed});
  final String label; // 태그 라벨
  final Function onPressed; // 버튼이 눌렸을 경우 실행할 함수

  @override
  State<CommonTag> createState() => _CommonTagState();
}

class _CommonTagState extends State<CommonTag> {
  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(16.0),
        boxShadow: const [
          BoxShadow(
            color: Colors.black26,
            offset: Offset(2, 2),
            blurRadius: 6.0,
            spreadRadius: 0.0,
          )
        ],
      ),
      child: CupertinoButton(
          padding: const EdgeInsets.fromLTRB(24.0, 8.0, 12.0, 8.0),
          color: MainColors.monotoneLight,
          minSize: 40.0,
          borderRadius: BorderRadius.circular(16.0),
          onPressed: () {
            widget.onPressed();
          },
          child: Row(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              Text(
                widget.label,
                style: const MainTextStyles()
                    .button
                    .copyWith(color: MainColors.monotoneGray),
              ),
              Container(
                margin: EdgeInsets.fromLTRB(4.0, 0.0, 0.0, 0.0),
                child: Icon(
                  Icons.close,
                  color: MainColors.monotoneGray,
                  size: 16,
                ),
              )
            ],
          )),
    );
  }
}
