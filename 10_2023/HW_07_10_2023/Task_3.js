alert('Задача 3 \nЗапросить у пользователя год и проверить, високосный он или нет.\n');

let year = Number(prompt('Введите год: '));

if(year==''){
    alert('Неверные данные')
} else if(year % 4 != 0){
    alert('Год не високосный.');
} else if(year % 100 == 0){
    if(year % 400 == 0){
        alert('Год високосный.');
    } else {
        alert('Год не високосный.')
    }
} else {
    alert('Год високосный.')
}