echo "\033[1;34mThis tool helps you convert a Flutter project into an IPA file.\033[0m"
echo "\033[1;34mYou will be prompted to enter the root directory of your Flutter project and the output directory for the IPA file.\033[0m"

read -p "Enter flutter project root directory: " root
read -p "Enter output directory: " end
cd "$root"
flutter build ipa --no-codesign
file="$root/build/ios/archive/Runner.xcarchive/Products/Applications/Runner.app"
if [ -d "$file" ]; then
    cd "$end"
    mkdir -p Payload
    cp -r $file Payload/
    zip -qr Payload.zip Payload/*
    mv Payload.zip app.ipa
    rm -rf Payload
    echo "app.ipa is created successfully. You can check it out in $end ."
else
    echo "Runner.app does not exist."
fi
read -p "Press enter to end the process."
