<script>
import { getPeople, createPerson, updatePerson, deletePerson, calculateIdealWeight } from '@/services/api';

export default {
  name: 'HomeView',
  data() {
    return {
      peopleList: [],
      newPerson: {
        name: '',
        birthday_date: '',
        cpf: '',
        sex: '',
        height: '',
        weight: '',
      },
      searchQuery: '',
      editingPerson: null,
    };
  },
  mounted() {
    this.fetchPeople();
  },
  watch: {
    searchQuery(newValue) {
      this.fetchPeople(newValue); // Busca no backend com o novo valor
    },
  },
  methods: {
    async fetchPeople(search = '') {
      try {
        const response = await getPeople(search);
        this.peopleList = response.data;
      } catch (error) {
        console.error('Erro ao buscar pessoas:', error);
      }
    },
    async addPerson() {
      try {
        const formattedPerson = {
          ...this.newPerson,
          cpf: this.newPerson.cpf.replace(/\D/g, ''),
          birthday_date: this.formatDateForAPI(this.newPerson.birthday_date),
        };
        await createPerson(formattedPerson);
        this.newPerson = {
          name: '',
          birthday_date: '',
          cpf: '',
          sex: '',
          height: '',
          weight: '',
        };
        this.fetchPeople(this.searchQuery); // Mantém a pesquisa atual
      } catch (error) {
        console.error('Erro ao adicionar pessoa:', error);
      }
    },
    async updatePerson(person) {
      try {
        const formattedPerson = {
          ...person,
          cpf: person.cpf.replace(/\D/g, ''),
          birthday_date: this.formatDateForAPI(person.birthday_date),
        };
        await updatePerson(person.id, formattedPerson);
        this.editingPerson = null;
        this.fetchPeople(this.searchQuery); // Mantém a pesquisa atual
      } catch (error) {
        console.error('Erro ao atualizar pessoa:', error);
      }
    },
    async deletePerson(id) {
      if (confirm('Tem certeza que deseja excluir esta pessoa?')) {
        try {
          await deletePerson(id);
          this.fetchPeople(this.searchQuery);
        } catch (error) {
          console.error('Erro ao excluir pessoa:', error);
        }
      }
    },
    async calculateIdealWeight(id) {
      try {
        const response = await calculateIdealWeight(id);
        const idealWeight = response.data.ideal_weight.toFixed(2);
        alert(`Peso Ideal: ${idealWeight} kg`);
      } catch (error) {
        console.error('Erro ao calcular peso ideal:', error);
        alert('Erro ao calcular o peso ideal. Verifique se o campo "Altura" está preenchido');
      }
    },
    startEditing(person) {
      this.editingPerson = {
        ...person,
        birthday_date: this.formatDateForDisplay(person.birthday_date),
        cpf: this.formatCPF(person.cpf),
      };
    },
    cancelEditing() {
      this.editingPerson = null;
    },
    formatCPF(value) {
      if (!value) return '';
      const cleaned = value.replace(/\D/g, '').slice(0, 11);
      return cleaned
        .replace(/(\d{3})(\d)/, '$1.$2')
        .replace(/(\d{3})(\d)/, '$1.$2')
        .replace(/(\d{3})(\d{1,2})$/, '$1-$2');
    },
    formatDateForDisplay(value) {
      if (!value) return '';
      const [year, month, day] = value.split('-');
      return `${day}/${month}/${year}`;
    },
    formatDateForAPI(value) {
      if (!value) return null;
      const [day, month, year] = value.split('/');
      return `${year}-${month}-${day}`;
    },
    handleCPFInput(event, target) {
      target.cpf = this.formatCPF(event.target.value);
    },
    handleDateInput(event, target) {
      const value = event.target.value.replace(/\D/g, '').slice(0, 8);
      if (value.length > 2) {
        target.birthday_date = value.replace(/(\d{2})(\d)/, '$1/$2').replace(/(\d{2})(\d)/, '$1/$2');
      } else {
        target.birthday_date = value;
      }
    },
  },
};
</script>

