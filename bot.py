import random

# 랜덤 응답 설정하기 
random_responses = ["재미있는 이야기네요, 자세히 알려주세요.",
                    "그렇군요. 계속 이야기해주세요.",
                    "왜 그렇게 말한건가요?",
                    "정말 웃긴 날씨네요, 안그래요?",
                    "주제를 바꿔봅시다.",
                    "어제 밤 경기 보셨어요?"]

print("안녕하세요 저는 간단한 챗봇 건국봇입니다.")
print("대화를 끝내고 싶으면 '그만'이라고 말해주세요 ")
print("각 답을 입력한 후 엔터를 눌러주세요 ")
print("오늘 기분 어떤가요")

while True:
    # 인풋 기다리기
    user_input = input("> ")
    if user_input == "그만":
        # 그만이라고 말하면 루프문 탈출(대화 그만하기)
        break
    else:
        response = random.choices(random_responses)[0]
    print(response)

print("좋은 대화였습니다. 안녕히가세요")
