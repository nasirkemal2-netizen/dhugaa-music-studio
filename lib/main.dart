import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import 'providers/audio_provider.dart';
import 'providers/ai_provider.dart';
import 'screens/home_screen.dart';

void main() {
  runApp(const AppRoot());
}

/// Root widget – Providers fi MaterialApp walitti qabee qaba
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

/// App guddaa (MaterialApp)
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
      home: const HomeScreen(),
    );
  }
}
