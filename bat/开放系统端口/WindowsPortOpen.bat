@echo off
color 0a
echo support Windows 2003 2008 2008R2 2012 2012R2 7 8 10
echo the method is by Firewall and reg and need system authority and ned restart the system
set /p c=port:
if "%c%"=="" goto end
goto edit
:edit
netsh advfirewall firewall add rule name="Remote PortNumber" dir=in action=allow protocol=TCP localport="%c%"
netsh advfirewall firewall add rule name="Remote PortNumber" dir=in action=allow protocol=TCP localport="%c%"
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\Wds\rdpwd\Tds\tcp" /v "PortNumber" /t REG_DWORD /d "%c%" /f
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v "PortNumber" /t REG_DWORD /d "%c%" /f
echo ok
pause
exit
:end
echo fail
pause
