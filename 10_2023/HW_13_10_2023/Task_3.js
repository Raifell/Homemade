let arr_a_y = ['yes', 'hello', 'no', 'easycode', 'what'];

function check_length(li) {
    for (let i = 0; i < li.length; i++) {
        if (li[i].length < 3){
            return false;
        }
    }
    return true;
}

console.log('Задача 3 Результат:', check_length(arr_a_y))
