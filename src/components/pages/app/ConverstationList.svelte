<script>

import { onMount } from 'svelte';
import { navigate } from 'svelte-routing';
import axios from 'axios';

let conversations = [];
let generatedId;

onMount(() => {
  fetchAll();
  generateNewId();
});

const generateNewId = () => {
  const timestamp = (new Date().getTime() / 1000 | 0).toString(16);
  const oid = timestamp + 'xxxxxxxxxxxxxxxx'
    .replace(/[x]/g, _ => (Math.random() * 16 | 0).toString(16))
    .toLowerCase();
  generatedId  = oid;
};

const fetchAll = () => {
  axios.get('/api/v1/conversations')
    .then(response => {
      const data = response.data;
      console.log(data)
      conversations = data;
    })
    .catch(error => {
      console.error('Error en listar las conversaciones del usuario:', error);
    });
}

const deleteRow = (id) => {
  alert(id);
}
</script>

<style></style>

<svelte:head>
	<title>Gestión de Conversaciones</title>
</svelte:head>
  
<div class="mb-3">
  <h4>Gestión de Conversaciones</h4>
</div>
<!-- Table Element -->
<div class="card border-0">
  <div class="card-header">
    <h5 class="card-title">
      Conversaciones Pasadas
    </h5>
    <h6 class="card-subtitle text-muted">
    </h6>
  </div>
  <div class="card-body">
    <table class="table">
      <thead>
        <tr>
          <th scope="col">Nombre</th>
          <th scope="col">Cantidad de Mensajes</th>
          <th scope="col">Fecha de Creación</th>
          <th scope="col">Última Actualización</th>
          <th scope="col">Acciones</th>
        </tr>
      </thead>
      <tbody>
        {#each conversations as conversation}
          <tr>
            <td>{conversation.name}</td>
            <td>{conversation.message_count}</td>
            <td>{conversation.created_at}</td>
            <td>{conversation.updated_at}</td>
            <td>
              <a href="/conversations/{conversation._id}" on:click|preventDefault={navigate(`/conversations/${conversation._id}`)} class="btn btn-secondary"><i class="fa fa-comments-o" aria-hidden="true"></i>Continuar</a>
              <button on:click|preventDefault={deleteRow(conversation.id)} class="btn btn-danger"><i class="fa fa-times" aria-hidden="true"></i>Eliminar</button>
            </td>
          </tr>
        {/each}
      </tbody>
      <tfoot>
        <tr>
          <td colspan="10">
            <a href="/conversations/{generatedId}" on:click|preventDefault={() => navigate(`/conversations/${generatedId}`)} class="btn btn-success"><i class="fa fa-plus" aria-hidden="true"></i>Nueva Conversación</a>
          </td>
        </tr>
      </tfoot>
    </table>
  </div>
</div>