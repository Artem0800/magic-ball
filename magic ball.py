import random
answers = ["Бесспорно","Предрешено","Никаких сомнений","Определенно да","Может быть уверен в этом","Мне кажется - да",
           "Вероятнее всего","Хорошие перспективы","Знаки говорят - да","Да","Пока неясно, попробуй снова",
           "Спроси позже","Лучше не рассказывать","Сейчас нельзя предсказать","Сконцентрируйся и спроси опять",
           "Даже не думай","Мой ответ - нет","По моим данным - нет","Перспективы не очень хорошие","Весьма сомнительно"]
print("Привет , я магический шар, и я знаю ответ на любой твой вопрос.")
name_user = input("Как тебя зовут ?")
print(f"Привет {name_user}")
while True:
    question = input("Какой твой вопрос ?")
    print(random.choice(answers))
    replay = input("Есть еще вопросы ? д/н")
    if replay == "н":
        print("Возвращайся если возникнут вопросы!")
        break
