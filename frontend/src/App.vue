<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="app">
    <header>
      <div class="wrapper">
        <img alt="Global Tech logo" class="logo" src="@/assets/globalTech.png" />

        <nav>
          <RouterLink to="/">Início</RouterLink>
          <RouterLink to="/about">Sobre</RouterLink>
        </nav>
      </div>
    </header>
  
    <RouterView />
  </div>
</template>

<style>
body {
  background-color: whitesmoke;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0; 
}
</style>

<style scoped>

header {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
  width: 200px;
  height: auto;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
  display: flex;
}

nav a.router-link-exact-active {
  color: #0D72FF;
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
  color: #B7B7B7;
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
