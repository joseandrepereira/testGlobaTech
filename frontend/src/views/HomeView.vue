<!-- <script setup>
import TheWelcome from '../components/TheWelcome.vue'
</script>

<template>
  <main>
    <TheWelcome />
  </main>
</template> -->

<script>
import { getPeople, createPerson, deletePerson } from '@/services/api';

export default {
  name: 'HomeView',
  data() {
    return {
      people: [],
      newPerson: { name: '', age: '' },
    };
  },
  mounted() {
    this.fetchPeople();
  },
  methods: {
    async fetchPeople() {
      try {
        const response = await getPeople();
        this.people = response.data;
      } catch (error) {
        console.error('Error fetching people:', error);
      }
    },
    async addPerson() {
      try {
        await createPerson(this.newPerson);
        this.newPerson = { name: '', age: '' };
        this.fetchPeople();
      } catch (error) {
        console.error('Error adding person:', error);
      }
    },
    async deletePerson(id) {
      try {
        await deletePerson(id);
        this.fetchPeople();
      } catch (error) {
        console.error('Error deleting person:', error);
      }
    },
  },
};
</script>

<template>
  <div class="home">
    <h1>People List</h1>
    <ul>
      <li v-for="person in people" :key="person.id">
        {{ person.name }} ({{ person.age }} anos)
        <button @click="deletePerson(person.id)">Delete</button>
      </li>
    </ul>
    <form @submit.prevent="addPerson">
      <input v-model="newPerson.name" placeholder="Name" required />
      <input v-model.number="newPerson.age" type="number" placeholder="Age" required />
      <button type="submit">Add Person</button>
    </form>
  </div>
</template>

<style scoped>
.home {
  padding: 20px;
}
ul {
  list-style: none;
  padding: 0;
}
li {
  margin: 10px 0;
}
input {
  margin-right: 10px;
}
</style>