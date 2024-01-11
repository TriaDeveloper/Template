@echo off
setlocal enabledelayedexpansion

:: Obtem o caminho completo do arquivo .bat do bot
set "BAT_DIR=%~dp0"

:: Exibe o caminho
echo O arquivo .bat esta localizado em: %BAT_DIR%

echo "Starting robot Python"
python "%BAT_DIR%\Bot.py"
pause

endlocal
