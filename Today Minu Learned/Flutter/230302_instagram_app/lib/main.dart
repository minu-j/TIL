import 'dart:io';

import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:path_provider/path_provider.dart';

import 'pages/Home.dart';
import 'pages/Create.dart';
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
  List contentList = [];
  var selectedImage;

  File? _imageFile;

  Future<void> _pickImage() async {
    final picker = ImagePicker();
    final pickedFile = await picker.pickImage(source: ImageSource.gallery);
    if (pickedFile != null) {
      setState(() {
        _imageFile = File(pickedFile.path);
        _saveImageToAsset();
      });
    }
  }

  Future<void> _saveImageToAsset() async {
    if (_imageFile == null) return;

    final bytes = await _imageFile!.readAsBytes();
    final directory = await getApplicationDocumentsDirectory();
    final imagePath = '${directory.path}/new_image.png';
    final newImageFile = File(imagePath);
    await newImageFile.writeAsBytes(bytes);

    await Navigator.push(context,
        MaterialPageRoute(builder: (context){
          return Create(selectedImage: _imageFile, contentList: contentList);
        })
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Instagram"),
        actions: [IconButton(
            onPressed: () async {
              _pickImage();
            },
            icon: const Icon(Icons.add_box_outlined)
          )
        ],
      ),
      body: [Home(contentList: contentList), const Text("shop")][tab],
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
