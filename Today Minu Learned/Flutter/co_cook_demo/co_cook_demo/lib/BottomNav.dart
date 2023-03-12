import 'package:flutter/material.dart';
import 'styles/color.dart';

class BottomNav extends StatefulWidget {
  final int currentIndex;
  final ValueChanged<int> onTap;

  BottomNav({
    Key? key,
    required this.currentIndex,
    required this.onTap,
  }) : super(key: key);

  @override
  _BottomNavState createState() => _BottomNavState();
}

class _BottomNavState extends State<BottomNav> {
  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        color: MainColors.monotoneLight,
        boxShadow: const [
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
              GestureDetector(
                onTapDown: (TapDownDetails) {
                  print('Home down');
                },
                onTap: () {
                  print('Home');
                },
                child: Container(
                  width: 40,
                  height: 40,
                  decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(8),
                    color: MainColors.monotoneLightGray,
                  ),
                  child: Icon(
                    Icons.home,
                    color: MainColors.monotoneBlack,
                    size: 18,
                  ),
                ),
              ),
              const SizedBox(
                width: 40,
                height: 40,
                child: Icon(
                  Icons.kitchen_outlined,
                  color: MainColors.monotoneBlack,
                  size: 18,
                ),
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
              const SizedBox(
                width: 40,
                height: 40,
                child: Icon(
                  Icons.search,
                  color: MainColors.monotoneBlack,
                  size: 18,
                ),
              ),
              const SizedBox(
                width: 40,
                height: 40,
                child: Icon(
                  Icons.account_circle_outlined,
                  color: MainColors.monotoneBlack,
                  size: 18,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
