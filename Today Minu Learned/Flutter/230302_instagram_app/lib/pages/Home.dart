import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:flutter/rendering.dart';
import 'package:flutter/cupertino.dart';

import '../widgets/Home/HomeContent.dart';

class Home extends StatefulWidget {
  const Home({Key? key, this.contentList}) : super(key: key);
  final contentList;

  @override
  State<Home> createState() => _HomePageState();
}

class _HomePageState extends State<Home> {
  get contentList => widget.contentList;

  getData() async {
    final response = await http.get(Uri.parse('https://codingapple1.github.io/app/data.json'));
    await Future.delayed(const Duration(seconds: 2));
    await setData(jsonDecode(response.body));
    print(response.body);
  }

  getMoreData() async {
    final response = await http.get(Uri.parse('https://codingapple1.github.io/app/more1.json'));
    await setData([jsonDecode(response.body)]);
  }

  setData(jsonResponse) async {
    setState(() {
      for (var json in jsonResponse) {
        contentList.add(json);
      }
    });
  }

  var scroll = ScrollController();

  @override
  void initState() {
    super.initState();
    getData();
    scroll.addListener(() {
      if (scroll.position.pixels == scroll.position.maxScrollExtent) {
        getMoreData();
      };
    });
  }

  @override
  Widget build(BuildContext context) {
    if (contentList.isNotEmpty) {
      return ListView.builder(
        controller: scroll,
        itemCount: contentList.length + 1,
        itemBuilder: (context, index) {
          if (index < contentList.length) {
            return HomeContent(
              index: index,
              name: contentList[index]["user"],
              location: "대전광역시",
              imgSrc: contentList[index]["image"],
              isLike: contentList[index]["liked"],
              likeCnt: contentList[index]["likes"],
              content: contentList[index]["content"],
              likeContent: likeContent,
            );
          } else {
            return const SizedBox(
              width: double.infinity,
              height: 100,
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                  CupertinoActivityIndicator(),
                ],
              )
            );
          }
        }
      );
    } else {
      return const SizedBox(
        width: double.infinity,
        height: double.infinity,
        child: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            CupertinoActivityIndicator(),
          ],
        ),
      );
    }
  }

  likeContent(index) {
    setState(() {
      if (contentList[index]["liked"]) {
        contentList[index]["likes"]--;
      } else {
        contentList[index]["likes"]++;
      }
      contentList[index]["liked"] = !contentList[index]["liked"];
    });
  }
}