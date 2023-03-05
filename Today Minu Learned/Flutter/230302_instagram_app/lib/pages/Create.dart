import 'package:flutter/material.dart';

class Create extends StatefulWidget {
  const Create({Key? key, this.selectedImage, this.contentList}) : super(key: key);
  final selectedImage;
  final contentList;

  @override
  State<Create> createState() => _CreateState();
}

class _CreateState extends State<Create> {
  createContent(String user, String content) {
    setState(() {
      widget.contentList.add({
        "id": widget.contentList.length + 1,
        "image": "https://codingapple1.github.io/app/img2.jpg",
        "likes": 0,
        "date": "Nov30",
        "content": content,
        "liked": false,
        "user": user,
      });
    });
  }
  String userName = "";
  String content = "";

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(onPressed: () {
          Navigator.pop(context);
        }, icon: const Icon(Icons.arrow_back, color: Colors.black,)),
        title: const Text("New Post", style: TextStyle(fontFamily: ""),),
        actions: [
          TextButton(onPressed: () {
            createContent(userName, content);
            Navigator.pop(context);
            ScaffoldMessenger.of(context).showSnackBar(
              SnackBar(content: Text('Successfully created a new post!')),
            );
          }, child: const Text("Save"))
        ],
      ),
      body: SingleChildScrollView(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Container(
              margin: EdgeInsets.fromLTRB(16, 16, 16, 0),
              child: TextField(
                onChanged: (value) {
                  setState(() {
                    userName = value;
                  });
                },
                onTapOutside: (PointerDownEvent event) {
                  FocusScope.of(context).requestFocus(FocusNode());
                },
                decoration: const InputDecoration(
                  labelText: "Name",
                  hintText: "Input your name",
                ),
              ),
            ),
            Container(
              margin: EdgeInsets.fromLTRB(16, 16, 16, 0),
              child: Row(
                children: [
                  Container(
                    width: 100,
                    height: 100,
                    margin: const EdgeInsets.fromLTRB(0, 0, 16, 0),
                    decoration: BoxDecoration(
                      image: DecorationImage( image: FileImage(widget.selectedImage), fit: BoxFit.cover,),
                    ),
                  ),
                  Expanded(
                    child: TextField(
                      onChanged: (value) {
                        setState(() {
                          content = value;
                        });
                      },
                      maxLines: 4,
                      decoration: InputDecoration(
                        labelText: "Description",
                        hintText: "Input Description here",
                      ),
                    )
                  )
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}

