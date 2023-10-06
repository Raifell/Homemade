alert('Задача 5 \nЗапросить у пользователя длину окружности и периметр квадрата. \n' +
    'Определить, может ли такая окружность поместиться в указанный квадрат.');

let circle = Number(prompt('Введите длину окружности'));
let square = Number(prompt('Введите периметр квадрата'));

let D_circle = circle / Math.PI
let N_square = square / 4

if(D_circle != '' && N_square != ''){
    if(D_circle<N_square){
        alert('Окружность с длиной ' + circle + ' можно поместить в квадрат с периметром ' + square)
    } else if(D_circle>=N_square) {
        alert('Окружность с длиной ' + circle + ' нельзя поместить в квадрат с периметром ' + square)
    }
} else {
    alert('Неверное значение')
}
