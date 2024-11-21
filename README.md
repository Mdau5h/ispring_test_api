# Тестовое задание ISpring API Tests.

## Подготовка проекта
- Установить Python 3.11:
https://www.python.org/downloads/

- Проверить версию Python:
```sh
python3 --version
```
- Перейти в директорию проекта
- Убедиться в наличии файла ```.env``` в корневой директории проекта. Пример:

```
BASE_URL=https://api.github.com
GITHUB_TOKEN={github_token}
TEST_REPO={test_repo}
TEST_USERNAME={test_username}
```
   
- Установить зависимости:
```sh
pip install -U pip setuptools pipenv && pipenv install
 ```

## Запуск тестов
Запуск тестов производится из директории проекта:
```sh
pytest ./tests -v -s
```