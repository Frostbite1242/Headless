# Починаемо 

Зараз розглянемо з чого почати якщо вибрали Python як мову розробки

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

    driver = webdriver.Firefox()
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()

У запущеному вами Python повинен бути встановлений модуль Selenium.


# Пояснення прикладу

Модуль selenium.webdriver забезпечує всі реалізації WebDriver. 
В даний час підтримуються реалізації WebDriver: Firefox, Chrome, IE та Remote. 
Клас клавіш забезпечує клавіші на клавіатурі, такі як RETURN, F1, ALT тощо.


    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys


Далі створюється екземпляр Firefox WebDriver.


    driver = webdriver.Firefox()


Метод driver.get перейде на сторінку, вказану за URL-адресою. WebDriver зачекає, 
поки сторінка повністю завантажиться (тобто спрацює подія «завантаження»), 
перш ніж повернути керування до тесту або сценарію.
Майте на увазі, що якщо ваша сторінка використовує багато AJAX під час завантаження, 
то WebDriver може не знати, коли вона повністю завантажиться:


./driver.get("http://www.python.org")


Наступний рядок - це твердження, яке підтверджує, що в заголовку є слово “Python”:


    assert "Python" in driver.title


WebDriver пропонує ряд способів пошуку елементів за допомогою одного з методів find_element_by_ *.
Наприклад, вхідний текстовий елемент може бути розміщений за його атрибутом name за допомогою методу find_element_by_name. 
Детальне пояснення пошуку елементів доступне в главі Розміщення елементів:


    elem = driver.find_element_by_name("q")


Далі ми надсилаємо ключі, це схоже на введення ключів за допомогою клавіатури.
Спеціальні ключі можна надіслати за допомогою клавіші Keys, імпортованої з selenium.webdriver.common.keys.
Для безпеки ми спочатку очистимо будь-який попередньо заповнений текст у полі введення (наприклад, "Пошук"), щоб це не впливало на результати пошуку:


    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)


Після подання сторінки ви повинні отримати результат, якщо такий є. 
Щоб переконатися, що деякі результати знайдені, зробіть твердження:


    assert "No results found." not in driver.page_source


Нарешті, вікно браузера закрито. Ви також можете викликати метод quit замість закриття.
Вихід закриє весь браузер, тоді як закриття закриє одну вкладку, 
але якщо була відкрита лише одна вкладка, за замовчуванням більшість браузерів вийде повністю:


    driver.close()


#Використання Selenium для написання тестів


Selenium в основному використовується для написання тестових кейсів.
Сам пакет Selenium не забезпечує інструмент / фреймворк для тестування.
Ви можете писати тестові кейси, використовуючи модуль unittest Python. Інші варіанти інструменту / фреймворку - це pytest та nose.

У цьому розділі ми використовуємо unittest як основу вибору. 
Ось модифікований приклад, який використовує модуль unittest. Це тест на функціональність пошуку python.org:



    import unittest
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

    class PythonOrgSearch(unittest.TestCase):

        def setUp(self):
            self.driver = webdriver.Firefox()

        def test_search_in_python_org(self):
            driver = self.driver
            driver.get("http://www.python.org")
            self.assertIn("Python", driver.title)
            elem = driver.find_element_by_name("q")
            elem.send_keys("pycon")
            elem.send_keys(Keys.RETURN)
            assert "No results found." not in driver.page_source


        def tearDown(self):
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()
    
    
    
Наведений результат показує, що тест успішно пройшов.

Примітка: Щоб запустити наведений вище тест в IPython або Jupyter, вам слід передати пару аргументів основній функції, як показано нижче:


    unittest.main(argv=['first-arg-is-ignored'], exit=False)


# Пояснення прикладу



Спочатку імпортуються всі необхідні основні модулі. Модуль unittest - це вбудований Python на основі JUnit Java. 
Цей модуль забезпечує основу для організації тестових кейсів. Модуль selenium.webdriver забезпечує всі реалізації WebDriver.



В даний час підтримуються реалізації WebDriver: Firefox, Chrome, IE та Remote. Клас клавіш забезпечує клавіші на клавіатурі, такі як RETURN, F1, ALT тощо.


    import unittest
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys


