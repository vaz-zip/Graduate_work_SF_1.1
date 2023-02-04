# Graduate_work_SF_1.1
Полное описание находится в файле: https://github.com/vaz-zip/Graduate_work_SF_1.1/blob/main/%D0%94%D0%B8%D0%BF%D0%BB%D0%BE%D0%BC%D0%BD%D0%B0%D1%8F%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0.doc

Группа FPW-57
автор:
Ширяев Константин
 Викторович

Дипломная работа
на тему:
«Разработка электронной сервисной книжки для автомобилей «Мой Силант»»

В процессе выполнения дипломной работы были реализованы следующие задачи:

1. Описания базы данных были перенесены в форму кода Django-models. В файл My_Silant/silant/models.py
2. При помощи настроек админ-панели Django были созданы три группы с различными правами доступа к содержимому сервиса: Client, Servis, Manager.
Каждой группе были даны соответствующие права через представления.
3. Были созданы страницы сервиса с данными из БД в табличном виде:
   
4. Для каждой таблицы была предусмотрена фильтрация:

5. Сортировка данных в соответствующих Таблицах по умолчанию  проводится по полям:
    • «дата отгрузки с завода» для таблицы «машина»; 
    • «дата проведения ТО» для таблицы «ТО»; 
    • «дата отказа« для таблицы «рекламации» благодаря применению во view-urlpatterns order_by() для соответствующих моделей: 
  
6.  Строки таблиц кликабельны и переводят на отдельную страницу с детальной информацией об объекте модели:
     
7. Пользователь не может самостоятельно зарегистрироваться, данные выдаются администратором. В панели авторизации отсутствует поле регистрации.
   
Администратор в админ-панели Django сам создает нового пользователя. 

8. Адаптивность и резиновость верстки достигнута использованием @media -запросов стилей,
    
относительных размеров: max-width, min-width, автоматических размеров, размеров в процентах от основного блока. Кроссбраузерность — так же прописывается в стилях:
    
9. Дизайн интерфейса выполнен в фирменном стиле (использование цветов, шрифта):
 Использовались только фирменные цвета, логотип и элементы дизайна оригинала.
10. Кроме всего прочего реализована панель для работы администратора -ь заполнение справочников и работы ст БД вне аминпанели:
   
