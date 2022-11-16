const headTitle = document.querySelector('#head-title')
const searchInput = document.querySelector('.search-input')
const searchButton = document.querySelector('.search-button')
const searchResult = document.querySelector('.search-result')
const searchResultLoader = document.querySelector('.search-result-loader')


const resetSearch = function () {
  searchResult.innerHTML = ''
}

headTitle.addEventListener('click', function (event) {
  resetSearch()
})

const searchMusic = function () {
  const inputData = searchInput.value
  searchInput.value = null

  searchResult.innerHTML = ''
  loadList(inputData)
  
  document.addEventListener('scroll', function (event) {
      console.log(event.path[1].scrollY)
      if (event.path[1].scrollY + 1000 > document.documentElement.scrollHeight) {
        loadList(inputData)
      }
  })
}

const loadList = function (inputData) {
  for (let i = 0; i < 6; i++) {
    setTimeout(() => {
      const searchResultCard = document.createElement("div")
      searchResultCard.classList.add('search-result-card-load')
      searchResultLoader.appendChild(searchResultCard)
  
      const albumImg = document.createElement("div")
      albumImg.classList.add('album-image-load')
      searchResultCard.appendChild(albumImg)
  
      const albumDiscription = document.createElement("div")
      albumDiscription.classList.add('album-discription-load')
      searchResultCard.appendChild(albumDiscription)
  
      const albumTitle = document.createElement("div")
      albumTitle.classList.add('album-title-load')
      albumDiscription.appendChild(albumTitle)
  
      const albumArtist = document.createElement("div")
      albumArtist.classList.add('album-artist-load')
      albumDiscription.appendChild(albumArtist)
    }, i * 40);
  }

  const API_KEY = config.apiKey
  axios.get(`https://ws.audioscrobbler.com/2.0/?method=album.search&album=${inputData}&api_key=${API_KEY}&format=json`)
    .then(response => {
      console.log(response.data)
      searchResultLoader.innerHTML = ''
      createCard(response.data.results.albummatches.album)
    })
}

searchInput.addEventListener('keyup', function (event) {
  if (event.key === 'Enter') {
    searchMusic()
  }
})
searchButton.addEventListener('click', function (event) {
  searchMusic()
})

const createCard = function (albums) {

  for (const album of albums) {
    const searchResultCard = document.createElement("a")
    searchResultCard.classList.add('search-result-card')
    searchResultCard.setAttribute('href', `${album.url}`)
    searchResult.appendChild(searchResultCard)

    const albumImg = document.createElement("img")
    albumImg.classList.add('album-image')
    if (album.image[2]['#text']) {
      albumImg.setAttribute('src', `${album.image[2]['#text']}`)
    } else {
      albumImg.setAttribute('src', 'https://op-js-music-search.netlify.app/assets/default.png')
    }

    searchResultCard.appendChild(albumImg)

    const albumDiscription = document.createElement("div")
    albumDiscription.classList.add('album-discription')
    searchResultCard.appendChild(albumDiscription)

    const albumTitle = document.createElement("p")
    albumTitle.classList.add('album-title')
    albumTitle.innerText = album.name
    albumDiscription.appendChild(albumTitle)

    const albumArtist = document.createElement("p")
    albumArtist.classList.add('album-artist')
    albumArtist.innerText = album.artist
    albumDiscription.appendChild(albumArtist)
  }
}