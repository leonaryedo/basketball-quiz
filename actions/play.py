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
    pass