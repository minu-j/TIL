import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      // home: Text('HelloWorld'),
      // home: Icon(Icons.star),
      // home: Image.asset('assets/DontLaugh.jpg'),
      // home: Center(
      //   child: Container(width: 50, height: 50, color: Colors.blue)
      // )
      home: Scaffold(
        appBar: AppBar(
          backgroundColor: Colors.blue,
          title: const Text("앱 이름 여기다"),
          leading: const Icon(Icons.star),
          actions: [
            IconButton(
                icon: const Icon(Icons.search),
                onPressed: () {
                  print("touch search");
                }),
            IconButton(
                icon: const Icon(Icons.list),
                onPressed: () {
                  print("touch list");
                }),
            IconButton(
                icon: const Icon(Icons.notifications_none),
                onPressed: () {
                  print("touch alarm");
                }),
          ],
        ),
        body: Align(
          alignment: Alignment.topCenter,
          child: Column(
            children: [
              Container(
                width: double.infinity, height: 100,
                margin: EdgeInsets.all(20),
                padding: EdgeInsets.all(20),
                decoration: BoxDecoration(
                  color: Colors.white,
                  border: Border.all(color: Colors.black26, width: 4),
                  borderRadius: BorderRadius.circular(16),
                  boxShadow: [
                    BoxShadow(
                      color: Colors.grey.withOpacity(0.4),
                      blurRadius: 5.0,
                      spreadRadius: 0.0,
                      offset: const Offset(0,7),
                    )
                  ]
                ),
                child: const Column(
                  children: [
                    Text('안녕하세요?',
                      style: TextStyle(
                        color: Color(0xff175495),
                        fontSize: 20,
                        fontWeight: FontWeight.w700
                      ),
                    ),
                  ],
                ),
              ),
              SizedBox(
                width: double.infinity,
                height: 70,
                child: Row(
                  children: [
                    Container(
                      width: 60,
                      height: 60,
                      child: Image.asset('assets/DontLaugh.jpg', fit: BoxFit.fill,),
                    )
                  ],
                ),
              ),
              ElevatedButton(
                  onPressed: () {
                    print("Touch TextButton");
                  },
                  child: const Text("글자버튼11"),
                  style: const ButtonStyle(
                    backgroundColor: MaterialStatePropertyAll<Color>(Colors.green),
                  )),
              TextButton(onPressed: () {
                print("Touch TextButton");
              }, child: const Text("글자버튼11")),
            ],
          ),
        ),
        // body: Row(
        //   mainAxisAlignment: MainAxisAlignment.spaceEvenly, // display: flex
        //   crossAxisAlignment: CrossAxisAlignment.center,
        //   children: [
        //     Icon(Icons.star),
        //     Icon(Icons.star),
        //     Icon(Icons.star),
        //   ],
        // ),
        // body: Column(
        //   mainAxisAlignment: MainAxisAlignment.spaceEvenly, // display: flex
        //   crossAxisAlignment: CrossAxisAlignment.center,
        //   children: [
        //     Icon(Icons.star),
        //     Icon(Icons.star),
        //     Icon(Icons.star),
        //   ],
        // ),
        bottomNavigationBar: BottomAppBar(
          child: SizedBox(
            height: 70,
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                IconButton(
                    icon: const Icon(Icons.phone),
                    onPressed: () {
                      print("touch phone");
                    }),
                IconButton(
                    icon: const Icon(Icons.message),
                    onPressed: () {
                      print("touch message");
                    }),
                IconButton(
                    icon: const Icon(Icons.contact_page),
                    onPressed: () {
                      print("touch contact_page");
                    }),
              ],
            ),
          )
        ),
      )
    );
  }
}