Клас тестового випадку успадковується від unittest.TestCase. Успадкування класу TestCase - це спосіб сказати модулю unittest, що це тестовий випадок:


    class PythonOrgSearch(unittest.TestCase):


SetUp є частиною ініціалізації, цей метод буде викликаний перед кожною тестовою функцією, 
яку ви збираєтеся написати у цьому класі тестового випадку. 
Тут ви створюєте екземпляр Firefox WebDriver.


    def setUp(self):
        self.driver = webdriver.Firefox()
    
    
Це метод тестування. Метод тестового випадку завжди повинен починатися з тестування символів. 
Перший рядок усередині цього методу створює локальне посилання на об'єкт драйвера, створений у методі setUp.


    def test_search_in_python_org(self):
        driver = self.driver

    
Метод driver.get переходить на сторінку, вказану для URL-адреси. WebDriver попереджає, 
залишаючи сторінку повністю завантажується (якщо задавати поділ «завантаження»), перш ніж повертати керування до тесту або сценарію.
Зверніться до уваги, якщо ваша сторінка використовує багато AJAX під час завантаження, щоб WebDriver не міг знати, коли вона буде повністю завантажена:


    driver.get("http://www.python.org")


Наступний рядок - це твердження, яке підтверджує, що в заголовку є слово “Python”:


    self.assertIn("Python", driver.title)


WebDriver пропонує ряд способів пошуку елементів за допомогою одного з методів find_element_by_ *. 
Наприклад, вхідний текстовий елемент може бути розміщений за його атрибутом name за допомогою методу find_element_by_name. 
Детальне пояснення пошуку елементів доступне в главі Розміщення елементів:


    elem = driver.find_element_by_name("q")


Далі ми надсилаємо ключі, це схоже на введення ключів за допомогою клавіатури. 
Спеціальні ключі можна надіслати за допомогою клавіші Клавіші, імпортованої із selenium.webdriver.common.keys:


    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)



Після подання сторінки ви повинні отримати результат відповідно до пошуку, якщо такий є. 
Щоб переконатися, що деякі результати знайдені, зробіть твердження:


assert "No results found." not in driver.page_source


Метод tearDown буде викликатися після кожного тестового методу.
Тут можна проводити всі очисні роботи. У поточному методі вікно браузера закрито. Ви також можете викликати метод quit замість закриття.
Вихід закриє весь браузер, тоді як закриття закриє вкладку, але якщо це єдина відкрита вкладка, за замовчуванням більшість браузерів вийде повністю:


    def tearDown(self):
        self.driver.close()
    
    
Останні рядки - це код котельної таблички для запуску тестового набору:


    if __name__ == "__main__":
        unittest.main()
    
    
 # Використання Selenium з віддаленим WebDriver
 
 
 Щоб використовувати віддалений WebDriver, у вас повинен бути запущений сервер Selenium. 
 Для запуску сервера використовуйте цю команду:
 

     java -jar selenium-server-standalone-2.x.x.jar
 
 
 Під час запуску сервера Selenium ви могли побачити повідомлення, що виглядає так:
 
 
 **15:43:07.541 INFO - RemoteWebDriver instances should connect to: http://127.0.0.1:4444/wd/hub**
 
 
 У наведеному вище рядку написано, що ви можете використовувати цю URL-адресу для підключення до віддаленого WebDriver. Ось кілька прикладів:
 
 
    from selenium import webdriver
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

    driver = webdriver.Remote(
       command_executor='http://127.0.0.1:4444/wd/hub',
       desired_capabilities=DesiredCapabilities.CHROME)

    driver = webdriver.Remote(
       command_executor='http://127.0.0.1:4444/wd/hub',
       desired_capabilities=DesiredCapabilities.OPERA)

    driver = webdriver.Remote(
       command_executor='http://127.0.0.1:4444/wd/hub',
       desired_capabilities=DesiredCapabilities.HTMLUNITWITHJS)
   
   
Бажаними можливостями є словник, тому замість використання словників за замовчуванням ви можете явно вказати значення:


    driver = webdriver.Remote(
       command_executor='http://127.0.0.1:4444/wd/hub',
       desired_capabilities={'browserName': 'htmlunit',
                             'version': '2',
                            'javascriptEnabled': True})
