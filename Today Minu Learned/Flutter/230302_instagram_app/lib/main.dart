import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'package:intl/intl.dart';
import 'style.dart' as style;

void main() {
  runApp(
    MaterialApp(
      theme: style.theme,
      home: const MyApp()
    )
  );
}

class MyApp extends StatefulWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  int tab = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Instagram"),
        actions: [IconButton(
            onPressed: () {},
            icon: const Icon(Icons.add_box_outlined)
          )
        ],
      ),
      body: [const HomePage(), const Text("shop")][tab],
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: tab,
        selectedItemColor: Colors.black,
        showSelectedLabels: false,
        showUnselectedLabels: false,
        onTap: (tabNum) {
          setState(() {
            tab = tabNum;
          });
        },
        items: const <BottomNavigationBarItem>[
          BottomNavigationBarItem(
            icon: (Icon(Icons.home_outlined)),
            label: 'Home',
          ),
          BottomNavigationBarItem(
              icon: Icon(Icons.shopping_bag_outlined),
              label: 'Shop'
          ),
        ],
      ),
    );
  }
}

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  List<Map> contentList = [
    {
      "name": "Minu",
      "location": "대전광역시",
      "imgSrc": "assets/images/sampleImage.jpg",
      "isLike": false,
      "likeCnt": 1000000000000,
      "content":
          "장문의 글을 써보아요 움치치 움치치 장문의 글을 써보아요 움치치 움치치 장문의 글을 써보아요 움치치 움치치 장문의 글을 써보아요 움치치 움치치",
    },
    {
      "name": "Minu",
      "location": "대전광역시",
      "imgSrc": "assets/images/sampleImage.jpg",
      "isLike": false,
      "likeCnt": 1000000000000,
      "content":
      "장문의 글을 써보아요 움치치 움치치 장문의 글을 써보아요 움치치 움치치 장문의 글을 써보아요 움치치 움치치 장문의 글을 써보아요 움치치 움치치",
    },
    {
      "name": "Minu",
      "location": "대전광역시",
      "imgSrc": "assets/images/sampleImage.jpg",
      "isLike": false,
      "likeCnt": 1000000000000,
      "content":
      "장문의 글을 써보아요 움치치 움치치 장문의 글을 써보아요 움치치 움치치 장문의 글을 써보아요 움치치 움치치 장문의 글을 써보아요 움치치 움치치",
    }
  ];

  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      itemCount: contentList.length,
      itemBuilder: (context, index) {
        return Content(
          index: index,
          name: contentList[index]["name"],
          location: contentList[index]["location"],
          imgSrc: contentList[index]["imgSrc"],
          isLike: contentList[index]["isLike"],
          likeCnt: contentList[index]["likeCnt"],
          content: contentList[index]["content"],
          likeContent: likeContent,
        );
      }
    );
  }

  likeContent(index) {
    setState(() {
      if (contentList[index]["isLike"]) {
        contentList[index]["likeCnt"]--;
      } else {
        contentList[index]["likeCnt"]++;
      }
      contentList[index]["isLike"] = !contentList[index]["isLike"];
    });
  }
}


class Content extends StatefulWidget {
  const Content({Key? key,
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
  State<Content> createState() => _ContentState();
}

class _ContentState extends State<Content> {
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
            IconButton(onPressed: () {}, icon: const Icon(Icons.more_horiz, size: 24,)),
            ],
          )
        ),
        Image.asset(widget.imgSrc),
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
