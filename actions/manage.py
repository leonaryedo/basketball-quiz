from quiz import Quiz

def add_quiz_action(game):
    #2. 퀴즈 추가
    print("\n" + "="*50)
    print("➕ 퀴즈 추가")
    print("="*50)

    # 1단계: 문제 입력
    question = input("\n❓ 문제를 입력하세요: ").strip()
    if not question:
        print("❌ 문제를 입력해주세요.\n")
        return

    # 2단계: 선택지 입력
    print("\n📝 선택지를 입력하세요 (4개, 엔터로 구분):")
    choices = []
    for i in range(4):
        choice = input(f" {i+1}번: ").strip()
        if not choice:
            print("❌ 모든 선택지를 입력해주세요.\n")
            return
        choices.append(choice)

    # 3단계: 정답 입력
    while True:
        try:
            answer = int(input("\n✅ 정답 번호를 입력하세요 (1-4): ")) - 1
            if 0 <= answer <4:
                break
            else:
                print("❌ 1-4 사이의 숫자를 입력해주세요.")
        except ValueError:
            print("❌ 숫자를 입력해주세요.")

    # 4단계: 힌트 입력
    hint = input("\n💡 힌트를 입력하세요 (선택사항, 엔터 스킵): ").strip()

    # 5단계: 퀴즈 생성 및 저장
    quiz = Quiz(question, choices, answer, hint)
    game.quizzes.append(quiz)
    game.save_state()

    print("\n✅ 퀴즈가 추가되었습니다!\n")

def show_quiz_list_action(game):
    #3. 퀴즈 목록
    print("\n" + "="*50)
    print("📚 퀴즈 목록")
    print("="*50)

    if not game.quizzes:
        print("\n❌ 등록된 퀴즈가 없습니다.\n")
        input("엔터를 눌러 계속하세요...")
        return

    for i, quiz in enumerate(game.quizzes, 1):
        print(f"\n[{i}번]")
        print(f" 문제: {quiz.question}")
        print(f" 선택지: {','.join(quiz.choices)}")    #join()은 앞의 값으로 (뒤)의 값들을 연결한다. 예: ','.join(["파이썬", "자바", "C언어"])   결과: "파이썬,자바,C언어"
        print(f" 정답: {quiz.choices[quiz.answer]}")
        if quiz.hint:
            print(f" 힌트: {quiz.hint}")

    print()
    input("엔터를 눌러 계속하세요...")
    

def delete_quiz_action(game):
    #5. 퀴즈 삭제
    print("\n" + "="*50)
    print("🗑️  퀴즈 삭제")
    print("="*50)

    if not game.quizzes:
        print("\n❌ 등록된 퀴즈가 없습니다.\n")
        return

    # 1단계: 퀴즈 목록 표시
    for i, quiz in enumerate(game.quizzes, 1):
        print(f"\n[{i}번] {quiz.question}")

    # 2단계: 삭제할 퀴즈 선택
    while True:
        try:
            choice = int(input("\n🗑️  삭제할 퀴즈 번호를 입력하세요: "))
            if 1 <= choice <= len(game.quizzes):
                break
            else:
                print(f"❌ 1-{len(game.quizzes)} 사이의 숫자를 입력해주세요.")
        except ValueError:
            print("❌ 숫자를 입력해주세요.")

    # 3단계: 확인 및 삭제
    deleted_quiz = game.quizzes[choice -1]
    confirm = input(f"\n정말 '{deleted_quiz.question}'을(를) 삭제하기겠습니까? (y/n): ").strip().lower()

    if confirm == 'y':
        game.quizzes.pop(choice - 1)
        game.save_state()
        print("✅ 퀴즈가 삭제되었습니다!\n")
    else:
        print("⏭️  삭제가 취소되었습니다.\n")
                