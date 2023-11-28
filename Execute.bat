@echo off
setlocal enabledelayedexpansion

:: Obtém o caminho completo do arquivo .bat
set "BAT_DIR=%~dp0"

:: Exibe o caminho
echo O arquivo .bat está localizado em: %BAT_DIR%

echo "Starting robot Python"
python "%BAT_DIR%\bot.py"
pause

endlocal
