# Создай класс Movies:
# проинициализируй в нём пустой список self.movies через конструктор;
# добавь метод add_movie(). Он будет принимать параметр movie и добавлять его в конец списка self.movies.
# Создай два дочерних класса — Comedy и Drama. Они наследуют метод add_movie(). 
# Метод этих классов должен принимать параметр movie и добавлять его в конец списка self.movies. 
# Затем возвращать записи вида Комедии: '[]' и Драмы: '[]' соответственно.
# Вызови метод add_movie() для объекта Comedy(). Входной параметр — 'Большой куш'. Выведи на экран результат.
# Вызови метод add_movie() для объекта Drama(). Входной параметр — 'Оружейный барон'. Выведи на экран результат.

# Чтобы добавить элемент в конец списка, нужен метод append(). То есть так: self.movies.append(movie).
# Чтобы вернуть значение, используй return. Понадобится вернуть значение в определённом виде: return f'Комедии: {self.movies}'.

class Movies:
    def __init__(self):
        self.movies = []

    def add_movies(self, movie):
        self.movies.append(movie)

class Comedy(Movies):
    def  add_movies(self, movie):
        super().add_movies(movie)  # вызываем метод родительского класса
        return f'Комедии: {self.movies}'  # возвращаем в нужном формате

class Drama(Movies):
    def  add_movies(self, movie):
        super().add_movies(movie)  # вызываем метод родительского класса
        return f'Драма: {self.movies}'  # возвращаем в нужном формате

comedy_result = Comedy().add_movies('Большой куш')
print(comedy_result)
drama_result = Drama().add_movies('Оружейный барон')
print(drama_result)