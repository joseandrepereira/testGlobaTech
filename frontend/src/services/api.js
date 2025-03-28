import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api/',
});

export const getPeople = () => api.get('people/');
export const createPerson = (person) => api.post('people/', person);
export const updatePerson = (id, person) => api.put(`people/${id}/`, person);
export const deletePerson = (id) => api.delete(`people/${id}/`);