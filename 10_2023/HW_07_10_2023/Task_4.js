alert('Задача 4 \nКонвертор валют. Пользователь вводит количество USD, \n' +
    'выбирает, в какую валюту хочет перевести: EUR, UAH или AZN, и получает' +
    'в ответ соответствующую сумму. ');

let conv = Number(prompt('Введите количество USD'));
let cash = prompt('Введите валютный код для конвертации\nEUR, UAN, AZN\nРегистр не имеет значения');

if(cash.toLowerCase()==='eur'){
    alert(conv + ' USD = ' + (conv * 0.94794).toFixed(2) + ' EUR')
} else if(cash.toLowerCase()==='uah'){
    alert(conv + ' USD = ' + (conv * 36.63).toFixed(2) + ' UAH')
} else if(cash.toLowerCase()==='azn'){
    alert(conv + ' USD = ' + (conv * 1.7).toFixed(2) + ' AZN')
} else {
    alert('Неверные данные')
}
