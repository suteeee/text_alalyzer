#!/bin/bash

# Text Analyzer MCP Server 시작 스크립트
# macOS/Linux용

echo "🚀 Text Analyzer MCP Server 시작!"
echo "=" | awk '{for(i=1;i<=50;i++) printf "%s", $0; print ""}'  # 50개의 = 출력

# 현재 디렉토리 확인
echo "작업 디렉토리: $(pwd)"

# 가상환경 활성화 확인
if [ ! -d "venv" ]; then
    echo "❌ 가상환경을 찾을 수 없습니다."
    echo "setup.py를 먼저 실행해주세요: python setup.py"
    exit 1
fi

# 가상환경 활성화
echo "🔧 가상환경 활성화 중..."
source venv/bin/activate

# FastMCP 설치 확인
if ! command -v fastmcp &> /dev/null; then
    echo "❌ FastMCP를 찾을 수 없습니다."
    echo "setup.py를 다시 실행해주세요: python setup.py"
    exit 1
fi

# 서버 파일 확인
if [ ! -f "text_analyzer_server.py" ]; then
    echo "❌ text_analyzer_server.py 파일을 찾을 수 없습니다."
    exit 1
fi

echo "✅ 모든 준비 완료!"
echo ""
echo "📡 MCP 서버를 시작합니다..."
echo "브라우저가 자동으로 열리면 MCP Inspector에서 테스트할 수 있습니다."
echo "종료하려면 Ctrl+C를 누르세요."
echo ""

# MCP 개발 서버 시작 (Inspector와 함께)
fastmcp dev text_analyzer_server.py
