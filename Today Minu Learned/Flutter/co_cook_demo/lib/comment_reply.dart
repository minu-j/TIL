import 'package:flutter/material.dart';
import 'package:sliding_up_panel/sliding_up_panel.dart';

import 'styles/color.dart';
import 'comment_reply_bubble.dart';

final PanelController panelController = PanelController();

class CommentReply extends StatefulWidget {
  const CommentReply({super.key});

  @override
  State<CommentReply> createState() => _CommentReplyState();
}

class _CommentReplyState extends State<CommentReply> {
  @override
  Widget build(BuildContext context) {
    return SlidingUpPanel(
      controller: panelController,
      backdropEnabled: true,
      borderRadius: const BorderRadius.only(
          topLeft: Radius.circular(16.0), topRight: Radius.circular(16.0)),
      minHeight: 0.0,
      color: MainColors.monotoneLight,
      panel: Column(
        children: [
          Container(
            height: 24,
            child: Icon(
              Icons.horizontal_rule_rounded,
              size: 52,
              color: MainColors.monotoneLightGray,
            ),
          ),
          Container(
            padding: EdgeInsets.fromLTRB(16.0, 0, 16.0, 0),
            height: 40,
            child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Text(
                    "댓글 0개",
                    style: const MainTextStyles()
                        .subtitle2
                        .copyWith(color: MainColors.monotoneBlack),
                  ),
                  GestureDetector(
                      onTap: () {
                        panelController.close(); // 댓글창 닫는 함수
                        FocusScope.of(context).unfocus(); // 키보드 닫는 함수
                      },
                      child: Icon(Icons.close))
                ]),
          ),
          Expanded(
            child: SingleChildScrollView(
              reverse: true,
              child: Column(
                children: [
                  CommentReplyBubble(
                    myReply: false,
                  ),
                  CommentReplyBubble(
                    myReply: true,
                  ),
                  CommentReplyBubble(
                    myReply: false,
                  ),
                  CommentReplyBubble(
                    myReply: true,
                  ),
                  CommentReplyBubble(
                    myReply: false,
                  ),
                ],
              ),
            ),
          ),
          Container(
            width: double.infinity,
            height: 48,
            decoration: BoxDecoration(
                color: MainColors.monotoneLight,
                boxShadow: const [
                  BoxShadow(
                    color: Colors.black26,
                    offset: Offset(1, 1),
                    blurRadius: 2.0,
                    spreadRadius: 0.0,
                  )
                ]),
            child: TextField(),
          )
        ],
      ),
    );
  }
}
