class Quiz:
    #농구 퀴즈 하나를 표현하는 클래스

    def __init__(self, question, choices, answer, hint=""):
        """
        __init__ : 생성자로 처음 메서드가 실행될 때 한 번만 실행
        self : 자기자신으로 파이썬은 원본 클래스가 있고 이것을 활용해서 객체를 생성하는데, 
               그때 필요한 객체의 정보(같은 클래스의 다른 객체가 여러 개 있으니)를 가져오기 위해서 자신의 정보를 담아둔 곳과 연결하기 위해서 self를 씀
        question (str): 퀴즈 문제
        choices (list): 선택지
        answer (int): 정답번호
        hint (str): 힌트(선택사항) hint=""이면 입력이 없으면 자동으로 빈 문자열이 들어감
        """
        self.question = question    #자기 자신에게 정보를 저장하는 것
        self.choices = choices
        self.answer = answer
        self.hint = hint
    
    def show(self):
        #문제와 선택지 출력
        print(f"\n{self.question}")
        for i, choice in enumerate(self.choices, 1): 
            print(f"{i}) {choice}")
            """
            enumerate는 리스트의 인덱스 값 동시에 가져온다. 
            첫번째 인자는 리스트, 두번째 인자는 인덱스의 시작 번호 지정 즉 인덱스 0 -> 1로 바뀐어 시작된다.
            """ 

    def check_answer(self, n):
        """
        입력 번호가 정답인지 확인
        n (int): 사용자 입력
        return (bool): 정답여부
        """
        return n == (self.answer +1) #인덱스는 0부터 시작, 사용자는 1부터 시작

    def show_hint(self):
        #힌트 출력
        if self.hint:
            print(f"💡 힌트: {self.hint}")  #이모지는 파이썬에서 문자열이라 직접포함가능
        else:
            print(f"💡 힌트가 없습니다.")

    def to_dict(self):
        #Quiz 객체를 dict로 변환 (JSON 저장)
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
            "hint": self.hint
        }

    @classmethod        #클래스 메서드는 인스턴스가 아닌 클래스 자체에서 호출하는 메서드로 어떤 클래스를 인스턴스(객체)화 하는지 가독성을 높여줌
    def from_dict(cls, data):      #클래스 메서드의 첫 번째 매개변수는 cls임. 해당 클래스의 변수 접근 쉬움 및 상속할 경우에 올바른 클래스가 됨.
        return cls(
            question=data["question"],
            choices=data["choices"],
            answer=data["answer"],
            hint=data.get("hint", "")  #data.get(키, 기본값)은 키가 있으면 그 값 반환, 키가 없으면 기본값 반환하기에 에러 예방
        )


"""
테스트 하기 1 - state.json 연동하여 확인
state.json코드
{
    "quizzes": [
        {
            "question": "농구에서 한 팀의 선수는 몇 명인가?",
            "choices": ["4명", "5명", "6명", "7명"],
            "answer": 1,
            "hint": "NBA 경기에서 코트에 나가는 선수 수입니다."
        }
    ],
    "best_score": 80,
    "best_record": {
        "correct": 4,
        "total": 5
    },
    "history": [
        {
            "date": "2024-01-15 14:30:00",
            "correct": 4,
            "total": 5,
            "score": 80
        }
    ]
}

파이썬에서 실행
from quiz import Quiz
# from 파일 import 클래스명   다른 폴더인 경우에는 경로 지정 필요
import json

# JSON 파일 읽기
with open('state.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# quizzes 배열에서 Quiz 객체 생성
quizzes = [Quiz.from_dict(q) for q in data["quizzes"]]

# 첫 번째 퀴즈 표시
quizzes[0].show()
quizzes[0].show_hint()
quizzes[0].answer
quizzes[0].check_answer(0)

"""
