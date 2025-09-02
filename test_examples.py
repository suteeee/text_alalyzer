#!/usr/bin/env python3
"""
Text Analyzer MCP Server 테스트 예시
서버의 기능들을 테스트하는 예시 스크립트
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

from text_analyzer_server import (
    count_characters,
    count_words,
    analyze_character_types,
    get_text_statistics,
    check_text_length_limit
)

def test_basic_character_counting():
    """기본 글자 수 세기 테스트"""
    print("📊 기본 글자 수 세기 테스트")
    print("-" * 40)
    
    test_text = "안녕하세요 Hello World!"
    result = count_characters(test_text, include_spaces=True)
    
    print(f"테스트 텍스트: '{test_text}'")
    print(f"전체 글자 수: {result['total_characters']}")
    print(f"공백 제외: {result['characters_without_spaces']}")
    print(f"공백 개수: {result['spaces_count']}")
    print(f"최종 개수: {result['final_count']}")
    print()

def test_word_counting():
    """단어 수 세기 테스트"""
    print("📊 단어 수 세기 테스트")
    print("-" * 40)
    
    test_text = "안녕하세요! 이것은 테스트 텍스트입니다. Hello world!"
    result = count_words(test_text)
    
    print(f"테스트 텍스트: '{test_text}'")
    print(f"단어 수: {result['word_count']}")
    print(f"고유 단어: {result['unique_words']}")
    print(f"평균 단어 길이: {result['average_word_length']}")
    print()

def test_character_type_analysis():
    """문자 타입 분석 테스트"""
    print("📊 문자 타입 분석 테스트")
    print("-" * 40)
    
    test_text = "안녕123! Hello@World#"
    result = analyze_character_types(test_text)
    
    print(f"테스트 텍스트: '{test_text}'")
    for char_type, count in result.items():
        print(f"{char_type}: {count}")
    print()

def test_comprehensive_statistics():
    """종합 통계 테스트"""
    print("📊 종합 통계 테스트")
    print("-" * 40)
    
    test_text = """안녕하세요!
이것은 여러 줄로 된 테스트입니다.
Hello World!
테스트가 완료되었습니다."""
    
    result = get_text_statistics(test_text)
    
    print(f"테스트 텍스트 미리보기:")
    print(f"'{result['text_preview']}'")
    print(f"줄 수: {result['line_count']}")
    print(f"비어있지 않은 줄: {result['non_empty_lines']}")
    print(f"문장 수: {result['sentence_count']}")
    
    print("\n문자 분석:")
    char_analysis = result['character_analysis']
    print(f"  전체 글자: {char_analysis['total_characters']}")
    print(f"  공백 제외: {char_analysis['characters_without_spaces']}")
    
    print("\n단어 분석:")
    word_analysis = result['word_analysis']
    print(f"  단어 수: {word_analysis['word_count']}")
    print(f"  고유 단어: {word_analysis['unique_words']}")
    print()

def test_length_limit_check():
    """길이 제한 검사 테스트"""
    print("📊 길이 제한 검사 테스트")
    print("-" * 40)
    
    # 짧은 텍스트
    short_text = "짧은 텍스트"
    result1 = check_text_length_limit(short_text, 100)
    
    print(f"짧은 텍스트: '{short_text}'")
    print(f"  현재 길이: {result1['current_length']}")
    print(f"  제한 내: {result1['within_limit']}")
    print(f"  사용률: {result1['percentage_used']}%")
    print(f"  잔여: {result1['remaining_characters']}글자")
    
    # 긴 텍스트
    long_text = "긴 텍스트입니다. " * 20  # 20번 반복
    result2 = check_text_length_limit(long_text, 50)
    
    print(f"\n긴 텍스트 (최솈50자 제한):")
    print(f"  현재 길이: {result2['current_length']}")
    print(f"  제한 내: {result2['within_limit']}")
    print(f"  사용률: {result2['percentage_used']}%")
    print(f"  초과: {result2['excess_characters']}글자")
    print()

def test_edge_cases():
    """예외 상황 테스트"""
    print("📊 예외 상황 테스트")
    print("-" * 40)
    
    # 빈 문자열
    empty_result = count_characters("")
    print(f"빈 문자열 결과: {empty_result}")
    
    # 공백만 있는 문자열
    spaces_only = count_characters("   ")
    print(f"공백만: {spaces_only}")
    
    # 숫자만 있는 문자열
    numbers_only = analyze_character_types("12345")
    print(f"숫자만: {numbers_only}")
    
    # 특수문자만 있는 문자열
    special_only = analyze_character_types("!@#$%")
    print(f"특수문자만: {special_only}")
    print()

def main():
    """모든 테스트 실행"""
    print("🚀 Text Analyzer MCP Server 테스트 시작!")
    print("=" * 50)
    print()
    
    try:
        test_basic_character_counting()
        test_word_counting()
        test_character_type_analysis()
        test_comprehensive_statistics()
        test_length_limit_check()
        test_edge_cases()
        
        print("🎉 모든 테스트가 성공적으로 완료되었습니다!")
        print("\n이제 MCP 서버를 실행하여 AI 에이전트와 연결할 수 있습니다.")
        
    except Exception as e:
        print(f"✗ 테스트 중 오류 발생: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
