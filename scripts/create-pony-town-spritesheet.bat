ffmpeg -y -i %1 -frames 1 -q:v 2 -filter_complex "fps=30,crop=552:624:672:178,tile=100x1,scale=6900:78:flags=neighbor" ./out.png
pause