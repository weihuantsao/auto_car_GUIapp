@echo OFF
set /p old_ver=<current_version.ini

wget -N http://140.92.39.230:9527/tsao_file_system/new_version.txt --no-verbose --quiet
set /p new_ver=<new_version.txt

REM echo %old_ver%
REM echo %new_ver%
if %old_ver% EQU %new_ver% GOTO _DONE
if %old_ver% NEQ  %new_ver% GOTO _UPDATE

:_DONE 
echo This is the latest version.
rem  new_version.txt 
rem pause
exit

:_UPDATE
echo Find new_version : %new_ver%
rem wget -N http://140.92.39.230:9527/file.txt --no-verbose
rem @echo %new_ver% > current_version.ini
del new_version.txt
rem start file.txt
exit