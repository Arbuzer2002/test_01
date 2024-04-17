document.addEventListener('DOMContentLoaded', function() {

    let newsCards = document.querySelectorAll('.projcard-container');

    for (let i = 1; i < newsCards.length; i++) {
        newsCards[i].classList.add('hidden');
    }

    function showPrevNews() {
        let currentNews = document.querySelector('.projcard-container.active');
        let prevNews = currentNews.previousElementSibling;
        if (prevNews) {
            currentNews.classList.remove('active');
            currentNews.classList.add('hidden');
            prevNews.classList.remove('hidden');
            prevNews.classList.add('active');
        }
    }


    function showNextNews() {
        let currentNews = document.querySelector('.projcard-container.active');
        if (currentNews) {
            let nextNews = currentNews.nextElementSibling;
            if (nextNews) {
                currentNews.classList.remove('active');
                currentNews.classList.add('hidden');
                nextNews.classList.add('active');
                nextNews.classList.remove('hidden');
            }
        }
    }


    document.querySelectorAll('.prev-news-button').forEach(button => {
        button.addEventListener('click', showPrevNews);
    });

    document.querySelectorAll('.next-news-button').forEach(button => {
        button.addEventListener('click', showNextNews);
    });
});
