import json
from pathlib import Path
#from datetime import datetime   #원래 관래상 모듈과 파일은 소문자로 시작, 클래스는 대문자로 시작인데... 이것은 초기 작성자가 클래스를 소문자로 작성함. 왜냐? 해당 모듈의 핵심 클래스는 소문자로 시작해서 알릴려고 했음.
from quiz import Quiz           #원래 관래상 모듈과 파일은 소문자로 시작, 클래스는 대문자로 시작

#모듈은 .py파일 한 개, 패키지는 __init__.py가 있는 폴도로 여러 개의 모듈이 있음, 라이브러리는 여러 개의 패키지 모임
from actions.play import play_game_action
from actions.manage import add_quiz_action, show_quiz_list_action, delete_quiz_action
from actions.record import show_best_score_action, show_history_action

class QuizGame:
    def __init__(self):
        #게임 초기화
        self.state_file = Path(__file__).parent / "state.json"  #파일 명을 변수에 넣어서 경로로 쓰기 위함. 그리고 코드 수정 시에 변수 하나만 바꾸면 되기에 편함
        self.quizzes = []                                       #Path(__file__)은 현재 파일인 quiz_game.py가 있는 곳, Path(__file__).parent는 현재 파일의 부모가 있는 곳
        self.best_score = 0
        self.best_record = {"correct": 0, "total": 0}
        self.history = []
        self.load_message = ""
        self.load_state()

    # ──────────────────────────────────────────
    # 데이터 관련
    # ──────────────────────────────────────────

    def load_state(self):
        #state.json에서 데이터 로드
        try:
            with open(self.state_file, "r", encoding="utf-8") as f:
                data = json.load(f)        #json.load() 파일 객체 타입을 받아 직접 읽기, json.loads() 문자열 타입을 직접 또는 그 변수를 받아 읽을 때

            self.quizzes = [Quiz.from_dict(q) for q in data.get("quizzes", [])]  #data.get(키, 기본값)은 키가 있으면 그 값 반환, 키가 없으면 기본값 반환하기에 에러 예방. 그리고 [리스트 컴프리헨션]의 내부에서 생성되는 값은 계속 append된다. 
            self.best_score = data.get("best_score", 0)
            self.best_record = data.get("best_record", {"correct": 0, "total": 0})
            self.history = data.get("history", [])

            self.load_message = (
                f"📂 저장된 데이터를 불러왔습니다. "
                f"(퀴즈 {len(self.quizzes)}개, 최고점수 {self.best_score}점)"
            )

        except FileNotFoundError:
            self.load_message = "📂 저장된 데이터가 없습니다. 새로 시작합니다."
            self.save_state(show_message=False)

        except json.JSONDecodeError:
            self.load_message = "⚠️  저장 파일이 손상되었습니다. 빈 상태로 시작합니다."

        except Exception as e:
            self.load_message = f"⚠️  데이터 로드 중 오류 발생: {e}"

    def save_state(self, show_message=True):
        #현재 상태를 state.json에 저장
        try:
            data = {
                "quizzes" : [q.to_dict() for q in self.quizzes],
                "best_score" : self.best_score,
                "best_record" : self.best_record,
                "history" : self.history
            }
            with open(self.state_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)   #data를 f에 덮어서 쓴다. json은 보통 덮어서 쓴다. 왜냐면 json은 하나의 객체 {  }가 되어야 하는데 이어서 쓰면 {  } {  } ...이런 형식이 된다.
                                                                   #json.dump() 파일에 저장, json.dumps() 파일을 문자열로 변환

            if show_message:
                print("✅ 저장되었습니다.")

        except Exception as e:
            print(f"⚠️  저장 중 오류 발생: {e}")

    # ──────────────────────────────────────────
    # 메뉴 및 메인 루프
    # ──────────────────────────────────────────

    def show_menu(self):
        #초기 화면 + 메인 메뉴 표시
        print("\n" + "=" * 40)
        print("        🎯 농구 퀴즈 게임 🎯")
        print("=" * 40)
        print(self.load_message)
        print("=" * 40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 최고 점수 확인")
        print("5. 퀴즈 삭제")
        print("6. 점수 기록 보기")
        print("7. 종료")
        print("=" * 40)

    def run(self):
        #게임 메인 루프
        menu_actions = {
            "1": self.play_game,
            "2": self.add_quiz,
            "3": self.show_quiz_list,
            "4": self.show_best_score,
            "5": self.delete_quiz,
            "6": self.show_history,
        }

        while True:
            try:
                self.show_menu()
                choice = input("선택: ").strip()     #input()은 티미널에 커서가 깜빡임. strip()은 앞뒤의 공백 및 줄바꿈 제거

                if choice == "7":
                    self.save_state(show_message=False)
                    print("\n👋 게임을 종료합니다. 또 만나요!\n")
                    break

                elif choice in menu_actions:     # v in dict이면 v가 dict에 있는가? boolean반환. 단, 딕셔너리면 키값 비교, 리스트면 요소 비교, 문자역이면 부분 문자열 비교
                    menu_actions[choice]()
            
            except KeyboardInterrupt:
                print("\n\n⚠️  강제 종료 감지. 저장 후 종료합니다")
                self.save_state(show_message=False)
                break
                
    # ──────────────────────────────────────────
    # 기능 메서드 (다음 단계에서 구현)
    # ──────────────────────────────────────────
    
    def play_game(self):
        #1. 퀴즈 풀기 -> actons/play.py
        play_game_action(self)
    
    def add_quiz(self):
        #2. 퀴즈 추가 ->actions/manage.py
        add_quiz_action(self)
        
    def show_quiz_list(self):
        #3. 퀴즈 목록 -> actions>manage.py
        show_quiz_list_action(self)
        
    def show_best_score(self):
        #4. 최고 점수 확인 -> actions/record.py
        show_best_score_action(self)
        
    def delete_quiz(self):
        #5. 퀴즈 삭제 -> actions/manage.py
        delete_quiz_action(self)
        
    def show_history(self):
        #6. 점수 기록 보기 -> action/record.py
        show_history_action(self)
        
# ──────────────────────────────────────────
# 진입점
# ──────────────────────────────────────────

if __name__ == "__main__":   #__name__은 파이썬이 직접 저장하는 변수로 현재 파일이 직접 실행이 되면 "__main__"을 저장하고, 다른 파일에서 import하면 그 파일 명을 저장함
    game = QuizGame()        #예: from quiz_game import QuizGame면 __name__에는 "quiz_game"이 저장된다.
    game.run()
