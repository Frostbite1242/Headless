# Вступ



Прив’язки Selenium Python надають простий API для написання функціональних 
прийнятних тестів за допомогою Selenium WebDriver. За допомогою API Selenium Python ви можете
інтуїтивно отримати доступ до всіх функцій Selenium WebDriver.

Прив’язки Selenium Python забезпечують зручний API для доступу до веб-драйверів Selenium, 
таких як Firefox, Chrome, Remote тощо. Поточні підтримувані версії Python становлять 3.5 і вище.

У цій документації розглянемо Selenium 2 WebDriver API



# Инсталювання Selenium 

Використовуйте pip для встановлення пакету Selenium . Python 3 має pip, доступний у стандартній бібліотеці.
Використовуючи pip, ви можете встановити Selenium  таким чином:

* Відкрити cmd

* Написати наступну команду 
    
    pip install selenium
   
   
* Також бажанно оновити pip командою 

    python -m pip install --upgrade pip
   
Selenium вимагає драйвера для взаємодії з обраним браузером. Наприклад, Firefox вимагає geckodriver,
який потрібно встановити перед запуском наведених нижче прикладів. Переконайтеся, що він у вашому PATH,
наприклад. г., помістіть його в / usr / bin або / usr / local / bin.
    
Недотримання цього кроку призведе до помилки

selenium.common.exceptions.WebDriverException: Message: ‘geckodriver’ executable needs to be in PATH

Інші підтримувані браузери матимуть власні драйвери. Далі посилаються на деякі найпопулярніші драйвери браузера.

-Chrome:	https://sites.google.com/a/chromium.org/chromedriver/downloads


-Edge:	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/


-Firefox:	https://github.com/mozilla/geckodriver/releases


-Safari:	https://webkit.org/blog/6900/webdriver-support-in-safari-10/





