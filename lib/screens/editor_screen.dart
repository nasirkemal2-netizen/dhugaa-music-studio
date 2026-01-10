import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../providers/ai_provider.dart';

class EditorScreen extends StatelessWidget {
  const EditorScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final ai = context.watch<AIProvider>();

    return Scaffold(
      appBar: AppBar(
        title: const Text('Audio Editor'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(
              Icons.auto_fix_high,
              size: 100,
              color: ai.isProcessing ? Colors.orange : Colors.grey,
            ),
            const SizedBox(height: 20),

            Text(
              ai.isProcessing
                  ? 'Processing audio with AI...'
                  : 'Split vocals & instruments',
              style: const TextStyle(fontSize: 18),
            ),

            const SizedBox(height: 30),

            ElevatedButton(
              onPressed: ai.isProcessing
                  ? null
                  : () async {
                      ai.startProcessing();
                      await Future.delayed(const Duration(seconds: 3));
                      ai.stopProcessing();
                    },
              child: const Text('Start AI Split'),
            ),
          ],
        ),
      ),
    );
  }
}
