import axios from 'axios';

export const getSession = () => {
  return new Promise((resolve, reject) => {
    axios.get('user/session', {
      params: {},
      headers:{
        'Client-Origin': 'webapp',
        'Content-Type': 'application/json',
      }
    }).then(function (response) {
      resolve(response);
    }).catch(function (error) {
      if(error.response.status == 404){
        console.error('Miembro no encontrado')
      }else{
        console.error(error.response.data);
      }
      reject(error.response);
    })
    .then(function () {
      // todo?
    });
  });
}

export const validateUser = (params) => {
  return new Promise((resolve, reject) => {
    axios.post('/user/validate', JSON.stringify(params), {
      headers: {
        'Client-Origin': 'webapp',
        'Content-Type': 'application/json',
      }
    }).then(function (response) {
      resolve(response);
    }).catch(function (error) {
      if(error.response.status == 404){
        console.error('Miembro a asociar no existe en el servidor')
      }else{
        console.error(error.response.data);
      }
      reject(error.response);
    })
    .then(function () {
      // todo?
    });
  });
}

export const createUser = (params) => {
  return new Promise((resolve, reject) => {
    axios.post('/user/create', JSON.stringify(params), {
      headers: {
        'Client-Origin': 'webapp',
        'Content-Type': 'application/json',
      }
    }).then(function (response) {
      resolve(response);
    }).catch(function (error) {
      if(error.response.status == 404){
        console.error('Miembro a asociar no existe en el servidor')
      }else{
        console.error(error.response.data);
      }
      reject(error.response);
    })
    .then(function () {
      // todo?
    });
  });
}

export const resetPassword = (params) => {
  return new Promise((resolve, reject) => {
    axios.post('/user/reset-password', JSON.stringify(params), {
      headers: {
        'Client-Origin': 'webapp',
        'Content-Type': 'application/json',
      }
    }).then(function (response) {
      resolve(response);
    }).catch(function (error) {
      if(error.response.status == 404){
        console.error('Miembro a asociar no existe en el servidor')
      }else{
        console.error(error.response.data);
      }
      reject(error.response);
    })
    .then(function () {
      // todo?
    });
  });
}
