let s = 1000,
    m = s * 60,
    h = m * 60,
    d = h * 24,
    y = d * 365;

//setInterval(() => {
//    counting();
//}, 1000);

setInterval(() => 1000);


const formAddDate = document.getElementById('addDate');
formAddDate.addEventListener('submit', addTime);

function addTime(e) {
    const date = document.getElementById('date').value,
        time = document.getElementById('time').value,
        timeYears = document.getElementById('time-years'),
        timeDays = document.getElementById('time-days'),
        timeHours = document.getElementById('time-hours'),
        timeMinutes = document.getElementById('time-minutes'),
        timeSeconds = document.getElementById('time-seconds');

    if (date && time) {
        const chosenDate = new Date(`${date} ${time}`)
        document.getElementById('until').innerText = chosenDate.toString();

        const hidden = document.querySelectorAll('.hidden');
        hidden.forEach(el => el.style.display = 'block');

        const interval = setInterval(() => {
            const pickedDate = new Date(`${date} ${time}`).getTime(),
                currentDate = new Date().getTime(),
                difference = pickedDate - currentDate,
                years = Math.floor(difference / y);

            if (years < 1) {
                timeYears.parentElement.style.display = 'none';
            } else {
                timeYears.parentElement.style.display = 'block';

            }
            timeYears.innerHTML = Math.floor(difference / y);
            timeDays.innerHTML = Math.floor((difference % y) / d);
            timeHours.innerHTML = Math.floor((difference % d) / h);
            timeMinutes.innerHTML = Math.floor((difference % h) / m);
            timeSeconds.innerHTML = Math.floor((difference % m) / s);
        }, 1000);

        document.querySelector('button').addEventListener('click', () => {
            clearInterval(interval);
        });

        formAddDate.reset();
    }
    e.preventDefault();
}