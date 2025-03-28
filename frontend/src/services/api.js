import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api/',
});

export const getPeople = (search = '') => api.get('people/', { params: { search } });
export const createPerson = (person) => api.post('people/', person);
export const updatePerson = (id, person) => api.put(`people/${id}/`, person);
export const deletePerson = (id) => api.delete(`people/${id}/`);
export const calculateIdealWeight = (id) => api.get(`people/${id}/calculate_ideal_weight/`);