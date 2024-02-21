read -p "Enter flutter project root directory: " root
read -p "Enter output directory: " end
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
    echo "Runner.app does not exist.\nPlease run \"flutter build ipa --no-codesign\" to build the app first."
fi
read -p "Press enter to end the process."