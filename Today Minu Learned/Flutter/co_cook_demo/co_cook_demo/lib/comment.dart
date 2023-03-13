import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'styles/color.dart';

class Comment extends StatefulWidget {
  const Comment({super.key});

  @override
  State<Comment> createState() => _CommentState();
}

class _CommentState extends State<Comment> {
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Text(
              "data",
              style: const MainTextStyles()
                  .subtitle1
                  .copyWith(color: MainColors.monotoneBlack),
            ),
            GestureDetector(
              onTap: () => print("more"),
              child: Container(
                  width: 40,
                  height: 40,
                  child: const Icon(Icons.more_horiz,
                      color: MainColors.monotoneBlack)),
            ),
          ],
        ),
        Placeholder(),
        Container(
            alignment: Alignment.centerLeft,
            child: Text(
              "날짜",
              style: const MainTextStyles()
                  .overline
                  .copyWith(color: MainColors.monotoneBlack),
            )),
        Container(
            alignment: Alignment.centerLeft,
            child: Text(
              "댓글내용",
              style: const MainTextStyles()
                  .body1
                  .copyWith(color: MainColors.monotoneBlack),
            )),
        Row(
          mainAxisAlignment: MainAxisAlignment.end,
          children: [
            Container(
              height: 40,
              child: Row(
                children: [
                  Icon(
                    Icons.thumb_up_outlined,
                    size: 16,
                  ),
                  Text(
                    "좋아요 개수",
                    style: const MainTextStyles()
                        .button
                        .copyWith(color: MainColors.monotoneBlack),
                  ),
                ],
              ),
            ),
            Container(
              margin: EdgeInsets.fromLTRB(8.0, 0.0, 0.0, 0.0),
              height: 40,
              child: Row(
                children: [
                  Icon(
                    Icons.mode_comment_outlined,
                    size: 16,
                  ),
                  Text(
                    "댓글 개수",
                    style: const MainTextStyles()
                        .button
                        .copyWith(color: MainColors.monotoneBlack),
                  ),
                ],
              ),
            ),
          ],
        ),
      ],
    );
  }
}
