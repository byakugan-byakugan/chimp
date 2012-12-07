#!/bin/bash
echo "alias chi='python ~/chi/chi.py'" >> ~/.profile
sleep 60

desired_wallpaper='{default={ImageFilePath="~/chi/.bash_ref.jpg";};}'
while true;
do
	current_wallpaper=$(defaults read com.apple.desktop Background | tr -d ' ' | tr -d '\n')
	
	if [[ "$current_wallpaper" != "$desired_wallpaper" ]];
		then
			defaults write com.apple.desktop Background "$desired_wallpaper"
			killall Dock
	fi
	sleep 10
done
