import 'package:flutter/material.dart';
import 'styles/color.dart';

import 'bottom_nav_bar_icon.dart';

class BottomNav extends StatefulWidget {
  BottomNav({
    Key? key,
    required this.currentIndex,
    required this.onTap,
  }) : super(key: key);
  final int currentIndex;
  final ValueChanged<int> onTap;

  @override
  _BottomNavState createState() => _BottomNavState();
}

class _BottomNavState extends State<BottomNav> {
  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: const BoxDecoration(
        color: MainColors.monotoneLight,
        boxShadow: [
          BoxShadow(
            color: Colors.black26,
            offset: Offset(0, 4),
            blurRadius: 6.0,
            spreadRadius: 0.0,
          )
        ],
      ),
      child: SafeArea(
        child: SizedBox(
          height: 64,
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              BottomNavIcon(
                index: 0,
                icon: Icons.home,
                iconOutlined: Icons.home_outlined,
                onTap: widget.onTap,
                currentIndex: widget.currentIndex,
              ),
              BottomNavIcon(
                index: 1,
                icon: Icons.kitchen,
                iconOutlined: Icons.kitchen_outlined,
                onTap: widget.onTap,
                currentIndex: widget.currentIndex,
              ),
              GestureDetector(
                  onTapDown: (TapDownDetails) {
                    print('co-cook down');
                  },
                  onTap: () {
                    print('co-cook!');
                  },
                  child: SizedBox(
                    height: 56,
                    child: const Image(
                        image: AssetImage('assets/images/Logo_3d_Circle.png')),
                  )),
              BottomNavIcon(
                index: 2,
                icon: Icons.screen_search_desktop_rounded,
                iconOutlined: Icons.screen_search_desktop_outlined,
                onTap: widget.onTap,
                currentIndex: widget.currentIndex,
              ),
              BottomNavIcon(
                index: 3,
                icon: Icons.account_circle,
                iconOutlined: Icons.account_circle_outlined,
                onTap: widget.onTap,
                currentIndex: widget.currentIndex,
              ),
            ],
          ),
        ),
      ),
    );
  }
}
