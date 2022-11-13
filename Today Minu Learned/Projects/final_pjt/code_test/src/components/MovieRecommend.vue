<template>
  <div>
    <!-- 제목 -->
    <div id="movie-recommend-title-box">
      <div id="movie-recommend-title">{{ name }}님이 좋아하시는 액션 장르를 모아봤어요</div>
    </div>
      <!-- 캐러셀 -->
      <div id="movie-recommend-carousel" class="carousel slide" data-bs-ride="false" data-bs-interval="false" touch="true">
        <div class="carousel-inner" role="listbox">

          <!-- 영화 카드 -->
          <div v-for="(movie, index) in movies" :key="`movie-${index}`" class="carousel-item carousel-item--cursor">
            <div class="col-6 col-md-3 movie-recommend-card">
              <div class="movie-recommend-card-item">
                <span class="movie-recommend-card-title">{{ movie.title }}</span>
                <img class="image-thumbnail" :src="`${movie.thumbnail}`">
              </div>
            </div>
          </div>
        </div>

        <!-- 좌우 이동 버튼 -->
        <a class="carousel-control-prev" href="#movie-recommend-carousel" type="button" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        </a>
        <a class="carousel-control-next" href="#movie-recommend-carousel" type="button" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
        </a>
      </div>
    </div>
</template>

<script>
export default {
  name: 'MovieRecommend',
  data() {
    return {
      name: '홍길동',
      movies: [ // dummy data
        {
          title: '기생충',
          thumbnail: 'https://img.sbs.co.kr/newimg/news/20190623/201326992_1280.jpg',
        },
        {
          title: '모가디슈',
          thumbnail: 'https://cdn.mhns.co.kr/news/photo/202106/507026_611653_2147.jpg',
        },
        {
          title: '긴제목긴긴긴긴목이긴기긴긴기린목이긴기린제목',
          thumbnail: 'http://ojsfile.ohmynews.com/PHT_IMG_FILE/2018/0201/IE002279353_PHT.jpg',
        },
        {
          title: '1987',
          thumbnail: 'http://ojsfile.ohmynews.com/STD_IMG_FILE/2018/0108/IE002268886_STD.jpg',
        },
        {
          title: 'D.P.',
          thumbnail: 'https://img4.daumcdn.net/thumb/R658x0.q70/?fname=https://t1.daumcdn.net/news/202108/03/NEWS1/20210803095000690pbol.jpg',
        },
        {
          title: '수리남',
          thumbnail: 'http://woman.chosun.com/news/photo/202209/102404_93305_2622.jpg',
        },
      ],
    }
  },
  methods: {
    playCardVideo() {
      console.log(1)
    },
    stopCardVideo(n, x) {
      console.log(n, x)
    }
  },
  mounted() {
    // 캐러셀 생성
    const carouselItems = document.querySelectorAll('.carousel .carousel-item--cursor')
    
    carouselItems.forEach((item, index) => { // 영화 목록을 순회하며 각 캐러셀 페이지 생성하기
      if (index === 0) {   // 첫번째 캐러셀에는 active 클래스 추가
        item.classList.add('active')
      }
      const minPerSlide = 4   // 각 페이지에 보여질 최소 카드 갯수

      for (let i = 0; i < minPerSlide; i++) {   // 각 케러셀 페이지 생성하기(양끝 한개씩 겹치게 만들기)
        let nextItem = carouselItems[index + 1 + i]
        if (!nextItem) {
          nextItem = carouselItems[index + 1 + i - carouselItems.length]
        }
        let nextItemChild = nextItem.querySelector('div')
        let nextItemChildClone = nextItemChild.cloneNode(true)
        item.appendChild(nextItemChildClone)
      }

      // 각 카드에 이벤트 리스너 달아주기(캐러셀 안에 있는 태그는 v-on이 안먹히는데, 이유는 모르겠음..)
      const movieRecommendCardItem = item.querySelectorAll('.movie-recommend-card-item');
      movieRecommendCardItem.forEach((card) => {
        card.addEventListener('click', () => {
          console.log(card)
        })
      })
    })
  }
}
</script>

<style>
#movie-recommend-title-box {
  display: flex;
  justify-content: center;
}
#movie-recommend-title {
  text-align: left;
  padding-inline: 20px;
  width: 1080px;
  font-size: 24px;
  font-weight: bold;
}

.carousel-item--cursor {
  cursor: pointer;
}

.movie-recommend-card {
  height: 250px;
}

.movie-recommend-card-item {
  width: 90%;
  height: 80%;
  position: relative;
  top: 20px;
  left: 6%;
  border-radius: 20px;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 6px 12px -2px, rgba(0, 0, 0, 0.3) 0px 3px 7px -3px;
  transition: all 0.2s ease-out;
  display: flex;
  justify-content: center;
}
.movie-recommend-card-item:hover {
  transform: scale(1.05);
}

.movie-recommend-card-title {
  width: 80%;
  color: white;
  font-size: 24px;
  font-weight: bold;
  position: absolute;
  top: 80%;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  transition: all 0.2s ease-out;
  text-shadow: 2px 2px 5px rgba(35, 35, 35, 0.701)
}

.image-thumbnail {
    width:100%;
    object-fit:cover;
    border-radius: 20px;
}

/* 캐러셀 작동용 */
.carousel-inner .carousel-item.active,
.carousel-inner .carousel-item-next,
.carousel-inner .carousel-item-prev {
    display: flex;
    justify-content: center;
}

@media (max-width: 768px) {
    .carousel-inner .carousel-item-end.active,
    .carousel-inner .carousel-item-next {
      transform: translateX(50%);
    }
    .carousel-inner .carousel-item-start.active, 
    .carousel-inner .carousel-item-prev {
      transform: translateX(-50%);
    }
}

.carousel-inner .carousel-item-end,
.carousel-inner .carousel-item-start{ 
  transform: translateX(0);
}

@media (min-width: 768px) {
    .carousel-inner .carousel-item-end.active,
    .carousel-inner .carousel-item-next {
      transform: translateX(25%);
    }
    .carousel-inner .carousel-item-start.active, 
    .carousel-inner .carousel-item-prev {
      transform: translateX(-25%);
    }
}

.carousel-inner .carousel-item-end,
.carousel-inner .carousel-item-start{ 
  transform: translateX(0);
}
</style>