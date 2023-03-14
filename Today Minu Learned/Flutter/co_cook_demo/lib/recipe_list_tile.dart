import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'recipe_bookmark.dart';
import 'styles/color.dart';

// ListView.builder(
//   shrinkWrap: true,
//   itemCount: 2,
//   itemBuilder: (BuildContext context, int index) {
//     return RecipeListTile(
//         cardData: {"index": index}, showImage: true);
//   }
// ),

class RecipeListTile extends StatefulWidget {
  const RecipeListTile({
    super.key,
    required this.cardData,
    this.showImage = true,
  });
  final Map cardData; // 데이터 담겨올 변수
  final bool showImage; // 이미지, 북마크 표시여부, 기본값 = true

  @override
  State<RecipeListTile> createState() => _RecipeListTileState();
}

class _RecipeListTileState extends State<RecipeListTile> {
  void toggleBookmark(int index) {
    print("ddd");
  }

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () => print(widget.cardData["index"]), // 클릭시 이벤트 연결
      child: Container(
          // 전체 컨테이너
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
          width: double.infinity, // 부모 요소의 너비를 가져옴
          height: 120,
          child: Row(
            children: [
              widget.showImage
                  ? LayoutBuilder(
                      builder:
                          (BuildContext context, BoxConstraints constraints) {
                        return Container(
                          width: constraints.maxHeight, // 부모 요소의 너비를 가져옴
                          height: constraints.maxHeight, // 부모 요소의 너비와 같은 값으로 설정
                          color: Colors.red,
                        );
                      },
                    )
                  : Container(),
              Expanded(
                child: Container(
                  margin: const EdgeInsets.fromLTRB(16.0, 0.0, 16.0, 24.0),
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Row(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Expanded(
                            child: Container(
                              alignment: Alignment.bottomLeft,
                              height: 48,
                              child: Text(
                                "레시피 이름", // 카드 타일의 제목
                                overflow: TextOverflow.ellipsis,
                                style: const MainTextStyles()
                                    .title2
                                    .copyWith(color: MainColors.monotoneBlack),
                              ),
                            ),
                          ),
                          widget.showImage
                              ? const RecipeBookmark(isAdd: true) // 북마크 여부
                              : Container()
                        ],
                      ),
                      Row(
                        children: [
                          const Icon(
                            Icons.stacked_line_chart,
                            size: 12,
                            color: MainColors.monotoneBlack,
                          ),
                          Container(
                            margin:
                                const EdgeInsets.fromLTRB(4.0, 0.0, 0.0, 0.0),
                            child: Text(
                              "난이도",
                              style: const MainTextStyles()
                                  .caption
                                  .copyWith(color: MainColors.monotoneBlack),
                            ),
                          ),
                        ],
                      ),
                      Row(
                        children: [
                          const Icon(
                            Icons.schedule,
                            size: 12,
                            color: MainColors.monotoneBlack,
                          ),
                          Container(
                            margin:
                                const EdgeInsets.fromLTRB(4.0, 0.0, 0.0, 0.0),
                            child: Text(
                              "시간",
                              style: const MainTextStyles()
                                  .caption
                                  .copyWith(color: MainColors.monotoneBlack),
                            ),
                          )
                        ],
                      ),
                    ],
                  ),
                ),
              )
            ],
          )),
    );
  }
}
