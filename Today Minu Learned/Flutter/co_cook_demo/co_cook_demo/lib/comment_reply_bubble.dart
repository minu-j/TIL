import 'package:flutter/material.dart';

import 'styles/color.dart';

class CommentReplyBubble extends StatelessWidget {
  const CommentReplyBubble({super.key, this.myReply = false});
  final bool myReply;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      padding: EdgeInsets.fromLTRB(24.0, 0.0, 24.0, 16.0),
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
            margin: EdgeInsets.fromLTRB(0.0, 4.0, 0.0, 4.0),
            padding: EdgeInsets.fromLTRB(16.0, 8.0, 16.0, 8.0),
            decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(16.0),
                color: myReply
                    ? MainColors.redLight
                    : MainColors.monotoneLightGray),
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
    );
  }
}
