# Dart asynchronous

```dart
void main() {
  async1();
  async2();
}

void async1() {
  print(1);
  Future.delayed(Duration(seconds: 2), () {
    print(2);
  });
  print(3);
}

void async2() async {
  print(4);
  await Future.delayed(Duration(seconds: 2), () {
    print(5);
  });
  print(6);
}

// 1
// 3
// 4
// 2
// 5
// 6
```
