#!/usr/bin/env python3
"""
Text Analyzer MCP Server
AI 에이전트에서 답변 문자열의 글자 수를 체크하는 FastMCP 서버
"""

from fastmcp import FastMCP
from typing import Dict, Any
import re
import unicodedata

# MCP 서버 인스턴스 생성
mcp = FastMCP("Text Analyzer Server")

@mcp.tool()
def count_characters(text: str, include_spaces: bool = True) -> Dict[str, Any]:
    """
    텍스트의 글자 수를 계산합니다.
    
    Args:
        text: 분석할 텍스트
        include_spaces: 공백을 포함할지 여부 (기본값: True)
    
    Returns:
        Dict containing character count analysis
    """
    if not text:
        return {
            "total_characters": 0,
            "characters_without_spaces": 0,
            "spaces_count": 0,
            "text_length": 0
        }
    
    total_chars = len(text)
    chars_without_spaces = len(text.replace(" ", ""))
    spaces_count = text.count(" ")
    
    result = {
        "total_characters": total_chars,
        "characters_without_spaces": chars_without_spaces,
        "spaces_count": spaces_count,
        "text_length": total_chars,
        "include_spaces_setting": include_spaces,
        "final_count": total_chars if include_spaces else chars_without_spaces
    }
    
    return result

@mcp.tool()
def count_words(text: str) -> Dict[str, Any]:
    """
    텍스트의 단어 수를 계산합니다.
    
    Args:
        text: 분석할 텍스트
    
    Returns:
        Dict containing word count analysis
    """
    if not text:
        return {
            "word_count": 0,
            "unique_words": 0,
            "average_word_length": 0.0
        }
    
    # 단어 분리 (공백, 구두점 기준)
    words = re.findall(r'\b\w+\b', text.lower())
    unique_words = set(words)
    
    avg_length = sum(len(word) for word in words) / len(words) if words else 0
    
    return {
        "word_count": len(words),
        "unique_words": len(unique_words),
        "average_word_length": round(avg_length, 2)
    }

@mcp.tool()
def analyze_character_types(text: str) -> Dict[str, Any]:
    """
    텍스트의 문자 타입별 분석을 수행합니다.
    
    Args:
        text: 분석할 텍스트
    
    Returns:
        Dict containing character type analysis
    """
    if not text:
        return {
            "alphabetic": 0,
            "numeric": 0,
            "spaces": 0,
            "punctuation": 0,
            "korean": 0,
            "english": 0,
            "special_characters": 0
        }
    
    counts = {
        "alphabetic": 0,
        "numeric": 0,
        "spaces": 0,
        "punctuation": 0,
        "korean": 0,
        "english": 0,
        "special_characters": 0
    }
    
    for char in text:
        if char.isspace():
            counts["spaces"] += 1
        elif char.isalpha():
            counts["alphabetic"] += 1
            # 한글 문자 체크
            if '\uac00' <= char <= '\ud7af':
                counts["korean"] += 1
            elif char.isascii():
                counts["english"] += 1
        elif char.isnumeric():
            counts["numeric"] += 1
        elif unicodedata.category(char).startswith('P'):
            counts["punctuation"] += 1
        else:
            counts["special_characters"] += 1
    
    return counts

@mcp.tool()
def get_text_statistics(text: str) -> Dict[str, Any]:
    """
    텍스트의 종합적인 통계 정보를 제공합니다.
    
    Args:
        text: 분석할 텍스트
    
    Returns:
        Dict containing comprehensive text statistics
    """
    char_stats = count_characters(text)
    word_stats = count_words(text)
    type_stats = analyze_character_types(text)
    
    # 줄 수 계산
    lines = text.split('\n')
    line_count = len(lines)
    non_empty_lines = len([line for line in lines if line.strip()])
    
    # 문장 수 계산 (간단한 방식)
    sentences = re.split(r'[.!?]+', text)
    sentence_count = len([s for s in sentences if s.strip()])
    
    return {
        "character_analysis": char_stats,
        "word_analysis": word_stats,
        "character_types": type_stats,
        "line_count": line_count,
        "non_empty_lines": non_empty_lines,
        "sentence_count": sentence_count,
        "text_preview": text[:100] + "..." if len(text) > 100 else text
    }

@mcp.tool()
def check_text_length_limit(text: str, max_length: int = 1000) -> Dict[str, Any]:
    """
    텍스트가 지정된 길이 제한을 초과하는지 확인합니다.
    
    Args:
        text: 검사할 텍스트
        max_length: 최대 허용 길이 (기본값: 1000)
    
    Returns:
        Dict containing length check results
    """
    current_length = len(text)
    is_within_limit = current_length <= max_length
    excess_chars = max(0, current_length - max_length)
    remaining_chars = max(0, max_length - current_length)
    
    return {
        "current_length": current_length,
        "max_length": max_length,
        "within_limit": is_within_limit,
        "excess_characters": excess_chars,
        "remaining_characters": remaining_chars,
        "percentage_used": round((current_length / max_length) * 100, 2) if max_length > 0 else 0
    }

# 리소스 정의
@mcp.resource("file://help")
def get_help() -> str:
    """
    텍스트 분석기 사용법 도움말을 제공합니다.
    """
    return """
    Text Analyzer MCP Server 도움말
    
    사용 가능한 도구:
    1. count_characters(text, include_spaces) - 글자 수 계산
    2. count_words(text) - 단어 수 계산
    3. analyze_character_types(text) - 문자 타입별 분석
    4. get_text_statistics(text) - 종합 통계 정보
    5. check_text_length_limit(text, max_length) - 길이 제한 검사
    
    예시:
    - count_characters("안녕하세요 Hello!", True)
    - get_text_statistics("분석할 텍스트를 입력하세요.")
    - check_text_length_limit("텍스트", 100)
    """

if __name__ == "__main__":
    # 서버 실행
    mcp.run()