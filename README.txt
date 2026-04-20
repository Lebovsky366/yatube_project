Yatube — социальная сеть для публикации личных дневников\
\
Yatube — это учебный проект социальной сети, где пользователи могут создавать учётные записи, публиковать записи, объединять их в тематические сообщества и управлять контентом через удобную админ-панель. Проект написан на Django с использованием Bootstrap для адаптивной вёрстки.\
\
Используемые технологии: Python 3.9+, Django 2.2.19, Bootstrap 5 (локально или через CDN), SQLite (база данных), Git (система контроля версий).\
\
Как развернуть проект на новом компьютере:\
\\

1. Клонирование репозитория:\\\
   git clone &lt;[https://github.com/ваш\\\\\\\_username/yatube_project.git&gt;\\\\](https://github.com/%D0%B2%D0%B0%D1%88%5C%5C%5C_username/yatube_project.git&gt;%5C%5C)\
   cd yatube_project\
   \\
2. Создание и активация виртуального окружения:\\\
   Для Windows (Git Bash):\\\
   python -m venv venv\\\
   source venv/Scripts/activate\\\
   Для macOS / Linux:\\\
   python3 -m venv venv\\\
   source venv/bin/activate\
   \\
3. Установка зависимостей:\\\
   pip install -r requirements.txt\
   \\
4. Применение миграций:\\\
   cd yatube (переходим в папку с \[[manage.py](http://manage.py)\]([http://manage.py))\\\\](http://manage.py\)\)%5C%5C)\
   python \[[manage.py](http://manage.py)\](<http://manage.py>) migrate\
   \\
5. Создание суперпользователя (администратора):\\\
   python \[[manage.py](http://manage.py)\](<http://manage.py>) createsuperuser\\\
   Следуйте инструкциям: введите логин, email (можно пропустить), пароль.\
   \\
6. Запуск сервера разработки:\\\
   python \[[manage.py](http://manage.py)\](<http://manage.py>) runserver\\\
   Проект станет доступен по адресу &lt;<http://127.0.0.1:8000/>&gt;\
   \
   Структура проекта:\\\
   yatube_project/\\\
   ├── yatube/ # рабочая папка с \[[manage.py](http://manage.py)\]([http://manage.py)\\\\](http://manage.py\)%5C%5C)\
   │ ├── posts/ # приложение для управления постами\\\
   │ ├── static/ # статические файлы (CSS, изображения)\\\
   │ ├── templates/ # HTML-шаблоны\\\
   │ │ ├── includes/ # подключаемые блоки (header, footer)\\\
   │ │ ├── posts/ # шаблоны приложения posts\\\
   │ │ └── base.html # базовый шаблон\\\
   │ └── yatube/ # настройки проекта (\[[settings.py](http://settings.py)\](<http://settings.py>), \[[urls.py](http://urls.py)\]([http://urls.py))\\\\](http://urls.py\)\)%5C%5C)\
   ├── venv/ # виртуальное окружение\\\
   ├── requirements.txt # зависимости\\\
   ├── \[[README.md](http://README.md)\](<http://README.md>) # этот файл\\\
   └── .gitignore # список игнорируемых файлов\
   \
   Основные страницы и URL:\
   \\

- Главная страница: / (список последних 10 постов от новых к старым)\
  \\
- Страница сообщества: /group/&lt;slug&gt;/ (например, /group/cats/) — посты, принадлежащие определённой группе\
  \\
- Админ-зона: /admin/ (управление пользователями, постами и группами)\
  \
  Работа с админ-панелью:\\\
  После входа под суперпользователем по адресу /admin/ доступны:\
  \\
- Users – управление пользователями.\
  \\
- Posts – список всех постов. Здесь можно добавлять, редактировать, удалять посты, а также назначать им группы.\
  \\
- Groups – создание и редактирование тематических сообществ.\\\
  Для удобства в админке настроены: поиск по тексту постов, фильтрация по дате публикации, быстрое редактирование поля group прямо из списка постов.\
  \
  Работа с моделями:\\\
  В проекте определены две основные модели:\
  \
  Модель Post (пост):\
  \\
- text – текст поста (TextField)\
  \\
- pub_date – дата публикации (автоматически проставляется)\
  \\
- author – ссылка на пользователя (ForeignKey)\
  \\
- group – ссылка на сообщество, необязательное поле (ForeignKey, blank=True, null=True)\
  \
  Модель Group (сообщество):\
  \\
- title – название группы\
  \\
- slug – уникальный адрес (часть URL)\
  \\
- description – описание сообщества\
  \
  После изменения моделей необходимо создать и применить миграции:\\\
  python \[[manage.py](http://manage.py)\](<http://manage.py>) makemigrations\\\
  python \[[manage.py](http://manage.py)\](<http://manage.py>) migrate\
  \
  Настройка статики:\\\
  Статические файлы (CSS, изображения) хранятся в папке static/ на уровне проекта. В \[[settings.py](http://settings.py)\](<http://settings.py>) прописано:\\\
  STATICFILES_DIRS = \\\[os.path.join(BASE_DIR, 'static')\\\]\\\
  В шаблонах статика подключается через теги:\\\
  {% load static %}\
  \
  &lt;link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}"&gt; &lt;img src="{% static 'img/logo.png' %}" alt="Логотип"&gt;\
  \
  Внесение изменений и работа с Git:\\\
  После любых изменений кода (например, после добавления новой модели или изменения шаблонов) рекомендуется выполнить:\\\
  git add .\\\
  git commit -m "Описание изменений"\\\
  git push\
  \
  Часто возникающие проблемы и их решение:\
  \\

1. Ошибка NoReverseMatch при ссылке на страницу группы:\
   \\
   - Убедитесь, что в posts/\[[urls.py](http://urls.py)\](<http://urls.py>) есть app_name = 'posts' и path('group/&lt;slug:slug&gt;/', ... name='group_list').\
     \\
   - В шаблоне используйте {% url 'posts:group_list' \[[post.group](http://post.group)\](<http://post.group).slug> %}.\
     \\
2. На главной странице не отображаются посты:\
   \\
   - Проверьте, что в \[[views.py](http://views.py)\](<http://views.py>) функция index() передаёт posts = Post.objects.order_by('-pub_date')\\\[:10\\\].\
     \\
   - Убедитесь, что в базе данных есть хотя бы один пост (создайте через админку).\
     \\
3. Статика не загружается (нет стилей):\
   \\
   - Проверьте, что папка static/ находится в корне проекта (рядом с \[[manage.py](http://manage.py)\](<http://manage.py>)).\
     \\
   - Добавьте STATICFILES_DIRS в \[[settings.py](http://settings.py)\](<http://settings.py>).\
     \\
   - Запустите сервер и проверьте доступность файла по адресу &lt;<http://127.0.0.1:8000/static/css/bootstrap.min.css>&gt;.\
     \\
4. Ошибка 404 при переходе на страницу группы:\
   \\
   - Убедитесь, что группа создана в админке и поле slug заполнено корректно (только латиница, цифры, дефисы).\
     \\
   - Проверьте URL: /group/правильный-slug/.\
     \
     Автор:\\\
     Проект выполнен в рамках учебного курса. Ваше имя: \\\[вставьте ваше имя\\\]. GitHub: \\\[ссылка на ваш профиль\\\] (опционально).
