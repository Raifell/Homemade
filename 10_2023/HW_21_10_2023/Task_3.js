console.log('Задача 3\nНаписать функцию, которая принимает три отдельные цифры и превращает их в' +
    ' одно число. Например: цифры 1, 4, 9 превратятся в число 149');

let num_4 = Math.floor(Math.random() * 10);
let num_5 = Math.floor(Math.random() * 10);
let num_6 = Math.floor(Math.random() * 10);

function create_int(a, b, c){
    return `${a}` + `${b}` + `${c}`;
}

console.log('Числа: ' + num_4 + ', ' + num_5 + ', ' + num_6 + '\nРезультат: ' + create_int(num_4, num_5, num_6));
console.log('');
