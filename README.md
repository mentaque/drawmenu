# drawmenu
Функция, реализованная через templatetags для отрисовки меню с n-ым количеством дочерних элементов.
Для того чтобы добавить дочерние ветки нужно использовать такую конструкцию:   
Между тэгами \<li> поместить \<ul>, в котором циклом проходимся по всем элементам, добавляем их в теги \<li> и т.д., можно добавить неограниченное кол-во дочерних элементов.
Всё редактируется в админке джанго.
# Недоработки
Пытался релизовать активный пункт меню через context, передаваемый в templatetags, но вышло очень запутанно.

