CatBot
=====

CatBot - ��� ��� ��� Telegram ��������� � ����� ������ ���� ����� �����, �������� ��� ���������� �������

���������
----------

�������� ����������� ��������� � ����������� ���. ����� � ����������� ��������� ���������:

.. code-block:: text

    pip install -r requirements.txt

�������� �������� � �������� � ����� images. �������� ����� ������ ���������� � cat, � �������������� .jpg �������� cat7347.jpg



���������
----------------

�������� ���� settings.py � �������� ���� ��������� ���������:

.. code-block:: python

	PROXY = {'proxy_url': 'socks5://���_SOCKS5_������:1080',
			 'urllib3_proxy_kwargs': {'username': '�����', 'password': '������'}}

	API_KEY = "API ����, ������� �� �������� � BotFather"

	USER_EMOJI = [':smiley_cat:', ':smiling_imp:', ':panda_face:', ':dog:']


������
------------

� �������������� ����������� ��������� ���������:

.. code-block:: text

	python3 bot.py
