function create_array(){
    let list = [];
    for(let i = 1; i < 10; i += 1){
    list.push(Math.floor((Math.random() * 10)));
    }
    return list;
}

function only_even(li){
    let new_list = [];
    for (let i = 0; i < li.length; i++) {
        if(li[i] % 2 === 0){
            new_list.push(li[i])
        }
    }
    return new_list;
}

let arr_ay = create_array()

console.log('Создать массив. Пользователь должен заполнить этот массив случайными \n' +
    'числами. Создать на основе этого массива новый массив, где будут только \n' +
    'четные элементы');

console.log('Задача 5 Результат:', only_even(arr_ay));
console.log();
