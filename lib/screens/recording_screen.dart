import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../providers/audio_provider.dart';

class RecordingScreen extends StatelessWidget {
  const RecordingScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final audio = context.watch<AudioProvider>();

    return Scaffold(
      appBar: AppBar(
        title: const Text('Voice Recording'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(
              audio.isRecording ? Icons.mic : Icons.mic_none,
              size: 100,
              color: audio.isRecording ? Colors.red : Colors.grey,
            ),
            const SizedBox(height: 20),

            Text(
              audio.isRecording
                  ? 'Recording...'
                  : 'Tap to start recording',
              style: const TextStyle(fontSize: 18),
            ),

            const SizedBox(height: 30),

            ElevatedButton(
              onPressed: audio.isRecording
                  ? audio.stopRecording
                  : audio.startRecording,
              child: Text(
                audio.isRecording ? 'Stop' : 'Record',
              ),
            ),
          ],
        ),
      ),
    );
  }
}
