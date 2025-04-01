<template>
  <div class="container">
    <h1>Busca de Empresas</h1>
    <div class="search-bar">
      <select v-model="searchType">
        <option value="name">Buscar por Nome</option>
        <option value="date">Buscar por Data</option>
        <option value="period">Buscar por Período</option>
      </select>

      <input
        v-if="searchType === 'name'"
        v-model="searchTerm"
        placeholder="Buscar transportadora..."
        @keyup.enter="searchCarriers" 
      />

      <input
        v-if="searchType === 'date'"
        v-model="date"
        type="date"
        placeholder="Escolha uma data"
      />

      <div v-if="searchType === 'period'">
        <input
          v-model="startDate"
          type="date"
          placeholder="Data de Início"
        />
        <input
          v-model="endDate"
          type="date"
          placeholder="Data de Fim"
        />
      </div>

      <button @click="searchCarriers">Buscar</button>
    </div>
    
    <div class="table-container">
      <table>
        <thead>
          <tr>
            <th>Nome Fantasia</th>
            <th>Razão Social</th>
            <th>Logradouro</th>
            <th>Número</th>
            <th>Bairro</th>
            <th>Cidade</th>
            <th>UF</th>
            <th>Telefone</th>
            <th>Email</th>
            <th>Modalidade</th>
            <th>Representante</th>
            <th>Registro ANS</th>
            <th>Data Registro ANS</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="carrier in carriers" :key="carrier.CNPJ">
            <td>{{ carrier.Nome_Fantasia || 'N/A' }}</td>
            <td>{{ carrier.Razao_Social }}</td>
            <td>{{ carrier.Logradouro }}</td>
            <td>{{ carrier.Numero }}</td>
            <td>{{ carrier.Bairro }}</td>
            <td>{{ carrier.Cidade }}</td>
            <td>{{ carrier.UF }}</td>
            <td>{{ carrier.Telefone }}</td>
            <td>{{ carrier.Endereco_eletronico }}</td>
            <td>{{ carrier.Modalidade }}</td>
            <td>{{ carrier.Representante }}</td>
            <td>{{ carrier.Registro_ANS }}</td>
            <td>{{ carrier.Data_Registro_ANS }}</td>
          </tr>
          <tr v-if="carriers.length === 0">
            <td colspan="13" class="no-results">Nenhum resultado encontrado</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      searchType: 'name', 
      searchTerm: '',
      date: '',
      startDate: '',
      endDate: '',
      carriers: []
    };
  },
  methods: {
    async searchCarriers() {
      let url = '';
      let params = {};

      if (this.searchType === 'name') {
        url = `http://127.0.0.1:5000/get?term=${this.searchTerm}`;
      } else if (this.searchType === 'date') {
        url = `http://127.0.0.1:5000/carriers/date`;
        params = { date: this.date };
      } else if (this.searchType === 'period') {
        url = `http://127.0.0.1:5000/carriers/period`;
        params = { start: this.startDate, end: this.endDate };
      }

      try {
        const response = await axios.get(url, { params });

if (Array.isArray(response.data)) {
  this.carriers = response.data; 
} else {
  console.error('Resposta inesperada:', response.data);
  this.carriers = [];
}
} catch (error) {
console.error('Erro ao buscar transportadoras:', error);
this.carriers = [];
}
}
}
};
</script>

<style scoped>
.container {
max-width: 1500px; 
margin: 0 auto;
padding: 20px;
}

h1 {
text-align: center;
margin-bottom: 20px;
}

.search-bar {
display: flex;
justify-content: center;
margin-bottom: 20px;
position: sticky;
top: 0; 
background-color: white; 
z-index: 1000;
}

select {
padding: 10px;
font-size: 16px;
margin-right: 10px;
}

input {
padding: 10px;
font-size: 16px;
border: 1px solid #ccc;
border-radius: 20px; 
box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); 
margin-right: 10px;
}

button {
padding: 10px 15px;
font-size: 16px;
background-color: #007bff;
color: white;
border: none;
border-radius: 4px;
cursor: pointer;
}

button:hover {
background-color: #0056b3;
}

.table-container {
overflow-x: auto; 
}

table {
width: 100%;
border-collapse: collapse;
table-layout: fixed; 
font-size: 14px; 
}

th {
background-color: #007bff; 
color: white; 
padding: 10px; 
position: sticky;
top: 0; 
z-index: 1000; 
}

th, td {
padding: 10px; 
border: 1px solid #ddd;
overflow: hidden; 
text-overflow: ellipsis; 
white-space: normal; 
word-wrap: break-word; 
}

td {
min-width: 100px; 
max-width: 200px; 
}

tr:nth-child(even) {
background-color: #f9f9f9; 
}

.no-results {
text-align: center;
color: #999;
font-style: italic;
}

@media (max-width: 600px) {
.search-bar {
flex-direction: column; 
}

input, select {
width: 100%; 
margin-bottom: 10px; 
}
}
</style>