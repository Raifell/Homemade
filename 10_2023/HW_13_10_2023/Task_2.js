let arr = [12, 4, 50, 1, 0, 18, 40];

function check_zero(li){
    for (let i = 0; i < li.length; i++) {
        if(li[i] === 0){
            return true;
        }
    }
    return false;
}

console.log('Проверить, содержит ли массив [12, 4, 50, 1, 0, 18, 40] элементы, равные нулю. \n' +
    'Если да - вернуть true\n');
console.log('Задача 2 Результат:', check_zero(arr));
console.log();
