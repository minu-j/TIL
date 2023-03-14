import 'package:flutter/material.dart';

import 'styles/color.dart';

class CommentReplyBubble extends StatelessWidget {
  const CommentReplyBubble({super.key, this.myReply = false});
  final bool myReply;

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onLongPressDown: (TapDownDetails) => print("내려감"),
      onLongPress: () => print("댓글세부내용"),
      child: Container(
        width: double.infinity,
        padding: EdgeInsets.fromLTRB(24.0, 8.0, 24.0, 8.0),
        child: Column(
          crossAxisAlignment:
              myReply ? CrossAxisAlignment.end : CrossAxisAlignment.start,
          children: [
            myReply
                ? Container()
                : Text(
                    "닉네임",
                    style: const MainTextStyles()
                        .caption
                        .copyWith(color: MainColors.monotoneBlack),
                  ),
            Container(
              constraints: BoxConstraints(minWidth: 100, maxWidth: 300),
              margin: EdgeInsets.fromLTRB(0.0, 8.0, 0.0, 8.0),
              padding: EdgeInsets.fromLTRB(16.0, 8.0, 16.0, 8.0),
              decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(16.0),
                  color: myReply
                      ? MainColors.redTertiary
                      : MainColors.monotoneLight,
                  boxShadow: const [
                    BoxShadow(
                      color: Colors.black26,
                      offset: Offset(1, 1),
                      blurRadius: 6.0,
                      spreadRadius: 0.0,
                    )
                  ]),
              child: Text(
                "댓글내용댓글내용댓글내용댓글내용 댓글내용댓글내용댓글내용댓글내용 s",
                style: const MainTextStyles()
                    .body1
                    .copyWith(color: MainColors.monotoneBlack),
              ),
            ),
            Text(
              "2023. 3. 8",
              style: const MainTextStyles()
                  .caption
                  .copyWith(color: MainColors.monotoneBlack),
            ),
          ],
        ),
      ),
    );
  }
}
