function restruct(variable){
    let list = [1, 2, 3, 4, 5];
    let string = '123456';
    let new_list = [];
    if(variable === 1){
        for (let i = 0; i < list.length; i++) {
            if(list[i] === 1 || list[i] === 4 || list[i] === 5){
                new_list.push(list[i])
            }
        }
    return new_list;
    } else if(variable === 2){
        return list.slice(1, 4);
    } else if(variable === 3){
        list.splice(3, 0, "c");
        list.splice(3, 0, "b");
        list.splice(3, 0, "a");
        return list;
    } else if(variable === 4){
        list.splice(1, 0, 'b');
        list.splice(1, 0, 'a');
        list.splice(6, 0, 'c');
        list.push('e');
        return list;
    } else {
        return string.split("").reverse().join("");
    }
}

console.log('• Дан массив [1, 2, 3, 4, 5]. Преобразуйте массив в [1, 4, 5]\n' +
    '• Дан массив [1, 2, 3, 4, 5]. Запишите в новый массив элементы [2, 3, 4].\n' +
    '• Дан массив [1, 2, 3, 4, 5]. Cделайте из него массив [1, 2, 3, \'a\', \'b\', \'c\', 4, 5].\n' +
    '• Дан массив [1, 2, 3, 4, 5]. Cделайте из него массив [1, \'a\', \'b\', 2, 3, 4, \'c\', 5, \'e\']\n' +
    '• Дана строка, например, \'123456\'. Переверните эту строку (сделайте из нее \n' +
    '\'654321\') не используя цикл.')

console.log('Задача 6 Часть 1 Результат:', restruct(1));
console.log('Задача 6 Часть 2 Результат:', restruct(2));
console.log('Задача 6 Часть 3 Результат:', restruct(3));
console.log('Задача 6 Часть 4 Результат:', restruct(4));
console.log('Задача 6 Часть 5 Результат:', restruct(5));
