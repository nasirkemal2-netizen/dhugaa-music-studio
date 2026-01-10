import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

// Providers
import 'providers/audio_provider.dart';
import 'providers/ai_provider.dart';

// Screens
import 'screens/home_screen.dart';
import 'screens/recording_screen.dart';
import 'screens/style_selection_screen.dart';
import 'screens/editor_screen.dart';
import 'screens/export_screen.dart';

void main() {
  runApp(
    MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => AudioProvider()),
        ChangeNotifierProvider(create: (_) => AIProvider()),
      ],
      child: const DhugaaMusicStudioApp(),
    ),
  );
}

class DhugaaMusicStudioApp extends StatelessWidget {
  const DhugaaMusicStudioApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Dhugaa Music Studio',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.green,
      ),
      home: const HomeScreen(),

      // 🔹 Kana galchi: route names
      routes: {
        '/recording': (context) => const RecordingScreen(),
        '/style': (context) => const StyleSelectionScreen(),
        '/editor': (context) => const EditorScreen(),
        '/export': (context) => const ExportScreen(),
      },
    );
  }
}
