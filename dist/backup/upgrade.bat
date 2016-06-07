@echo OFF

taskkill /f /im auto_car.exe

XCOPY %cd% %cd%\backup\ /y
xcopy .\help .\backup\help\ /y
xcopy .\icon .\backup\icon\ /y