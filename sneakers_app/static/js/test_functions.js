function displayMatchingProducts(result) {
	fetch('/app/process_quiz_and_display_products', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify({ answers: result }),
	})
	.then(response => {
		if (response.ok) {
			window.location.href = '/app/test_matching_products';
		} else {
			console.error('Ошибка при выполнении запроса:', response.statusText);
		}
	})
	.catch(error => {
		console.error('Ошибка:', error);
	});
}

//Обновление теста
function Update()
{
	//Проверяем, есть ли ещё вопросы
	if(quiz.current < quiz.questions.length)
	{
		//Если есть, меняем вопрос в заголовке
		headElem.innerHTML = quiz.questions[quiz.current].text;

		//Удаляем старые варианты ответов
		buttonsElem.innerHTML = "";

		//Создаём кнопки для новых вариантов ответов
		for(let i = 0; i < quiz.questions[quiz.current].answers.length; i++)
		{
			let btn = document.createElement("button");
			btn.className = "button";

			btn.innerHTML = quiz.questions[quiz.current].answers[i].text;

			btn.setAttribute("index", i);

			buttonsElem.appendChild(btn);
		}

		//Выводим номер текущего вопроса


		//Вызываем функцию, которая прикрепит события к новым кнопкам
		Init();
	}
	else
	{
		//Если это конец, то выводим результат
		buttonsElem.innerHTML = "";
		headElem.innerHTML = "";
		displayMatchingProducts(quiz.results[quiz.result]);
	}
}

function Init()
{
	//Находим все кнопки
	let btns = document.getElementsByClassName("button");

	for(let i = 0; i < btns.length; i++)
	{
		//Прикрепляем событие для каждой отдельной кнопки
		//При нажатии на кнопку будет вызываться функция Click()
		btns[i].addEventListener("click", function (e){ Click(e.target.getAttribute("index")); });
	}
}

function Click(index)
{
	//Получаем номер правильного ответа
	let correct = quiz.Click(index);

	//Находим все кнопки
	let btns = document.getElementsByClassName("button");

   	//Делаем кнопку зеленой

	btns[index].className = "button button_correct";

	//Ждём секунду и обновляем тест
	setTimeout(Update, 1000);
}