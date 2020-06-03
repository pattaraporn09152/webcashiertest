import 'package:flutter/material.dart';
void main() => runApp(new MyApp());
class MyApp extends StatelessWidget {
  Widget build(BuildContext context) {
    return new MaterialApp(
      title: 'ตัวอย่าง Flutter Application',
      home: new MyHomePage(title: 'ตัวอย่าง Flutter App'),
    );
  }
}
class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);
  final String title;
  _MyHomePageState createState() => new _MyHomePageState();
}
class _MyHomePageState extends State<MyHomePage> {
  Widget build(BuildContext context) {
    return new Scaffold(
      appBar: new AppBar(
        title: new Text(widget.title),
      ),
      body: new Container(),
      floatingActionButton: new Builder(builder: (context) {
        return new FloatingActionButton(onPressed: () {
          Scaffold.of(context).showSnackBar(
                new SnackBar(
                  backgroundColor: Colors.blue,
                  content: new Text('SnackBar'),
                ),
              );
        });
      }),
    );
  }
}
