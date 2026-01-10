import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../providers/audio_provider.dart';
import '../providers/ai_provider.dart';

class EditorScreen extends StatelessWidget {
  const EditorScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final audio = context.watch<AudioProvider>();
    final ai = context.watch<AIProvider>();

    return Scaffold(
      appBar: AppBar(
        title: const Text('Studio Editor'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          children: [
            Text(
              audio.isRecording
                  ? 'Recording in progress...'
                  : 'Ready to record',
              style: const TextStyle(fontSize: 18),
            ),
            const SizedBox(height: 20),

            ElevatedButton(
              onPressed: audio.isRecording
                  ? audio.stopRecording
                  : audio.startRecording,
              child: Text(
                audio.isRecording ? 'Stop Recording' : 'Start Recording',
              ),
            ),

            const SizedBox(height: 30),

            ElevatedButton(
              onPressed: ai.isProcessing
                  ? null
                  : () {
                      ai.startProcessing();
                      Future.delayed(const Duration(seconds: 2), () {
                        ai.stopProcessing();
                      });
                    },
              child: Text(
                ai.isProcessing
                    ? 'AI Processing...'
                    : 'Generate AI Music',
              ),
            ),
          ],
        ),
      ),
    );
  }
}
