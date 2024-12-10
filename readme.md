# Build Flutter IPA for Altstore
![Screenshot](https://cloud-1zkeqlrh7-hack-club-bot.vercel.app/0screen_shot_2024-12-07_at_11.21.20___pm.png)

## Why you need to use it

1. Free Installation of Apps Without Jailbreaking

AltStore uses Apple’s Developer program mechanism to sideload apps without requiring a jailbreak. This makes it an attractive option for users who want to run non-App Store apps for free while keeping their devices secure.

2. How AltStore Works with .ipa Files

AltStore works by signing and installing .ipa files (iOS app packages). To install an app through AltStore:

- You need a valid .ipa file for the app you want.
- AltStore re-signs the .ipa using your Apple ID and pushes it to your device.

This process bypasses the App Store while staying within Apple’s security framework.

3. Convenience of .ipa Files

- .ipa files are the standard format for iOS apps. Having the .ipa file lets users distribute apps privately or access apps that are no longer on the App Store.
- Developers often provide .ipa files for beta testing or for apps that cannot be published on the App Store due to policy restrictions.

4. Free Sideloading for Limited Apps

Apple allows free Apple Developer accounts to sideload up to three active apps (with a limited number of re-signings). Building an .ipa is necessary to take advantage of this.

5. It's convenient

The tool helps you build no-code-sign ipa without typing script.

## How to use it

### With CLI
<video width="320" height="240" controls>
  <source src="https://cloud-3amv5qe3f-hack-club-bot.vercel.app/0screen_shot_2024-12-07_at_6.14.46___pm.mp4" type="video/mp4">
</video>

1. Open mac terminal app
2. Enter command below and make sure `{your app.command path}` is path of app.command:
   ```shell=
   chmod +x {your app.command path}
   ```
3. Double-click `app.command`
4. Enter your flutter project root directory
5. Enter output directory (iCloud is best choice)
6. The program will build your project and convert it to ipa
7. Open the file on your iphone and share with altstore

### With GUI

1. Clone the Repo

```bash
git clone https://github.com/ycy-0510/turn_app_into_ipa_for_flutter.git
```

2. Enter command below and make sure `{your gui-app.command path}` is path of app.command:
   ```shell=
   chmod +x {your gui-app.command path}
   ```
3. Double-click `gui-app.command`

---

Or Run the app with python

```bash
source .venv/bin/activate
pip3 install -r requirements.txt
python3 app.py
```
## Next Step
I'll build it into an app that you can just install and run!

## How to Contribute
Thank you for your interest in contributing to this project! Here are some ways you can contribute:

1. Report Issues:

- If you find any bugs or have suggestions for improvements, please create an issue on GitHub.
2. Submit Pull Requests:

- Fork this repository and clone it to your local machine.
- Create a new branch for your changes.
- Commit your changes and push them to your branch.
- Create a pull request, describing your changes.

3. Improve Documentation:

- If you find any errors or areas for improvement in the documentation, feel free to submit a pull request to improve it.
4. Add New Features:

- If you have ideas for new features, please create an issue to discuss your ideas first.
- Once approved, you can start implementing and submit a pull request.
5. Testing:

- Help test existing and new features, and report any issues you find.
Thank you for your contributions!

## LICENSE
Copyright 2024 YCY
Licensed under the Apache License, Version 2.0 (the "License")