# project-blog
Создаю приложение для блога.
Модель пользователя будет находится в модуле django.contrib.auth.models.User
Для регистрации пользователя достаточно воспользоваться методом create_user (метод можно посмотреть в объявлении модели User в исходном коде фреймворка). 
Пример использования функции: from django.contrib.auth.models import User
User.objects.create_user("user1", "user@mail.ru", "user_password")
В функцию передается 3 параметра: логин, email и пароль. Для того, чтобы пользователь смог отправить эти данные, необходимо создать страницу с формой регистрации и обработать вводимые значения. 
Должна быть выполнена проверка на предмет того, имеется ли уже в базе данных пользователь с таким логином. Чтобы это проверить, достаточно попробовать найти его в базе данных с помощью метода get, который вызовет исключение, если объекта не существует:
Try: User.objects.get(username=username)
# если пользователь существует, то ошибки не произойдет и программа # удачно доберется до следующей строчки
print "Пользователь с таким именем уже есть"
except User.DoesNotExist:
print "Этот логин свободен"

Создаю шаблон формы регистрации:
def create_user(request):
    if request.method == "POST":
        form = {
            'username': request.POST["username"],
            'mail': request.Post["mail"],
            'password': request.POST["password"]
        }
        art = None
        try:
            art = User.objects.get(username=form["username"])
            art = User.objects.get(email=form["mail"])
            # если юзер существует, то ошибки не произойдет и
            # программа удачно доберётся до следущей строки
            print(u"Такой юзер уже есть")
        except User.DoesNotExist:
            print(u"Такого юзера ещё нет")    
        if form["username"] and form["mail"] and form["password"] and art is None:
            art = User.objects.create_user(username=form["username"],
                                        email=form["mail"],
                                        password=form["password"])
            return redirect(archive)
        else:
            if art is not None:
                form['errors'] = u"Логин или почта уже занята"
            else:   
                form['errors'] = u"Не все поля заполнены"
            return render(request, 'registration.html', {'form': form})
    else:
        return render(request, 'registration.html', {})

        Создаю  стили, подключив CSS-файл к шаблону

        texstarea {
    margin: 5px 0;
    width: 196px;
    height: 34px;
    border: 1px solid black;
    border-radius: 4px;
}

input[type="text"] {
    width: 200px;
    border: 1px solid black;
    border-radius: 4px;
}

input {
    border: 2px solid black;
    border-radius: 4px;
}

body {
    background: #1abc9c;
    font-family: Tahoma, Arial, Helvetica, sans-serif;
    color: #ffffff;
}

.content {
    width: 960px;
    margin-left: auto;
    margin-right: auto;
    text-align: center;
}

.errors {
    color: rgb(218, 0, 0);
    font-weight: bold;
}

img {
    display: block;
    width: 318px;
    margin-left: auto;
    margin-right: auto;
}

Добавляю в шапку страницы всех записей и страницы для определенных статей, ссылку на регистрацию в верхнем правом углу (стиль ссылки сделать такой же, как у ссылки “Все статьи” на собственных страницах постов в предыдущих работах). 

Выполняю создание формы, шаблона и представления для авторизации.

Для того, чтобы пользователь мог войти в систему, он должен пройти процесс аутентификации (проверка подлинности предъявленного пользователем идентификатора, т.е. имеется ли в базе данных такая пара логин – пароль) и авторизации (предоставление определённому лицу прав на выполнение определённых действий, процесс проверки (подтверждения) данных прав при попытке выполнения этих действий). 
Для этого можно воспользоваться функцией authenticate из модуля django.contrib.auth. Данная функция принимает два параметра: логин и пароль и сверяет их с базой данных, если такая пара логин – пароль существует, то метод возвращает объект User, иначе возвратит None:
from django.contrib.auth import authenticate
user = authenticate(username="user1", password="user_pass")
После удачной аутентификации, можно авторизовать пользователя функцией login из модуля django.contrib.auth. Функция принимает два параметра: текущий объект запроса и объект пользователя):
from django.contrib.auth import login
login(request, user)
Иначе, если аутентификация оказалось неудачной и вместо объекта User вернулся None, то пользователю нужно снова вернуть форму входа в систему, при этом вывив сообщение о том, что такого аккаунта не существует.
Создаю шаблон и настройте адрес для отображения формы авторизации;
•	Создаю представление, которое будет обрабатывать поступающие запросы и авторизировать зарегистрированных пользователей. Не забудем сделать проверку на то, что отправленные поля не являются пустыми, а введенные имя пользователя и пароль соответствуют одному из зарегистрированных аккаунтов; 
def input_user(request):
    if request.method == "POST":
        form = {
            'username': request.POST["username"],
            'password': request.POST["password"]
        }
        if form["username"] and form["password"]:
            user = authenticate(request, username=form["username"],password=form["password"])
            if user is None:
                form['errors'] = u"Такой пользователь не зарегестрирован!"
                
                return render(request, 'auth.html', {'form': form})
            else:
                login(request, eser)
            return redirect(archive)    
        else:
            form['errors'] = u"Не все поля заполнены"
            return render(request, 'auth.html', {'form': form})
    else:
        return render(request, 'auth.html', {})

      Создаю стили, подключив CSS-файл к шаблону.

Загружаю мой проект на гит-репозиторий
  
