import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'styles/color.dart';

class Tag extends StatefulWidget {
  const Tag({super.key, required this.label, required this.onPressed});
  final String label;
  final Function onPressed;

  @override
  State<Tag> createState() => _TagState();
}

class _TagState extends State<Tag> {
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
