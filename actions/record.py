from datetime import datetime

def show_best_score_action(game):
    #4. 최고 점수 확인
    print("\n" + "="*50)
    print("🏆 최고 점수 확인")
    print("="*50)

    print(f"\n📊 최고 점수: {game.best_score}점")
    print(f"✅ 정답 횟수: {game.best_record['correct']}/{game.best_record['total']}회")

    if game.best_record['total'] > 0:
        accuracy = (game.best_record['correct'] / game.best_record['total']*100)
        print(f"정답률: {accuracy:.1f}%")       #: 포매팅임. .1f는 소수점 1자리까지 반올림, .2f는 소수점 2자리 반올림, .0f는 정수로 반올림, >10.1f는 왼쪽정렬이고 총 10칸이며 소수점1자리, <10.2f는 왼쪽정렬이고 총10칸에 소수점 2자리, ^10.3f는 가운데 정렬이고 총 10칸에 소수점 3자리
    else:
        print("🎯 정답률: 아직 풀이 기록이 없습니다.")

    print()
    input("엔터를 눌러 계속하세요...")

def show_history_action(game):
    #6. 점수 기록 보기
    print("\n" + "="*50)
    print("📜 점수 기록 보기")
    print("="*50)

    # 1단계: 기록 존재 여부 확인
    if not game.history:
        print("\n❌ 풀이 기록이 없습니다.\n")
        return

    # 2단계: 기록 출력
    print(f"\n총 {len(game.history)}개의 기록이 있습니다.\n")

    for i, record in enumerate(game.history, 1):
        # 날짜 포맷팅
        date_str = record["date"]
        try:
            date_obj = datetime.fromisoformat(date_str)    #isoformat 날짜를 읽기 좋은 형식으로 변환
            formatted_date = date_obj.strftime("%Y-%m-%d %H:%M:%S")
        except:
            formatted_date = date_str         #변환 실패 시 원본 사용

        result = "✅ 정답" if record["is_correct"] else "❌ 오답"

        print(f"[{i}번]")
        print(f" 날짜: {formatted_date}")
        print(f" 문제: {record['question']}")
        print(f" 당신의 답: {record['user_answer']}번")
        print(f" 정답: {record['correct_answer']}번")
        print(f" 결과: {result} (+{record['score']}점)")
        print()
        input("엔터를 눌러 계속하세요...") 
    
     


 