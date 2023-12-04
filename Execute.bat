@echo off
setlocal enabledelayedexpansion

:: Obt�m o caminho completo do arquivo .bat
set "BAT_DIR=%~dp0"

:: Exibe o caminho
echo O arquivo .bat est� localizado em: %BAT_DIR%

echo "Starting robot Python"
python "%BAT_DIR%\Bot.py"
pause

endlocal
