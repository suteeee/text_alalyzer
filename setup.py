#!/usr/bin/env python3
"""
Text Analyzer MCP Server 설치 스크립트
"""

import subprocess
import sys
import os

def create_virtual_environment():
    """가상환경 생성"""
    print("해결: 가상환경 생성 중...")
    try:
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print("✓ 가상환경이 성공적으로 생성되었습니다.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ 가상환경 생성에 실패했습니다: {e}")
        return False

def get_pip_path():
    """가상환경의 pip 경로 반환"""
    if os.name == 'nt':  # Windows
        return os.path.join("venv", "Scripts", "pip")
    else:  # macOS/Linux
        return os.path.join("venv", "bin", "pip")

def install_dependencies():
    """의존성 설치"""
    print("현재: 의존성 설치 중...")
    pip_path = get_pip_path()
    
    try:
        # pip 업그레이드
        subprocess.run([pip_path, "install", "--upgrade", "pip"], check=True)
        
        # requirements.txt 설치
        subprocess.run([pip_path, "install", "-r", "requirements.txt"], check=True)
        
        print("✓ 의존성이 성공적으로 설치되었습니다.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ 의존성 설치에 실패했습니다: {e}")
        return False

def test_installation():
    """설치 테스트"""
    print("체크: 설치 테스트 중...")
    pip_path = get_pip_path()
    
    try:
        # fastmcp 설치 확인
        result = subprocess.run([pip_path, "show", "fastmcp"], 
                              capture_output=True, text=True, check=True)
        
        if "Name: fastmcp" in result.stdout:
            print("✓ FastMCP가 올바르게 설치되었습니다.")
            return True
        else:
            print("✗ FastMCP 설치를 확인할 수 없습니다.")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"✗ 설치 테스트에 실패했습니다: {e}")
        return False

def print_activation_instructions():
    """가상환경 활성화 도움말 출력"""
    print("\n🚀 설치가 완료되었습니다!")
    print("\n다음 단계:")
    print("1. 가상환경 활성화:")
    
    if os.name == 'nt':  # Windows
        print("   venv\\Scripts\\activate")
    else:  # macOS/Linux
        print("   source venv/bin/activate")
    
    print("\n2. 서버 실행:")
    print("   # 개발 모드 (권장)")
    print("   fastmcp dev text_analyzer_server.py")
    print("")
    print("   # 또는 직접 실행")
    print("   python text_analyzer_server.py")
    
    print("\n3. AI 클라이언트 연결:")
    print("   README.md 파일의 '설치 및 실행' 섹션을 참조하세요.")

def main():
    print("🎉 Text Analyzer MCP Server 설치 시작!")
    print("="*50)
    
    # 현재 디렉토리 확인
    print(f"작업 디렉토리: {os.getcwd()}")
    
    # 필수 파일 확인
    required_files = ['text_analyzer_server.py', 'requirements.txt']
    missing_files = [f for f in required_files if not os.path.exists(f)]
    
    if missing_files:
        print(f"✗ 필수 파일이 누락되었습니다: {missing_files}")
        print("올바른 디렉토리에서 실행해주세요.")
        return False
    
    # 가상환경 생성
    if not create_virtual_environment():
        return False
    
    # 의존성 설치
    if not install_dependencies():
        return False
    
    # 설치 테스트
    if not test_installation():
        return False
    
    # 완료 메시지
    print_activation_instructions()
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
