@echo off
color 0A
echo Remember to add /upload to the end of the ngrok server URL (forwarding)
pause

ngrok.exe authtoken ::your ngrok token
ngrok.exe http 5000