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
      padding: EdgeInsets.fromLTRB(0.0, 40.0, 0.0, 0.0),
      borderRadius: const BorderRadius.only(
          topLeft: Radius.circular(16.0), topRight: Radius.circular(16.0)),
      minHeight: 0.0,
      color: MainColors.monotoneLight,
      panel: Column(
        children: [
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
                    myReply: false,
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
            height: 96,
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
