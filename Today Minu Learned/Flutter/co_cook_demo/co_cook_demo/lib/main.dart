import 'package:flutter/material.dart';

import 'styles/color.dart';
import 'bottom_nav_bar.dart';
import 'recipe_card_tile.dart';
import 'common_button.dart';
import 'common_tag.dart';
import 'common_toggle.dart';
import 'recipe_list_tile.dart';
import 'comment.dart';
import 'comment_reply.dart';

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
      home: CommentScreen(),
    );
  }
}

class CommentScreen extends StatefulWidget {
  const CommentScreen({super.key});

  @override
  State<CommentScreen> createState() => _CommentScreenState();
}

class _CommentScreenState extends State<CommentScreen> {
  void changeTabIndex(int index) {
    setState(() {
      _currentIndex = index;
    });
    print('탭 변경 : $_currentIndex');
  }

  int _currentIndex = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
          title: Text(
            "Co-Cook!",
            style: const MainTextStyles()
                .logo
                .copyWith(color: MainColors.redPrimary),
          ),
          backgroundColor: MainColors.monotoneLight,
          shadowColor: Colors.transparent),
      body: Stack(children: [
        Column(children: [
          Comment(
            highlight: true,
            myComment: true,
            panelController: panelController,
          ),
        ]),
        CommentReply()
      ]),
      bottomNavigationBar:
          BottomNav(currentIndex: _currentIndex, onTap: changeTabIndex),
    );
  }
}

// class HomeScreen extends StatefulWidget {
//   const HomeScreen({super.key});

//   @override
//   State<HomeScreen> createState() => _HomeScreenState();
// }

// class _HomeScreenState extends State<HomeScreen> {
//   bool isToggleOn = true;

//   void _buttonAction() {
//     print('Button Pressed');
//   }

//   void _toggleChange() {
//     setState(() {
//       isToggleOn = !isToggleOn;
//     });
//     print(isToggleOn);
//   }

//   void changeTabIndex(int index) {
//     setState(() {
//       _currentIndex = index;
//     });
//     print('탭 변경 : $_currentIndex');
//   }

//   int _currentIndex = 0;

//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(
//           title: Text(
//             "Co-Cook!",
//             style: const MainTextStyles()
//                 .logo
//                 .copyWith(color: MainColors.redPrimary),
//           ),
//           backgroundColor: MainColors.monotoneLight,
//           shadowColor: Colors.transparent),
//       body: Container(
//         alignment: Alignment.center,
//         child: Column(children: [
//           CommonButton(
//             label: "버튼",
//             color: ButtonType.red,
//             isActive: true,
//             onPressed: _buttonAction,
//           ),
//           CommonToggle(
//               label: "토글", isToggleOn: isToggleOn, onPressed: _toggleChange),
//           Row(
//             children: [
//               CommonTag(label: "태그1", onPressed: _buttonAction),
//               CommonTag(label: "태그2", onPressed: _buttonAction),
//             ],
//           ),
//           GridView.builder(
//             shrinkWrap: true,
//             itemCount: 2,
//             gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
//               crossAxisCount: 2, // 2개의 열
//               crossAxisSpacing: 16.0, // 열 간격
//               mainAxisSpacing: 16.0, // 행 간격
//               childAspectRatio: 0.7, // 아이템의 가로 세로 비율
//             ),
//             itemBuilder: (BuildContext context, int index) {
//               return RecipeCardTile(cardData: {"index": index});
//             },
//           ),
//           ListView.builder(
//               shrinkWrap: true,
//               itemCount: 2,
//               itemBuilder: (BuildContext context, int index) {
//                 return RecipeListTile(
//                     cardData: {"index": index}, showImage: true);
//               }),
//         ]),
//       ),
//       bottomNavigationBar:
//           BottomNav(currentIndex: _currentIndex, onTap: changeTabIndex),
//     );
//   }
// }
