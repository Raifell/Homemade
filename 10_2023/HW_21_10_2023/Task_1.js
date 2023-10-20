console.log('Задача 1 \nНаписать функцию, которая принимает 2 числа и возвращает -1, ' +
    'если первое меньше, чем второе; 1 – если первое больше, чем второе; и 0 – если числа равны.');

let num_1 = Math.floor(Math.random() * 11);
let num_2 = Math.floor(Math.random() * 11);

function search(a, b){
    if(a < b){
        return '-1';
    } else if(a > b) {
        return '1';
    } else {
        return '0';
    }
}

console.log('Числа: ' + num_1 + ', ' + num_2 + '\nРезультат: ' + search(num_1, num_2));
console.log('');
