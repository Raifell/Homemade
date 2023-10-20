console.log('Задача 2\nНаписать функцию, которая вычисляет факториал переданного ей числа.');

let num_3 = Math.floor(Math.random() * 11);

function factorial(a){
    let result = 1;
    for (let i = 1; i <= a; i++) {
        result *= i;
    }
    return result;
}

console.log('Число: ' + num_3 + '\nФакториал: ' + factorial(num_3));
console.log('');
