CatBot
=====

CatBot - это бот для Telegram сщзданный с целью делать вашу жизнь лучше, присылая вам фотографии котиков

Установка
----------

Создайте виртуальное окружение и активируйте его. Потом в вирутальном окружении выполните:

.. code-block:: text

    pip install -r requirements.txt

Положите картинки с котиками в папку images. Название файла должно начинаться с cat, а заканичиваться .jpg например cat7347.jpg



Настройка
----------------

Создайте файл settings.py и добавьте туда следующие настройки:

.. code-block:: python

	PROXY = {'proxy_url': 'socks5://ВАШ_SOCKS5_ПРОКСИ:1080',
			 'urllib3_proxy_kwargs': {'username': 'ЛОГИН', 'password': 'ПАРОЛЬ'}}

	API_KEY = "API ключ, который вы получили у BotFather"

	USER_EMOJI = [':smiley_cat:', ':smiling_imp:', ':panda_face:', ':dog:']


Запуск
------------

В активированном виртуальном окружении выполните:

.. code-block:: text

	python3 bot.py
