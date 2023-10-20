console.log('Задача 4\nНаписать функцию, которая принимает длину и ширину прямоугольника и вычисляет ' +
    'его площадь. Если в функцию передали 1 параметр, то она вычисляет площадь квадрата.');

let num_7 = Math.floor(Math.random() * 10 + 1);
let num_8 = Math.floor(Math.random() * 11);

function square(a, b=0){
    let result = 0;
    if(b){
        result += a * b;
        return [result, 'Прямоугольник'];
    } else {
        result += a * a;
        return [result, 'Квадрат'];
    }
}

let result_1;
if(num_8) {
    result_1 = square(num_7, num_8);
} else {
    num_8 = 'Отсутствует для фигуры Квадрат'
    result_1 = square(num_7);
}

console.log('Фигура: ' + result_1[1] + '\nCторона A: ' + num_7 + '\nСторона B: ' + num_8 + '\nПлощать сторон фигуры: ' +
    result_1[0]);
