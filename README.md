# Дипломный проект тестирования сайта https://ru.wikipedia.org/

## В проекте присутствуют UI, API и интеграционные тесты

___

### Используемые технологии

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-plain-wordmark.svg" height="40" wigth="40"/><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg" height="40" wigth="40"/><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/selenium/selenium-original.svg" height="40" wigth="40"/><img src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4" height="40" wigth="40"/><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original-wordmark.svg" height="40" wigth="40"/>

### Настройка проекта перед запуском

Перед запуском тестов необходимо создать файл `.env` в корне проекта.   
Для файла `.env` заполнить креды для доступа к selenoid и доступа к Википедии по API.   
Пример файла, куда необходимо внести свои данные - `.env.example`

#### Команды для запуска тестов:

- Запуск всех тестов

```
pytest tests
```

- Запуск UI тестов

```
pytest tests/UI/<test_file_name>
```

- Запуск API тестов

```
pytest tests/API/<test_file_name>
```

- Запуск интеграционных тестов

```
pytest tests/Integration/<test_file_name>
```

- Генерация allure отчета после выполнения тестов

```
allure serve allure-results
```

--- 

### Описание шагов теста с выводом скриншота и скринкаста

<img src="https://github.com/pijamaenota90/qa_final/blob/main/images/First_diplom.png" width="943" height="412">

### Настройка telegram бота для уведомлений о результатах прохождении тестов

<img src="https://github.com/pijamaenota90/qa_final/blob/main/images/Second_diplom.png" width="478" height="422">


          
