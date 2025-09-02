# Text Analyzer MCP Server

AI 에이전트에서 답변 문자열의 글자 수를 체크하는 FastMCP 서버입니다.

## 기능

### 주요 도구 (Tools)

1. **count_characters(text, include_spaces)** - 글자 수 계산
   - 전체 글자 수
   - 공백 제외 글자 수
   - 공백 개수
   - 설정에 따른 최종 글자 수

2. **count_words(text)** - 단어 수 계산
   - 총 단어 수
   - 고유 단어 수
   - 평균 단어 길이

3. **analyze_character_types(text)** - 문자 타입별 분석
   - 알파벳, 숫자, 공백, 구두점
   - 한글, 영어, 특수문자 분류

4. **get_text_statistics(text)** - 종합 통계 정보
   - 문자, 단어, 줄, 문장 수
   - 문자 타입별 분석
   - 텍스트 미리보기

5. **check_text_length_limit(text, max_length)** - 길이 제한 검사
   - 현재 길이와 제한 비교
   - 초과/잔여 문자 수
   - 사용률 백분율

### 리소스

- **text_analyzer://help** - 사용법 도움말

## 설치 및 실행

### 1. 환경 설정

```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 의존성 설치
pip install -r requirements.txt
```

### 2. 서버 실행

#### 개발 모드 (권장)
```bash
# MCP Inspector와 함께 실행 (브라우저에서 테스트 가능)
fastmcp dev text_analyzer_server.py
```

#### 직접 실행
```bash
# Python으로 직접 실행
python text_analyzer_server.py

# 또는 FastMCP CLI 사용
fastmcp run text_analyzer_server.py
```

### 3. AI 클라이언트와 연결

#### Claude Desktop 설정
`claude_desktop_config.json` 파일에 다음을 추가:

```json
{
  "mcpServers": {
    "text_analyzer": {
      "command": "python",
      "args": ["/path/to/text_analyzer_server.py"]
    }
  }
}
```

#### VS Code/Cursor 설정
`.vscode/mcp.json` 또는 `.cursor/mcp.json` 파일 생성:

```json
{
  "servers": {
    "text_analyzer": {
      "type": "stdio",
      "command": "python",
      "args": ["/path/to/text_analyzer_server.py"]
    }
  }
}
```

## 사용 예시

### 기본 글자 수 세기
```python
# AI 에이전트에서 사용 예시
# "안녕하세요 Hello World!"의 글자 수를 계산해주세요.

count_characters("안녕하세요 Hello World!", True)
# 결과: 
# {
#   "total_characters": 18,
#   "characters_without_spaces": 16,
#   "spaces_count": 2,
#   "final_count": 18
# }
```

### 종합 텍스트 분석
```python
get_text_statistics("안녕하세요! 이것은 테스트 텍스트입니다.")
# 한글, 영어, 구두점 등 상세 분석 결과 제공
```

### 글자 수 제한 검사
```python
check_text_length_limit("분석할 텍스트", 100)
# 100자 제한에서 현재 사용량과 잔여량 확인
```

## 개발자 정보

이 MCP 서버는 FastMCP 프레임워크를 사용하여 개발되었습니다.

### 주요 특징
- 한글과 영어 텍스트 모두 지원
- 다양한 문자 타입 분석
- 유니코드 완전 지원
- 실시간 텍스트 통계 제공

### 확장 가능성
- 텍스트 감정 분석
- 언어 자동 감지
- 가독성 점수 계산
- 키워드 추출

## 문제 해결

### 자주 발생하는 문제

1. **모듈을 찾을 수 없음**: 가상환경이 활성화되었는지 확인
2. **포트 충돌**: 다른 MCP 서버가 실행 중인지 확인
3. **권한 문제**: Python 실행 권한 확인

### 로그 확인
```bash
# 디버그 모드로 실행
fastmcp dev text_analyzer_server.py --verbose
```

## 라이선스

MIT License

## 기여

버그 리포트나 기능 요청은 GitHub Issues를 통해 제출해주세요.
