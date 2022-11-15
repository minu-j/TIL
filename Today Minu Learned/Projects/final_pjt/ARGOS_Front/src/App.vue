<template>
  <div id="app">
    <nav id="nav" class="navbar navbar-expand-sm navbar-dark">
      <div class="container-fluid">
        <router-link to="/home" class="navbar-brand" id="logo" href="">
          <img id="logo-img" src="@/assets/ARGOS_LOGO.png" alt="LOGO">
          <span>ARGOS</span>
        </router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <div class="nav-item--select">
                <div class="nav-item--select-bg"></div>
              </div>
              <router-link to="/home">Home</router-link>
            </li>
            <li class="nav-item">
              <div class="nav-item--select">
                <div class="nav-item--select-bg"></div>
              </div>
              <router-link to="/ticket">Ticket</router-link>
            </li>
            <li class="nav-item">
              <div class="nav-item--select">
                <div class="nav-item--select-bg"></div>
              </div>
              <router-link to="/play">Play</router-link>
            </li>
            <li class="nav-item">
              <div class="nav-item--select">
                <div class="nav-item--select-bg"></div>
              </div>
              <router-link to="/news">News</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<style lang="scss">
@import "@/style/reset.scss";
@import "@/App.scss";
</style>
