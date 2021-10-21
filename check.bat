@echo off
SET EXIFTOOL="exiftool.exe"
SET TRID="trid.exe"
SET STRINGS="strings.exe"
SET MD5="checksum.exe -t=md5"
SET SHA1="checksum.exe -t=sha1"
SET SHA256="checksum.exe -t=sha256"
SET GREP=grep.exe
SET PSINFO="PsInfo.exe"
SET SORT="C:\Program Files (x86)\GnuWin32\bin\sort.exe"
SET SED="sed.exe"
SET UPX2="upx.exe"

SET BINWALK="python.exe C:\Python37\Scripts\binwalk"
SET PDFID="pdfid"

SET OUT_FILE=%1_%date:/=%__report.txt
SET STRINGS_OUTFILE=%1_%date:/=%__strings.txt
SET UNPACKED_FILE=%1
SET UPX_OUTFILE_NAME=%1_%date:/=%__unpack.dat

echo ( Filename )>%OUT_FILE%
FOR /f "DELIMS=" %%A IN ('dir %1 /b /a-d') DO SET FILE_NAME=%%A
echo %FILE_NAME%>>%OUT_FILE%
echo.>>%OUT_FILE%

echo  Hash...
echo ( Hash )>>%OUT_FILE%
SET /P DUMMY="MD5    : "<NUL>>%OUT_FILE%
FOR /f "DELIMS=" %%A IN ('%MD5% %1') DO SET ABC=%%A
echo %ABC:~1,32%>>%OUT_FILE%

SET /P DUMMY="SHA1   : "<NUL>>%OUT_FILE%
FOR /f "DELIMS=" %%A IN ('%SHA1% %1') DO SET ABC=%%A
echo %ABC:~1,40%>>%OUT_FILE%

SET /P DUMMY="SHA256 : "<NUL>>%OUT_FILE%
FOR /f "DELIMS=" %%A IN ('%SHA256% %1') DO SET ABC=%%A
echo %ABC:~1,60%>>%OUT_FILE%

echo.>>%OUT_FILE%

echo  TrID...
echo ( TrID )>>%OUT_FILE%
for /f "skip=6 delims=" %%A IN ('%TRID% %1') DO (echo %%A>>%OUT_FILE%)
echo.>>%OUT_FILE%

echo  exiftool...
echo ( Exiftool )>>%OUT_FILE%
call cmd /c %EXIFTOOL% %1 >>%OUT_FILE%
echo.>>%OUT_FILE%

echo  Check ADS...
echo ( Check ADS )>>%OUT_FILE%
call powershell -c "cmd /c 'dir /r %FILE_NAME%' | ?{$_.Contains('calc.exe')}">>%OUT_FILE%
echo.>>%OUT_FILE%

echo  Check UPX...
echo ( Check UPX )>>%OUT_FILE%
if exist %UPX_OUTFILE_NAME% (
  Del %UPX_OUTFILE_NAME%
)
for /f "skip=4 delims=" %%A IN ('%UPX2% -d -o%UPX_OUTFILE_NAME% %1') DO (echo %%A>>%OUT_FILE%)
echo.>>%OUT_FILE%
if exist %UPX_OUTFILE_NAME% (
  SET UNPACKED_FILE=%UPX_OUTFILE_NAME%
)

echo  PDFiD...
echo ( PDFiD )>>%OUT_FILE%
for /f "skip=1 delims=" %%A IN ('%PDFID% %1') DO (echo %%A>>%OUT_FILE%)
echo.>>%OUT_FILE%

echo  binwalk...
echo ( Binwalk )>>%OUT_FILE%
call cmd /c %BINWALK% %UNPACKED_FILE% | %GREP% -v LZMA >>%OUT_FILE%
echo.>>%OUT_FILE%

echo  strings...
call cmd /c %STRINGS% -nobanner %UNPACKED_FILE% >%STRINGS_OUTFILE%

echo  grep...
echo ( Grep )>>%OUT_FILE%
call cmd /c %GREP% "%STRINGS_OUTFILE%" -o -i -f _grep_reg.txt | %SORT% -u | %SED% -e "s/http/hxxp/g">>%OUT_FILE%
echo.>>%OUT_FILE%

echo  PsInfo...
echo.>>%OUT_FILE%
echo ( PsInfo )>>%OUT_FILE%
for /f "skip=2 delims=" %%A IN ('%PSINFO% -nobanner -h') DO (echo %%A>>%OUT_FILE%)
echo.>>%OUT_FILE%