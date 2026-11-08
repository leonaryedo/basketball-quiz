import json
from pathlib import Path
from datetime import datetime   #원래 관래상 모듈과 파일은 소문자로 시작, 클래스는 대문자로 시작인데... 이것은 초기 작성자가 클래스를 소문자로 작성함. 왜냐? 해당 모듈의 핵심 클래스는 소문자로 시작해서 알릴려고 했음.
from quiz import Quiz           #원래 관래상 모듈과 파일은 소문자로 시작, 클래스는 대문자로 시작

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

            self.quizzes = [Quiz.from_dict(q) for q in data.get("quizzes", [])]  #data.get(키, 기본값)은 키가 있으면 그 값 반환, 키가 없으면 기본값 반환하기에 에러 예방
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
                "bset_score" : self.best_score,
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

    def run(self)
        #게임 메인 루프
        