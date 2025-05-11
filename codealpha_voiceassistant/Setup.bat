@echo off
setlocal

echo ===============================
echo Checking if Python is installed...
echo ===============================

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python not found. Installing via winget...
    winget install --id Python.Python.3 --source winget --accept-package-agreements --accept-source-agreements
    echo Waiting for Python to become available...
    timeout /t 10 >nul
) else (
    echo Python is already installed.
)

echo.
echo ===============================
echo Upgrading pip...
echo ===============================
python -m pip install --upgrade pip

echo.
echo ===============================
echo Installing required Python packages...
echo ===============================
python -m pip install SpeechRecognition pyttsx3 wikipedia pyaudio
if %errorlevel% neq 0 (
    echo PyAudio installation failed. Trying fallback with pipwin...
    python -m pip install pipwin
    pipwin install pyaudio
)

echo.
echo ===============================
echo Running VoiceAssistant.py...
echo ===============================
python VoiceAssistant.py

echo.
echo Script finished. Press any key to exit...
pause >nul