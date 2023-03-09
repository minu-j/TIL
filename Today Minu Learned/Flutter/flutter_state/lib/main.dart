import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter_local_notifications/flutter_local_notifications.dart';
import 'package:provider/provider.dart';
import 'dart:convert';

import 'package:shared_preferences/shared_preferences.dart';
import 'notification.dart';

void main() {
  runApp(ChangeNotifierProvider(create: (context) => Store1(), child: const MyApp()));
}

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    initNotification();
  }
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return CupertinoApp(
      title: 'Flutter Demo',
      home: const MyHomePage(title: 'HomePage'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
    saveData(_counter);
  }

  void _resetCounter() async {
    var storage = await SharedPreferences.getInstance();
    storage.remove('number');
    setState(() {
      _counter = 0;
    });
  }

  getData() async {
    var storage = await SharedPreferences.getInstance();
    var storageNum = storage.getInt('number');
    if (storageNum != null) {
      setState(() {
        _counter = storageNum;
      });
    }

    saveData(_counter);
  }

  saveData(int num) async {
    var storage = await SharedPreferences.getInstance();
    storage.setInt('number', num);
    print(storage.get('number'));
  }

  showNotification() async {

    var androidDetails = AndroidNotificationDetails(
      '유니크한 알림 채널 ID',
      '알림종류 설명',
      icon: 'app_icon',
      priority: Priority.high,
      importance: Importance.max,
      color: Color.fromARGB(255, 255, 0, 0),
    );

    var iosDetails = DarwinNotificationDetails(
      presentAlert: true,
      presentBadge: true,
      presentSound: true,
    );

    // 알림 id, 제목, 내용 맘대로 채우기
    notifications.show(
        1,
        '제목1',
        '내용1',
        NotificationDetails(android: androidDetails, iOS: iosDetails)
    );
  }

  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    getData();
  }


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: CupertinoNavigationBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        middle: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text(
              'You have pushed the button this many times:',
            ),
            GestureDetector(
              child: Text(
                '$_counter',
                style: Theme.of(context).textTheme.headlineMedium,
              ),
              onTap: () {
                Navigator.push(context, 
                  CupertinoPageRoute(builder: (context) => NumberDetail(previousTitle: 'HomePage'))
                );
              },
            ),
            CupertinoButton(onPressed: _incrementCounter, child: Text('Increment')),
            TextButton(onPressed: _resetCounter, child: Text('Reset')),
            CupertinoButton(child: Text("알림뿅"), onPressed: showNotification, color: Colors.blue,)
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Increment',
        child: const Icon(Icons.add),
      ), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}

class Store1 extends ChangeNotifier {
  int num2 = 0;
  void _incrementNum2() {
    num2++;
    notifyListeners();
  }
}

class NumberDetail extends StatelessWidget {
  const NumberDetail({Key? key, required this.previousTitle}) : super(key: key);
  final String previousTitle;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: CupertinoNavigationBar(
        previousPageTitle: 'HomePageHomePageHomePageHomePageHomePage',
        middle: Text('${context.watch<Store1>().num2}')),
      body: Row(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          CupertinoButton(
            onPressed: context.read<Store1>()._incrementNum2,
            child: Text('asdf'),
            color: Colors.blue,
            borderRadius: const BorderRadius.all(Radius.circular(16))
          ),

        ],
      ),
    );
  }
}