<template>
  <div class="home">
    <h1>Adicionar Pessoa</h1>

    <!-- Formulário para adicionar -->
    <form @submit.prevent="addPerson" class="add-form">
      <input v-model="newPerson.name" placeholder="Nome" required />
      <input
        v-model="newPerson.birthday_date"
        @input="handleDateInput($event, newPerson)"
        placeholder="Data de Nascimento (DD/MM/AAAA)"
        maxlength="10"
      />
      <input
        v-model="newPerson.cpf"
        @input="handleCPFInput($event, newPerson)"
        placeholder="CPF (000.000.000-00)"
        maxlength="14"
      />
      <select v-model="newPerson.sex" required>
        <option value="" disabled>Sexo</option>
        <option value="m">Masculino</option>
        <option value="f">Feminino</option>
      </select>
      <input v-model.number="newPerson.height" type="number" step="0.01" placeholder="Altura (m)" />
      <input v-model.number="newPerson.weight" type="number" step="0.1" placeholder="Peso (kg)" />
      <button type="submit">Adicionar</button>
    </form>

    <h1>Lista de Pessoas</h1>
    <!-- Campo de pesquisa -->
    <input v-model="searchQuery" placeholder="Pesquisar por nome ou CPF" class="search-input" />

    <!-- Tabela -->
    <table>
      <thead>
        <tr>
          <th>Id</th>
          <th>Nome</th>
          <th>Data de Nascimento</th>
          <th>CPF</th>
          <th>Sexo</th>
          <th>Altura (m)</th>
          <th>Peso (kg)</th>
          <th>Ações</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="person in peopleList" :key="person.id">
          <td>{{ person.id }}</td>
          <td v-if="editingPerson?.id === person.id">
            <input v-model="editingPerson.name" />
          </td>
          <td v-else>{{ person.name }}</td>

          <td v-if="editingPerson?.id === person.id">
            <input
              v-model="editingPerson.birthday_date"
              @input="handleDateInput($event, editingPerson)"
              maxlength="10"
            />
          </td>
          <td v-else>{{ formatDateForDisplay(person.birthday_date) }}</td>

          <td v-if="editingPerson?.id === person.id">
            <input
              v-model="editingPerson.cpf"
              @input="handleCPFInput($event, editingPerson)"
              maxlength="14"
            />
          </td>
          <td v-else>{{ formatCPF(person.cpf) }}</td>

          <td v-if="editingPerson?.id === person.id">
            <select v-model="editingPerson.sex">
              <option value="m">Masculino</option>
              <option value="f">Feminino</option>
            </select>
          </td>
          <td v-else>{{ person.sex === 'm' ? 'Masculino' : 'Feminino' }}</td>

          <td v-if="editingPerson?.id === person.id">
            <input v-model.number="editingPerson.height" type="number" step="0.01" />
          </td>
          <td v-else>{{ person.height }}</td>

          <td v-if="editingPerson?.id === person.id">
            <input v-model.number="editingPerson.weight" type="number" step="0.1" />
          </td>
          <td v-else>{{ person.weight }}</td>

          <td>
            <button v-if="editingPerson?.id === person.id" @click="updatePerson(editingPerson)">
              Salvar
            </button>
            <button v-if="editingPerson?.id === person.id" @click="cancelEditing">Cancelar</button>
            <span v-else>
              <button @click="startEditing(person)">Alterar</button>
              <button @click="deletePerson(person.id)">Excluir</button>
            </span>
            <button v-if="!editingPerson?.id" @click="calculateIdealWeight(person.id)">
              Peso Ideal
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
.home {
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
}

h1 {
  color: #676c73;
}

.add-form {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.add-form input,
.add-form select {
  padding: 5px;
}

.search-input {
  width: 100%;
  padding: 8px;
  margin-bottom: 20px;
}

table {
  width: 100%;
  border-collapse: collapse;
}

thead tr {
  color: #000;
  background-color: brown;
}

th,
td {
  padding: 10px;
  text-align: left;
  border-bottom: 1px solid #ddd;
  color: black;
}

th {
  background-color: #0f73ff;
  color: #fff;
  font-weight: 500;
}

button {
  padding: 5px 10px;
  margin-right: 5px;
  margin-bottom: 5px;
  cursor: pointer;
}
</style>