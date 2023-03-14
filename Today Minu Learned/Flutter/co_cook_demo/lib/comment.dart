import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'styles/color.dart';

class Comment extends StatefulWidget {
  const Comment(
      {super.key,
      this.highlight = false,
      this.myComment = false,
      required this.panelController});
  final bool highlight;
  final bool myComment;
  final panelController;

  @override
  State<Comment> createState() => _CommentState();
}

class _CommentState extends State<Comment> {
  bool _isLike = false;

  void _toggleLike() {
    setState(() {
      _isLike = !_isLike;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      color: widget.highlight ? MainColors.redLight : MainColors.monotoneLight,
      padding: const EdgeInsets.fromLTRB(24.0, 0.0, 24.0, 0.0),
      child: Column(
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text(
                widget.myComment ? "내 한줄평" : "data",
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
          Container(
            height: 168,
            color: Colors.black,
          ),
          Container(
              margin: const EdgeInsets.fromLTRB(0.0, 8.0, 0.0, 0.0),
              alignment: Alignment.centerLeft,
              child: Text(
                "2023. 3. 13.",
                style: const MainTextStyles()
                    .overline
                    .copyWith(color: MainColors.monotoneBlack),
              )),
          Container(
              margin: const EdgeInsets.fromLTRB(0.0, 8.0, 0.0, 0.0),
              alignment: Alignment.centerLeft,
              child: Text(
                "댓글내용댓글내용댓글내용댓글내용댓글내용댓글내용댓글내용댓글내용댓글내용댓글내용댓글내용댓글내용댓글내용댓글내용댓글내용댓글내용댓글내용댓글내용댓글내용댓글내용댓글내용댓글내용댓글내용댓글내용댓글내용댓글내용댓글내용댓글내용댓글내용댓글내용댓글내용댓글내용댓글내용",
                style: const MainTextStyles()
                    .body1
                    .copyWith(color: MainColors.monotoneBlack),
              )),
          Row(
            mainAxisAlignment: MainAxisAlignment.end,
            children: [
              GestureDetector(
                onTap: _toggleLike,
                child: Container(
                  height: 40,
                  color: widget.highlight
                      ? MainColors.redLight
                      : MainColors.monotoneLight,
                  child: Row(
                    children: [
                      Icon(
                        _isLike ? Icons.thumb_up : Icons.thumb_up_outlined,
                        size: 16,
                        color: _isLike
                            ? MainColors.redPrimary
                            : MainColors.monotoneBlack,
                      ),
                      Container(
                        margin: const EdgeInsets.fromLTRB(4.0, 0.0, 0.0, 0.0),
                        child: Text(
                          "245",
                          style: const MainTextStyles()
                              .button
                              .copyWith(color: MainColors.monotoneBlack),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
              GestureDetector(
                onTap: () => widget.panelController.open(),
                child: Container(
                  margin: const EdgeInsets.fromLTRB(8.0, 0.0, 0.0, 0.0),
                  height: 40,
                  color: widget.highlight
                      ? MainColors.redLight
                      : MainColors.monotoneLight,
                  child: Row(
                    children: [
                      const Icon(
                        Icons.mode_comment_outlined,
                        size: 16,
                      ),
                      Container(
                        margin: const EdgeInsets.fromLTRB(4.0, 0.0, 0.0, 0.0),
                        child: Text(
                          "32",
                          style: const MainTextStyles()
                              .button
                              .copyWith(color: MainColors.monotoneBlack),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
}
