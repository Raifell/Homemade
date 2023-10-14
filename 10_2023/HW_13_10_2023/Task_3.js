let arr_a_y = ['yes', 'hello', 'no', 'easycode', 'what'];

function check_length(li) {
    for (let i = 0; i < li.length; i++) {
        if (li[i].length < 3){
            return false;
        }
    }
    return true;
}

console.log('Проверить, все ли элементы массива имеют длину более 3х символов [\'yes\', \n' +
    '\'hello\', \'no\', \'easycode\', \'what\']. Если да - вернуть true, иначе false');
console.log('Задача 3 Результат:', check_length(arr_a_y));
console.log();
