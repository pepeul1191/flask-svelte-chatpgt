import { CSRF, BASE_URL } from '../configs/constants.js';

export const validate = (user, password) => {
  const requestOptions = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer yourAccessTokenHere',
      'RESTClient': 'webapp',
    },
    body: JSON.stringify({
      user: user,
      password: password
    })
  };
  // do request
  return fetch(`${BASE_URL}user/validate`, requestOptions)
    .then(response => {
      if (!response.ok) {
        return response.text().then(errorText => {
          console.error(response.status, errorText);
          throw new Error('Ha ocurrido un error no controlado');
        });
      } 
      return response.json();
    })
    .catch(error => {
      throw error; // Re-lanzar el error para manejarlo en el componente
    });
};

export const createFromLogin = (form) => {
  const requestOptions = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer yourAccessTokenHere',
    },
    body: JSON.stringify({
      username: form.user,
      password: form.password,
      email: form.email,
    })
  };
  // do request
  return fetch(`${BASE_URL}user/create`, requestOptions)
  .then(response => {
    if (!response.ok) {
      // Si la respuesta no es exitosa, lanzar un error
      return response.text().then(errorText => {
        console.error('Error en la respuesta:', errorText);
        throw new Error(errorText);
      });
    }
    // Analizar la respuesta JSON si es exitosa
    return response;
  })
  .then(data => {
    console.log('Respuesta recibida:', data);
    return data;
  })
    .catch(error => {
      console.log('CATCH')
      throw error;
    });
};

export const sendEmail = (email) => {
  const requestOptions = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer yourAccessTokenHere',
    },
    body: JSON.stringify({
      email: email,
    })
  };
  // do request
  return fetch(`${BASE_URL}user/reset-password`, requestOptions)
    .then(response => {
      if (!response.ok) {
        return response.text().then(errorText => {
          console.error(response.status, errorText);
          throw new Error('Ha ocurrido un error no controlado');
        });
      } 
      return response.json();
    })
    .catch(error => {
      throw error; // Re-lanzar el error para manejarlo en el componente
    });
};

export const loginCheck = () => {
  const requestOptions = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + localStorage.getItem('jwtToken'),
    },
    body: JSON.stringify({})
  };
  // do request
  return fetch(`${BASE_URL}user/login-check`, requestOptions)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .catch(error => {
      throw error; // Re-lanzar el error para manejarlo en el componente
    });
};
