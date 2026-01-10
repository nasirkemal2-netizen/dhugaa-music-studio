
import 'package:flutter/material.dart';

class StyleSelectionScreen extends StatelessWidget {
  const StyleSelectionScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Select Music Style'),
      ),
      body: ListView(
        padding: const EdgeInsets.all(20),
        children: [
          _styleTile(context, 'Ethiopian Traditional'),
          _styleTile(context, 'Afro Beat'),
          _styleTile(context, 'Hip Hop'),
          _styleTile(context, 'Gospel'),
          _styleTile(context, 'Acoustic'),
        ],
      ),
    );
  }

  Widget _styleTile(BuildContext context, String styleName) {
    return Card(
      child: ListTile(
        title: Text(styleName),
        trailing: const Icon(Icons.arrow_forward),
        onTap: () {
          Navigator.pushNamed(context, '/editor');
        },
      ),
    );
  }
}
