import 'package:flutter/material.dart';
import 'styles/color.dart';

class BottomNavIcon extends StatefulWidget {
  const BottomNavIcon({
    super.key,
    required this.index,
    required this.currentIndex,
    required this.icon,
    required this.iconOutlined,
    required this.onTap,
  });
  final int index; // 페이지 인덱스
  final int currentIndex; // 현재 페이지 인덱스
  final IconData icon; // 아이콘
  final IconData iconOutlined; // 아웃라인 아이콘
  final Function onTap; // 탭하면 실행될 함수

  @override
  State<BottomNavIcon> createState() => _BottomNavIconState();
}

class _BottomNavIconState extends State<BottomNavIcon> {
  bool _isTapDown = false;

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTapDown: (details) {
        setState(() {
          _isTapDown = true;
        });
      },
      onTapUp: (details) {
        setState(() {
          _isTapDown = false;
        });
        widget.onTap(widget.index);
      },
      child: Container(
        width: 40,
        height: 40,
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(8),
          color: _isTapDown ? MainColors.monotoneLightGray : null,
        ),
        child: Icon(
          widget.index == widget.currentIndex
              ? widget.icon
              : widget.iconOutlined,
          color: MainColors.monotoneBlack,
          size: 18,
        ),
      ),
    );
  }
}
