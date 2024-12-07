# Build Flutter IPA for Altstore

## Why you need to use it

1. Free Installation of Apps Without Jailbreaking

AltStore uses Apple’s Developer program mechanism to sideload apps without requiring a jailbreak. This makes it an attractive option for users who want to run non-App Store apps for free while keeping their devices secure.

2. How AltStore Works with .ipa Files

AltStore works by signing and installing .ipa files (iOS app packages). To install an app through AltStore:
-	You need a valid .ipa file for the app you want.
-	AltStore re-signs the .ipa using your Apple ID and pushes it to your device.

This process bypasses the App Store while staying within Apple’s security framework.

3. Convenience of .ipa Files
-	.ipa files are the standard format for iOS apps. Having the .ipa file lets users distribute apps privately or access apps that are no longer on the App Store.
-	Developers often provide .ipa files for beta testing or for apps that cannot be published on the App Store due to policy restrictions.

4. Free Sideloading for Limited Apps

Apple allows free Apple Developer accounts to sideload up to three active apps (with a limited number of re-signings). Building an .ipa is necessary to take advantage of this.

5. It's convinient 

The tool helps you build no-code-sign ipa without typing script.

## How to use it

### With Cli

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
1. Download the app
2. Run the app