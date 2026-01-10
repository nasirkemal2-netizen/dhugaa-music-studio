import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

// providers
import 'providers/audio_provider.dart';
import 'providers/ai_provider.dart';

// screens
import 'screens/home_screen.dart';
import 'screens/editor_screen.dart';
import 'screens/recording_screen.dart';
import 'screens/export_screen.dart';
import 'screens/style_selection_screen.dart';

void main() {
  runApp(const AppRoot());
}

/// Root widget – Providers hunda of keessaa qaba
class AppRoot extends StatelessWidget {
  const AppRoot({super.key});

  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => AudioProvider()),
        ChangeNotifierProvider(create: (_) => AIProvider()),
      ],
      child: const SirbituuApp(),
    );
  }
}

/// App guddaa – MaterialApp
class SirbituuApp extends StatelessWidget {
  const SirbituuApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Dhugaa Music Studio',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.green,
        useMaterial3: true,
      ),

      /// Screen jalqabaa
      home: const HomeScreen(),

      /// Routes (navigation)
      routes: {
        '/home': (context) => const HomeScreen(),
        '/editor': (context) => const EditorScreen(),
        '/recording': (context) => const RecordingScreen(),
        '/export': (context) => const ExportScreen(),
        '/style': (context) => const StyleSelectionScreen(),
      },
    );
  }
}
