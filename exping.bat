@echo off
for /f %%i IN (D:\ping.txt) DO ping %%i -n 1 >>exping.txt
for /f %%i IN (D:\ping.txt) DO systeminfo /s %%i >%%i.txt
pause
