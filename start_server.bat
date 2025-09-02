@echo off
chcp 65001 >nul
setlocal EnableDelayedExpansion

REM Text Analyzer MCP Server 시작 스크립트
REM Windows용

echo 🚀 Text Analyzer MCP Server 시작!
echo ==================================================

REM 현재 디렉토리 확인
echo 작업 디렉토리: %cd%

REM 가상환경 확인
if not exist "venv" (
    echo ❌ 가상환경을 찾을 수 없습니다.
    echo setup.py를 먼저 실행해주세요: python setup.py
    pause
    exit /b 1
)

REM 가상환경 활성화
echo 🔧 가상환경 활성화 중...
call venv\Scripts\activate.bat

REM FastMCP 설치 확인
fastmcp version >nul 2>&1
if errorlevel 1 (
    echo ❌ FastMCP를 찾을 수 없습니다.
    echo setup.py를 다시 실행해주세요: python setup.py
    pause
    exit /b 1
)

REM 서버 파일 확인
if not exist "text_analyzer_server.py" (
    echo ❌ text_analyzer_server.py 파일을 찾을 수 없습니다.
    pause
    exit /b 1
)

echo ✅ 모든 준비 완료!
echo.
echo 📡 MCP 서버를 시작합니다...
echo 브라우저가 자동으로 열리면 MCP Inspector에서 테스트할 수 있습니다.
echo 종료하려면 Ctrl+C를 누르세요.
echo.

REM MCP 개발 서버 시작 (Inspector와 함께)
fastmcp dev text_analyzer_server.py

REM 스크립트 종료시 일시정지
if errorlevel 1 (
    echo.
    echo ❌ 서버 실행 중 오류가 발생했습니다.
    pause
)
