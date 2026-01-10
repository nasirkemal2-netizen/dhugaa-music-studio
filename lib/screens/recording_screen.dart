
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/audio_provider.dart';

class RecordingScreen extends StatelessWidget {
  const RecordingScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final audioProvider = Provider.of<AudioProvider>(context);

    return Scaffold(
      appBar: AppBar(
        title: const Text('Voice Recording'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              audioProvider.isRecording
                  ? 'Recording...'
                  : 'Press button to record',
              style: const TextStyle(fontSize: 18),
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                audioProvider.isRecording
                    ? audioProvider.stopRecording()
                    : audioProvider.startRecording();
              },
              child: Text(
                audioProvider.isRecording ? 'Stop' : 'Start Recording',
              ),
            ),
          ],
        ),
      ),
    );
  }
}
