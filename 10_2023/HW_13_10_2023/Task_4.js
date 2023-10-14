let list =  ['I','am','a','fornt-end','developer'];
let result = list.sort((a, b) => a.length - b.length);

console.log('Дан массив строк [\'I\',\'am\',\'a\',\'fornt-end\',\'developer\']. Отсортировать массив по \n' +
    'длине строк (в порядке возрастания и наоборот)');

console.log('Задача 4 Результат в порядке возрастания:',
    result);

console.log('Задача 4 Результат в порядке убывания:',
    result.reverse());

console.log();
