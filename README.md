# vocalize_ros

sudo apt install espeak-ng

Terminal Example: espeak-ng "Hello. World." -v zh-yue -p 90 -a 150 -g 15 -s 150 -x

-Setting Specific Audio Device-

pactl list short sinks

alsamixer

pacmd list-sinks for name or index number of possible sinks

pacmd list-sources for name or index number of possible sources

pacmd set-default-sink "SINKNAME" | index to set the default output sink

-Possible Requirements-

sudo apt install pulseaudio-utils

sudo apt install alsamixer
