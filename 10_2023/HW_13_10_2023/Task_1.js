function create_array(){
    let list = [];
    for(let i = 1; i < 6; i += 1){
    list.push(Math.floor((Math.random() * 10)));
    }
    return list;
}

function not_in_list(li, el) {
    for (let i = 0; i < li.length; i += 1) {
        if (li[i] === el) {
            return true;
        }
    }
    return false;
}

function new_list(li_1,li_2){
    let new_list = [];
    for (let i = 0; i < li_1.length; i++) {
        let check = not_in_list(li_2, li_1[i])
        if(!check){
            new_list.push(li_1[i]);
        }
    }
    return new_list;
}

function common_elements(li_1, li_2){
    let new_list = [];
    for (let i = 0; i < li_1.length; i++) {
        for (let j = 0; j < li_2.length; j++) {
            if(li_1[i] === li_2[j]){
                new_list.push(li_1[i]);
            }
        }
    }
    return new_list;
}

let arr_1 = create_array();
let arr_2 = create_array();

console.log('Создать еще один массив из 5 случайных чисел и написать следующие \n' +
    'функции:\n' +
    '▪ Функция принимает 2 массива и возвращает новый массив, в котором \n' +
    'собраны общие элементы (то есть элементы, которые встречаются и в \n' +
    'первом, и во втором массивах) без повторений. \n' +
    '▪ Функция принимает 2 массива и возвращает новый массив, в котором \n' +
    'собраны все элементы из первого массива, которых нет во втором \n' +
    'массиве.');

console.log('Первый массив: ', arr_1);
console.log('Второй массив: ', arr_2);
console.log('Задание 1 часть 1 Результат:', Array.from(new Set(common_elements(arr_1, arr_2))));
console.log('Задание 1 часть 2 Результат:', new_list(arr_1, arr_2));
console.log()
