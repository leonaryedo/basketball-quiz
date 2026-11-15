import json
import time
import sys
from quiz import Quiz

def measure_performance(file_name):
    print(f"\n--- [{file_name}] 테스트 시작 ---")
    
    # 1. 파일 읽기 및 JSON 파싱 시간 측정
    start_time = time.time()
    with open(file_name, "r", encoding="utf-8") as f:
        data = json.load(f)
    load_end_time = time.time()
    
    # 2. 딕셔너리를 Quiz 객체로 변환하는 시간 측정
    quizzes = [Quiz(q["question"], q["choices"], q["answer"]) for q in data["quizzes"]]
    conversion_end_time = time.time()
    
    # 결과 출력
    print(f"파일 로딩 시간: {load_end_time - start_time:.5f}초")
    print(f"객체 변환 시간: {conversion_end_time - load_end_time:.5f}초")
    print(f"총 소요 시간: {conversion_end_time - start_time:.5f}초")
    print(f"메모리 내 객체 개수: {len(quizzes)}개")
    
    # 3. 메모리 점유율 대략적 확인 (바이트 단위)
    print(f"데이터 리스트 크기: {sys.getsizeof(quizzes)} bytes")

# 두 파일 비교 실행
try:
    measure_performance("state_5.json")    # 문제 5개 파일
    measure_performance("state_1000.json") # 문제 1000개 파일
except FileNotFoundError as e:
    print(f"파일을 찾을 수 없습니다: {e}")