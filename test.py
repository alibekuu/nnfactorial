class CinemaTicketSystem:
    def __init__(self):
        # Инициализация системы с пустыми словарями и счетчиками
        self.movies = {}  # Хранит фильмы, где ключ - movie_id, а значение - movieName
        self.users = {}  # Хранит пользователей, где ключ - user_id, а значение - userName
        self.tickets = {}  # Хранит билеты, где ключ - ticket_id, а значение - кортеж (userId, movieId)
        
        # Счетчики для генерации уникальных ID для фильмов, пользователей и билетов
        self.movie_counter = 1  # Начать нумерацию ID фильмов с 1
        self.user_counter = 1  # Начать нумерацию ID пользователей с 1
        self.ticket_counter = 1  # Начать нумерацию ID билетов с 1

    def addMovie(self, movieName):
        # Добавление нового фильма в систему
        movie_id = self.movie_counter  # Присвоить ID фильма текущий счетчик фильмов
        self.movies[movie_id] = movieName  # Сохранить фильм в словаре
        self.movie_counter += 1  # Увеличить счетчик фильмов для следующего фильма
        return movie_id  # Вернуть ID нового фильма

    def showAllMovies(self):
        # Отображение всех фильмов, которые есть в системе
        if not self.movies:  # Проверить, есть ли фильмы в системе
            print("В данный момент нет доступных фильмов.")  # Сообщить пользователю, если фильмов нет
        else:
            for movie_id, movieName in self.movies.items():  # Перебрать все фильмы
                print(f"{movie_id}. {movieName}")  # Показать ID и название каждого фильма

    def addUser(self, userName):
        # Добавление нового пользователя в систему
        user_id = self.user_counter  # Присвоить ID пользователя текущий счетчик пользователей
        self.users[user_id] = userName  # Сохранить пользователя в словаре
        self.user_counter += 1  # Увеличить счетчик пользователей для следующего пользователя
        return user_id  # Вернуть ID нового пользователя

    def showAllUsers(self):
        # Отображение всех пользователей, которые есть в системе
        if not self.users:  # Проверить, есть ли пользователи в системе
            print("В данный момент нет зарегистрированных пользователей.")  # Сообщить, если пользователей нет
        else:
            for user_id, userName in self.users.items():  # Перебрать всех пользователей
                print(f"{user_id}. {userName}")  # Показать ID и имя каждого пользователя

    def deleteUser(self, userId):
        # Удаление пользователя из системы
        if userId in self.users:  # Проверить, существует ли пользователь с таким ID
            user_name = self.users[userId]  # Получить имя пользователя
            del self.users[userId]  # Удалить пользователя из словаря
            # Также удалить все билеты, которые были куплены этим пользователем
            self.tickets = {ticket_id: (uid, mid) for ticket_id, (uid, mid) in self.tickets.items() if uid != userId}
            print(f"Пользователь '{user_name}' с ID {userId} был успешно удален.")  # Сообщить об успешном удалении
            return True  # Вернуть True, чтобы указать, что пользователь был удален
        else:
            return False  # Вернуть False, чтобы указать, что пользователь с таким ID не найден

    def buyTicket(self, userId, movieId):
        # Позволить пользователю купить билет на фильм
        if userId in self.users and movieId in self.movies:  # Проверить, валидны ли ID пользователя и фильма
            ticket_id = self.ticket_counter  # Присвоить ID билета текущий счетчик билетов
            self.tickets[ticket_id] = (userId, movieId)  # Сохранить билет с ID пользователя и фильма
            self.ticket_counter += 1  # Увеличить счетчик билетов для следующего билета
            print(ticket_id)
            return ticket_id  # Вернуть ID нового билета
        else:
            return None  # Вернуть None, если ID не валидны

    def cancelTicket(self, ticketId):
        # Отмена билета путем удаления его из системы
        if ticketId in self.tickets:  # Проверить, существует ли такой ID билета
            del self.tickets[ticketId]  # Удалить билет из словаря
            return True  # Сообщить об успешной отмене билета
        else:
            return False  # Сообщить, что билет с таким ID не найден

    def menu(self):
        # Отображение меню для взаимодействия с системой
        while True:
            # Показать доступные опции
            print("\nДобро пожаловать! Вот ваши опции:")
            print("1. Добавить новый фильм")
            print("2. Показать все доступные фильмы")
            print("3. Добавить нового пользователя")
            print("4. Показать всех пользователей")
            print("5. Удалить пользователя")
            print("6. Купить билет")
            print("7. Отменить билет")
            print("8. Выйти")

            # Получить выбор пользователя
            choice = input("Выберите опцию: ")

            if choice == "1":
                # Опция 1: Добавить новый фильм
                movie_name = input("Введите название фильма: ")  # Запросить название фильма
                self.addMovie(movie_name)  # Добавить фильм в систему
                print(f"Фильм '{movie_name}' успешно добавлен!")  # Подтвердить добавление

            elif choice == "2":
                # Опция 2: Показать все доступные фильмы
                self.showAllMovies()  # Показать все фильмы

            elif choice == "3":
                # Опция 3: Добавить нового пользователя
                user_name = input("Введите имя пользователя: ")  # Запросить имя пользователя
                self.addUser(user_name)  # Добавить пользователя в систему
                print(f"Пользователь '{user_name}' успешно добавлен!")  # Подтвердить добавление

            elif choice == "4":
                # Опция 4: Показать всех пользователей
                self.showAllUsers()  # Показать всех пользователей

            elif choice == "5":
                # Опция 5: Удалить пользователя
                self.showAllUsers()  # Показать всех пользователей перед удалением
                try:
                    user_id = int(input("Введите ID пользователя, которого хотите удалить: "))  # Запросить ID пользователя
                    if self.deleteUser(user_id):  # Попытаться удалить пользователя
                        print(f"Пользователь с ID {user_id} успешно удален.")  # Подтвердить удаление
                    else:
                        print("Ошибка: пользователь с таким ID не найден.")  # Обработать отсутствие пользователя
                except ValueError:
                    print("Ошибка: пожалуйста, введите допустимое числовое значение.")  # Обработать нечисловой ввод

            elif choice == "6":
                # Опция 6: Купить билет
                try:
                    user_id = int(input("Введите ID пользователя: "))  # Запросить ID пользователя
                    movie_id = int(input("Введите ID фильма: "))  # Запросить ID фильма
                    ticket_id = self.buyTicket(user_id, movie_id)  # Попытаться купить билет
                    if ticket_id:
                        print(f"Ваш билет на фильм с ID {movie_id} успешно куплен! ID билета: {ticket_id}")  # Подтвердить покупку
                    else:
                        print("Ошибка: неверный ID пользователя или фильма.")  # Обработать неверные ID
                except ValueError:
                    print("Ошибка: пожалуйста, введите допустимые числовые значения.")  # Обработать нечисловой ввод

            elif choice == "7":
                # Опция 7: Отменить билет
                try:
                    ticket_id = int(input("Введите ID билета: "))  # Запросить ID билета
                    if self.cancelTicket(ticket_id):  # Попытаться отменить билет
                        print(f"Билет с ID {ticket_id} успешно отменен.")  # Подтвердить отмену
                    else:
                        print("Ошибка: билет с таким ID не найден.")  # Обработать отсутствие билета с данным ID
                except ValueError:
                    print("Ошибка: пожалуйста, введите допустимый числовой ID билета.")  # Обработать нечисловой ввод

            elif choice == "8":
                # Опция 8: Выйти из системы
                print("До свидания!")  # Прощальное сообщение
                break  # Выйти из цикла

            else:
                # Обработать некорректный выбор
                print("Ошибка: неверный выбор. Попробуйте снова.")  # Сообщить пользователю о некорректном вводе

# Создать экземпляр системы и запустить меню
cinemaSystem = CinemaTicketSystem()
cinemaSystem.menu()
