import random
from datetime import datetime

def play_game_action(game):   
    """
    game은 quiz_game.py에서 QuizGame클래스를 game변수 넣었음. 그래서 그걸 받는 것임
    단. quiz_game.py모듈에서 QuizGame클래스를 보면 
    
        def play_game(self):
            play_game_action(self)
            
    이렇게 self로 QuizGame클래스를 주고 있는데 종복으로 주는 것이 아닌가란 위문이 생길 수 있음.
    하지만 self는 해당 클래스 내부에서만 사용되는 것으로 외부파일에서 접근하기 위해서는 명시적으로
    인자를 주어야 한다.
        
    """
    #1. 퀴즈 풀기
    
    # 1단계: 퀴즈 존재 여부 확인
    if not game.quizzes:     #game.quizzes가 비어 있으면( [], {}, "", 0, False, None)이면 False인데 앞에 not이 있으니 True가 되어 실행
        print("\n❌ 등록된 퀴즈가 없습니다")
        print("먼저 퀴즈를 추가해주세요.\n")
        return               #return은 현재 실행되고 있는 그 함수만 즉시 종료하는 것으로 if, for와 같은 (블록)문의 종료가 아님.
    
    # 2단계: 랜덤 퀴즈 선택
    quiz = random.choice(game.quizzes)   #random.choice(var)에서 var이 []자료에서 랜덤하게 값을 하나 뽑아 내는 함수  
    
    print("\n" + "="*50)
    print("🎮 퀴즈 풀기")
    print("="*50)
    
    # 3단계: 퀴즈 출력
    quiz.show()
    
    # 4단계: 사용자 입력(힌트 옵션 포함)
    print("\n💡 팁: 'h'를 입력하면 힌트를 볼 수 있습니다.")
    print(" 'q'를 입력하면 포기합니다.\n")
    
    user_input = input("👉 답을 입력하세요: ").strip()
    
    # 5단계: 포기 처리
    if user_input.lower() == 'q':
        print("\n⏭️  이 문제를 건너뜁니다.")
        print(f"정답은: {quiz.choices[quiz.anser]}\n")
        return
    
    # 6단계: 힌트 요청 처리
    if user_input.lower() == 'h':
        quiz.show_hint()
        user_input = input("👉 답을 입력하세요: ").strip()
        
    # 7단계: 입력값 검증 및 정수 변환 ⭐ 추가됨
    