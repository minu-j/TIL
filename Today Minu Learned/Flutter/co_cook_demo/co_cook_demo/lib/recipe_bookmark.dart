import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'dart:ui' as ui;

import 'styles/color.dart';

class RecipeBookmark extends StatefulWidget {
  const RecipeBookmark({super.key, required this.isAdd});
  final bool isAdd; // 북마크 추가여부

  @override
  State<RecipeBookmark> createState() => _RecipeBookmarkState();
}

class _RecipeBookmarkState extends State<RecipeBookmark> {
  late bool isAdd;

  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    setState(() {
      isAdd = widget.isAdd; // 북마크 추가 여부를 받아서 저장
    });
  }

  void toggleIsAdd() {
    setState(() {
      isAdd = !isAdd;
    });
  }

  // 북마크가 추가되어있는지 여부
  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: toggleIsAdd,
      child: Stack(
        alignment: Alignment.center,
        children: [
          Positioned(
              child: CustomPaint(
            size: Size(36, (36 * 1.2).toDouble()),
            painter: RPSCustomPainter(isAdd: isAdd),
          )),
          Positioned(
              child: Container(
                  child: isAdd
                      ? const Icon(
                          Icons.star,
                          color: MainColors.monotoneLight,
                        )
                      : const Icon(
                          Icons.add,
                          color: MainColors.monotoneGray,
                        )))
        ],
      ),
    );
  }
}

// 배경 도형
class RPSCustomPainter extends CustomPainter {
  RPSCustomPainter({required this.isAdd});
  final bool isAdd;

  @override
  void paint(Canvas canvas, Size size) {
    Path path_0 = Path();
    path_0.moveTo(size.width, 0);
    path_0.lineTo(0, 0);
    path_0.lineTo(0, size.height * 0.7551028);
    path_0.lineTo(size.width * 0.5000000, size.height);
    path_0.lineTo(size.width, size.height * 0.7551028);
    path_0.lineTo(size.width, 0);
    path_0.close();

    Paint paint0Fill = Paint()..style = PaintingStyle.fill;
    paint0Fill.color =
        isAdd ? MainColors.redPrimary : MainColors.monotoneLightGray;
    canvas.drawPath(path_0, paint0Fill);
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) {
    return true;
  }
}
