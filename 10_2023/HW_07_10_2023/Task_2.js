alert('Задача 2 \nЗапросить у пользователя число от 0 до 9 и вывести ему спецсимвол, \n' +
    'который расположен на этой клавише (1–!, 2–@, 3–# и т. д).');

let arr = {'1':'!', '2':"@", '3':'#', '4':'$', '5':'%', '6':'^', '7':'&', '8':'*', '9':'(', '0':')'};
let question = prompt('Введите число от 0 до 9');

if(question!=null){
    if(question>=0&&question<=9) {
        alert('Символ цифры ' + question + ' на клавиатуре: ' + arr[question])
    }
} else {
    alert('Неверные данные')
}