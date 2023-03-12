import 'package:flutter/material.dart';

import 'styles/color.dart';
import 'button.dart';
import 'toggle.dart';
import 'tag.dart';
import 'BottomNav.dart';

void main() {
  runApp(const MainScreen());
}

class MainScreen extends StatefulWidget {
  const MainScreen({super.key});

  @override
  State<MainScreen> createState() => _MainScreenState();
}

class _MainScreenState extends State<MainScreen> {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: HomeScreen(),
    );
  }
}

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  bool isToggleOn = true;

  _buttonAction() {
    print('Button Pressed');
  }

  _toggleChange() {
    setState(() {
      isToggleOn = !isToggleOn;
    });
    print(isToggleOn);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
          title: Text(
            "Co-Cook!",
            style: MainTextStyles().logo.copyWith(color: MainColors.redPrimary),
          ),
          backgroundColor: MainColors.monotoneLight,
          shadowColor: Colors.transparent),
      body: Container(
        alignment: Alignment.center,
        child: Column(children: [
          Button(
            label: "버튼",
            color: ButtonType.red,
            isActive: true,
            onPressed: _buttonAction,
          ),
          Toggle(label: "토글", isToggleOn: isToggleOn, onPressed: _toggleChange),
          Row(
            children: [
              Tag(label: "태그1", onPressed: _buttonAction),
              Tag(label: "태그2", onPressed: _buttonAction),
            ],
          )
        ]),
      ),
      bottomNavigationBar: BottomNav(currentIndex: 0, onTap: (int index) {}),
    );
  }
}
