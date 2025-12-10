# Дз №14: Учимся быстро разрабатывать готовые проекты для тестовых заданий.
## UI тесты на сайт https://ru.wikipedia.org/
___
### Используемые технологии
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-plain-wordmark.svg" height="40" wigth="40"/><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg" height="40" wigth="40"/><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/selenium/selenium-original.svg" height="40" wigth="40"/><img src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4" height="40" wigth="40"/><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original-wordmark.svg" height="40" wigth="40"/>
### Настройка проекта перед запуском
Перед запуском тестов необходимо создать файл `.env` в директории `tests`   
Для файла `.env` заполнить креды для доступа к selenoid.   
**Например:**
```
SELENOID_LOGIN=user1
SELENOID_PASS=1234
SELENOID_URL=selenoid.autotests.cloud
```

#### Команды для запуска тестов:

- Прогон всех тестов   
```
pytest tests
```
- Запуск конкретного теста
```
pytest tests/<test_file_name>
```
- Генерация allure отчета после выполнения тестов   
```
allure serve allure-results
```
--- 
### Запуск в [jenkins](https://jenkins.autotests.cloud/job/qa_lesson14/)
<img src="https://github.com/pijamaenota90/qa_lesson14/raw/main/images/First.png" width="943" height="412">  

### Описание шагов теста с выводом скриншота и скринкаста
<img src="https://github.com/pijamaenota90/qa_lesson14/raw/main/images/Second.png" width="943" height="412">

### Настройка telegram бота для уведомлений о результатах прохождении тестов
<img src="https://github.com/pijamaenota90/qa_lesson14/raw/main/images/Third.png" width="478" height="422">


          
