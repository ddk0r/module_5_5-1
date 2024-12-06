import time

class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __repr__(self):
        return self.nickname

class Video:
    def __init__(self, title: str, duration: int, time_now = 1, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __repr__(self):
        return self.title

class UrTube:
    def __init__(self, videos = [], current_user = None, users = []):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, nickname, password):
        for i in self.users:
            if i.nickname == nickname:
                if i.password == hash(password):
                    self.current_user = i
                    print('Авторизация прошла успешно')
                    return
                else:
                    print('Пароль введён не верно')
                    return
        print('Такого пользователя не существует')

    def register(self, nickname, password, age):
        for i in self.users:
            if i.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        curr_us = User(nickname, password, age)
        self.users.append(curr_us)
        self.current_user = curr_us
        print('Пользователь зарегистрирован')

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            flag = False
            for j in self.videos:
                if i.title == j.title:
                    flag = True
                    break
            if not flag:
                self.videos.append(i)

    def get_videos(self, match):
        match_videos = []
        for i in self.videos:
            if match.lower() in i.title.lower():
                match_videos.append(i)
        if len(match_videos) == 0:
            print('Подходящие видео не найдены')
        return match_videos

    def watch_video(self, match):
        match_video = None
        for i in self.videos:
            if match == i.title:
                match_video = i
                break
        if not match_video:
            print('Искомое видео не найдено')
            return

        if self.current_user:
            if (match_video.adult_mode and self.current_user.age >= 18) or not match_video.adult_mode:
                for i in range(match_video.time_now, match_video.duration):
                    print(i)
                    match_video.time_now = i
                    time.sleep(1)
                print('Конец видео')
            else:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode = True)
# Добавление видео

ur.add(v1, v2)
# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)


# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')