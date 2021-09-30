@echo off
rem 【argv1】は時間、【argv2】は加算／減算する時間（分単位）

set argv1=21:02
set argv2=-3
set argv3=3 
if "%argv1:~0,1%" EQU "0" (set /a HOUR=%argv1:~1,1%) else (set /a HOUR=%argv1:~0,2%)
set /a MINUTE=%argv1:~-2,2%
echo MINUTE by %MINUTE%
echo HOUR by %HOUR%
set /a MINTOTAL=HOUR*60+MINUTE+argv2
set /a MAXTOTAL=HOUR*60+MINUTE+argv3
echo MINTOTAL %MINTOTAL% MAXTOTAL %MAXTOTAL%

if %MINTOTAL% LSS 0 set /a MINTOTAL+=((-MINTOTAL/1440+1)*1440)
set /a MINTOTAL%%=1440
set /a HOUR=MINTOTAL / 60
set /a MINUTE=MINTOTAL %% 60

if %MINUTE% LSS 10 set MINUTE=0%MINUTE%
if %HOUR% LSS 10 set HOUR=0%HOUR%

set RESULT=%HOUR%:%MINUTE%
echo %RESULT%

if %MAXTOTAL% LSS 0 set /a MAXTOTAL+=((-MAXTOTAL/1440+1)*1440)
set /a MAXTOTAL%%=1440
set /a HOUR2=MAXTOTAL / 60
set /a MINUTE2=MAXTOTAL %% 60

if %MINUTE2% LSS 10 set MINUTE2=0%MINUTE2%
if %HOUR2% LSS 10 set HOUR2=0%HOUR2%

set RESULT2=%HOUR2%:%MINUTE2%
echo %RESULT2%
pause