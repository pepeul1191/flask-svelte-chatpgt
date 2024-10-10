<script>

import { onMount } from 'svelte';
import { navigate } from 'svelte-routing';
let levels = [];
let generatedId;

onMount(() => {
  fetchLevels();
  generateNewId();
});

const generateNewId = () => {
  const timestamp = (new Date().getTime() / 1000 | 0).toString(16);
  const oid = timestamp + 'xxxxxxxxxxxxxxxx'
    .replace(/[x]/g, _ => (Math.random() * 16 | 0).toString(16))
    .toLowerCase();
  generatedId  = oid;
};

const fetchLevels = (map) => {
  fetch(`/level/list`)
    .then(response => {
      if (!response.ok) {
        throw new Error('Error en la solicitud: ' + response.status);
      }
      return response.json(); // Convertir la respuesta a JSON
    })
    .then(data => {
      levels = data; // Asignar la respuesta a la variable levels
    })
    .catch(error => {
      console.error('Error en la solicitud:', error);
    });
}

const deleteLevel = (id) => {
  alert(id);
}
</script>

<style></style>

<svelte:head>
	<title>Gestión de Conversaciones</title>
</svelte:head>
  
<div class="mb-3">
  <h4>Gestión de Conversaciones</h4>
  <a href="/conversations/{generatedId}" on:click|preventDefault={() => navigate(`/conversations/${generatedId}`)} class="btn btn-success"><i class="fa fa-plus" aria-hidden="true"></i>Nueva Conversación</a>
</div>
<!-- Table Element -->
<div class="card border-0">
  <div class="card-header">
    <h5 class="card-title">
        Niveles de las rutinas
    </h5>
    <h6 class="card-subtitle text-muted">
    </h6>
  </div>
  <div class="card-body">
    <table class="table">
      <thead>
        <tr>
          <th scope="col">Nombre</th>
          <th scope="col">Acciones</th>
        </tr>
      </thead>
      <tbody>
        {#each levels as level}
          <tr>
            <td>{level.name}</td>
            <td>
              <a href="/admin/level/edit/{level.id}" on:click|preventDefault={navigate(`/admin/level/edit/${level.id}`)} class="btn btn-danger">Editar</a>
              <button on:click|preventDefault={deleteLevel(level.id)} class="btn btn-secondary">Eliminar</button>
            </td>
          </tr>
        {/each}
      </tbody>
    </table>
  </div>
</div>