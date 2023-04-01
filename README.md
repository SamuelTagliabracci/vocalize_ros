# Description

Creates a /vocalize topic that you can publish string data to. String data will be converted TTS and vocalized.

# Install

sudo apt install espeak-ng

# Install Additional Languages (MBROLA)

sudo apt-cache search mbrola

sudo apt install mbrola mbrola-us1 mbrola-us2 mbrola-us3

# Test

espeak-ng "Hello. World." -v zh-yue -p 90 -a 150 -g 15 -s 150 -x

espeak-ng "Hello. World. I am mbrola voice US3" -v mb-us3 -p 90 -a 150 -g 15 -s 150 -x

# List Languages

espeak-ng --voices

# Volume Control

pacmd set-sink-volume index volume

pacmd set-source-volume index volume for volume control (65536 = 100 %, 0 = mute; or a bit more intuitive 0x10000 = 100 %, 0x7500 = 75 %, 0x0 = 0 %)

# Config Setting Specific Audio Device

pactl list short sinks

alsamixer

pacmd list-sinks for name or index number of possible sinks

pacmd list-sources for name or index number of possible sources

pacmd set-default-sink "SINKNAME" | index to set the default output sink

-Possible Requirements-

sudo apt install pulseaudio-utils

sudo apt install alsamixer
