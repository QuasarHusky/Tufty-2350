ffmpeg -y -i %1 -frames 1 -q:v 2 -filter_complex "fps=30,tile=12x16,scale=1920:1920" ./out.png
pause