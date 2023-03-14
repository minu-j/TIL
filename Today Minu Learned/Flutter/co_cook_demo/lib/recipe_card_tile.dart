import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'styles/color.dart';

// 상위 위젯에서 그리드 사용시
//
// GridView.builder(
//   shrinkWrap: true,
//   itemCount: 2,
//   gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
//     crossAxisCount: 2, // 2개의 열
//     crossAxisSpacing: 16.0, // 열 간격
//     mainAxisSpacing: 16.0, // 행 간격
//     childAspectRatio: 0.7, // 아이템의 가로 세로 비율
//   ),
//   itemBuilder: (BuildContext context, int index) {
//     return RecipeCardTile(cardData: {index: 1});
//   },
// )

class RecipeCardTile extends StatefulWidget {
  const RecipeCardTile({super.key, required this.cardData});
  final Map cardData; // 카드 데이터

  @override
  State<RecipeCardTile> createState() => _RecipeCardTileState();
}

class _RecipeCardTileState extends State<RecipeCardTile> {
  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () => print(widget.cardData["index"]),
      child: SizedBox(
        width: double.infinity, // 부모 요소의 너비를 가져옴
        child: Column(
          children: [
            LayoutBuilder(
              builder: (BuildContext context, BoxConstraints constraints) {
                return Container(
                  width: constraints.maxWidth, // 부모 요소의 너비를 가져옴
                  height: constraints.maxWidth, // 부모 요소의 너비와 같은 값으로 설정
                  decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(16),
                    color: Colors.white,
                    boxShadow: const [
                      BoxShadow(
                        color: Colors.black26,
                        offset: Offset(1, 1),
                        blurRadius: 6.0,
                        spreadRadius: 0.0,
                      )
                    ],
                  ),
                );
              },
            ),
            Container(
              width: double.infinity,
              height: 40,
              alignment: Alignment.centerLeft,
              child: Text(
                "육개장육개장육개장육개장육개장",
                overflow: TextOverflow.ellipsis,
                style: const MainTextStyles()
                    .title2
                    .copyWith(color: MainColors.monotoneBlack),
              ),
            ),
            Row(
              children: [
                const Icon(
                  Icons.stacked_line_chart,
                  size: 12,
                  color: MainColors.monotoneBlack,
                ),
                Container(
                  margin: const EdgeInsets.fromLTRB(4.0, 0.0, 0.0, 0.0),
                  child: Text(
                    "난이도",
                    style: const MainTextStyles()
                        .caption
                        .copyWith(color: MainColors.monotoneBlack),
                  ),
                ),
                Container(
                  margin: const EdgeInsets.fromLTRB(8.0, 0.0, 0.0, 0.0),
                  child: const Icon(
                    Icons.schedule,
                    size: 12,
                    color: MainColors.monotoneBlack,
                  ),
                ),
                Container(
                  margin: const EdgeInsets.fromLTRB(4.0, 0.0, 0.0, 0.0),
                  child: Text(
                    "시간",
                    style: const MainTextStyles()
                        .caption
                        .copyWith(color: MainColors.monotoneBlack),
                  ),
                )
              ],
            )
          ],
        ),
      ),
    );
  }
}
