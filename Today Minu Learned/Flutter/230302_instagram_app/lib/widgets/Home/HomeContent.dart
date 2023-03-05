import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter_share/flutter_share.dart';

class HomeContent extends StatefulWidget {
  const HomeContent({Key? key,
    required this.index,
    required this.name,
    required this.location,
    required this.imgSrc,
    required this.isLike,
    required this.likeCnt,
    required this.content,
    required this.likeContent,
  }) : super(key: key);
  final int index;
  final String name;
  final String location;
  final String imgSrc;
  final bool isLike;
  final int likeCnt;
  final String content;
  final Function likeContent;

  @override
  State<HomeContent> createState() => _ContentState();
}

class _ContentState extends State<HomeContent> {
  var f = NumberFormat("###,###,###,###");

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Container(
            width: double.infinity,
            margin: const EdgeInsets.fromLTRB(16, 16, 16, 8),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                SizedBox(
                  child: Row(
                    children: [
                      Container(
                          margin: const EdgeInsets.fromLTRB(0, 0, 8, 0),
                          child: const Icon(Icons.account_circle, size: 40,)
                      ),
                      Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(widget.name, style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w700),),
                          Text(widget.location, style: const TextStyle(fontSize: 12,),),
                        ],
                      ),
                    ],
                  ),
                ),
                IconButton(onPressed: () {
                  _showActionSheet(context);
                }, icon: const Icon(Icons.more_horiz, size: 24,)),
              ],
            )
        ),
        Image.network(widget.imgSrc),
        Container(
          margin: const EdgeInsets.all(8),
          child: Row(
            children: [
              IconButton(onPressed: () {
                widget.likeContent(widget.index);
              }, icon: widget.isLike
                  ? const Icon(Icons.favorite, size: 30, color: Colors.red,)
                  : const Icon(Icons.favorite_border, size: 30,)
              ),
              IconButton(onPressed: () {}, icon: const Icon(Icons.mode_comment_outlined, size: 30,)),
            ],
          ),
        ),
        Container(
          width: double.infinity,
          margin: const EdgeInsets.fromLTRB(20, 0, 20, 0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text("좋아요 ${f.format(widget.likeCnt)}개", style: const TextStyle(fontWeight: FontWeight.w700),),
              Text(widget.name, style: const TextStyle(fontWeight: FontWeight.w700),),
              Text(widget.content),
            ],
          ),
        )

      ],
    );
  }
}

Future<void> share() async {
  await FlutterShare.share(
      title: 'Example share',
      text: 'Example share text',
      linkUrl: 'https://flutter.dev/',
      chooserTitle: 'Example Chooser Title'
  );
}

void _showActionSheet(BuildContext context) {
  showCupertinoModalPopup<void>(
    context: context,
    builder: (BuildContext context) => CupertinoActionSheet(
      title: const Text('더보기'),
      actions: <CupertinoActionSheetAction>[
        CupertinoActionSheetAction(
          isDefaultAction: true,
          onPressed: () {
            share();
            Navigator.pop(context);
          },
          child: const Text('공유'),
        ),
        CupertinoActionSheetAction(
          onPressed: () {
            Navigator.pop(context);
          },
          child: const Text('숨기기'),
        ),
        CupertinoActionSheetAction(
          isDestructiveAction: true,
          onPressed: () {
            Navigator.pop(context);
          },
          child: const Text('신고'),
        ),
      ],
    ),
  );
}

