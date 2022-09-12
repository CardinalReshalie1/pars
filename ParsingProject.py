
import requests                                  #добавляем необходимые библиотеки, это реквест для отправки HTTP запросов на разные сайты.
from bs4 import BeautifulSoup                    #Потом BeautifulSoup из bs4 (библиотека Python для извлечения данных из файлов HTML и XML)
from time import sleep                           #библиотека для управлением временем, а в этом случае создание задержки перед запросами

headers = {"User-Agent":                         #Создаем словарь с другим именем, что бы сайты не блокировали твои запросы, так как на сайте будет видно что ты БОТ!
            "Mozilla/5.0 (Windows NT 6.1; en-US; rv:1.9.1.5)Gecko/20091102 Firefox/3.5.5"}



for count in range(1, 8):                        # создаем цикл рендж что бы данная команда повторялась с 1 по 8 страницу! со строкой слип(3) что значит задержка 3 секунды
    sleep(3)
    url = f"https://scrapingclub.com/exercise/list_basic/?page={count}" # урл сайт с которого будут взяты данные
    

    response = requests.get(url, headers=headers)                       # это команда requests https://otus.ru/nest/post/1516/
                                                                        # если коротко то http серия идет Запрос-Ответ
                                                                        # Самый популярный запрос — GET. Он указывает, что осуществляется попытка извлечь -
                                                                        # данные из какого-нибудь ресурса. Для выполнения этого запроса используют команду requests.get().
                                                                        # В вышеописанном примере мы использовали get() для захвата определённого значения, являющегося частью объекта Response
                                                                        # с последующим помещением этого значения в переменную response.
                                                                        # Теперь мы получили возможность использовать переменную response для изучения данных, полученных в результате отправки запроса GET.
            
    soup = BeautifulSoup(response.text, "lxml")                         #придаем переменной соуп значение и + это lxml это команда для правильного получения текста, так же можно "html.parser"
    data = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")        #Придаем переменной дата что бы соуп находила див с указанным классом, это наш первый блок
                                                                        #Далее, делаем цикл фор для I из data, ишем имя, ищем цену, и картинку. в конце вывод.
    for i in data:

        name = i.find("h4", class_="card-title").text.replace("\n", "")
        price = i.find("h5").text
        url_img = "https://scrapingclub.com" + i.find("img", class_="card-img-top img-fluid").get("src")

        print(name + "\n" + price + "\n" + url_img + "\n\n")








