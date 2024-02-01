# A amperage Flet app

An example of a minimal Flet app.

To run the app:

```
flet run main.py
```

build app for detail

```
flet build apk -vv
flet build apk --flutter-build-args=--target-platform --flutter-build-args=android-arm  --flutter-build-args=--analyze-size

flet build apk --flutter-build-args=--release --no-android-splash
```

hot reload

```
flet run main.py --android

```