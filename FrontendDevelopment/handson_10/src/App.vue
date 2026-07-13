<template>
  <Header />
  <router-view />
</template>

<script setup>
import Header from "./components/Header.vue";
</script>

<style>
body{
  margin:0;
  font-family:Arial, Helvetica, sans-serif;
  background:#f5f7fb;
}
</style>