@echo off
for /f %%i IN (D:\ping.txt) DO ping %%i -n 1 >>exping.txt
pause
