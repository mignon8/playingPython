// サーバー通信
function api(url) {
  return new Promise((resolve, reject) => {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.onreadystatechange = function (e) {
      if (this.readyState === 4 && this.status === 200) {
        resolve(this.responseText);
      }
    };
    xhr.send();
  });
}

const get2021sFilm = () => {
  api('/api/film_2021').then((res) => {
    let films = JSON.parse(res);
    console.log(films);

    films.forEach((film) => {
      const newElm = document.createElement('p')
      newElm.textContent = `${film.title}：${film.rating}`
      document.getElementById('result').appendChild(newElm);
    });
  });
};

window.addEventListener('DOMContentLoaded', () => {
  document.getElementById('filmButton').onclick = get2021sFilm;
});
