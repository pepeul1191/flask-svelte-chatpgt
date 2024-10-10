<script>
  import { onMount } from 'svelte';
  
  export let message = {};
  let data = [];
  let columns = [];

  // {"_id": ObjectId, "question": String, "answer": {"_id": "670807559d305cfce425ffb7", "query": "SELECT players.name AS player_name, nations.name AS nation_name \n      FROM players \n      JOIN nations ON players.nation_id = nations.id \n      WHERE players.sex_id = 1 LIMIT 100;", "result_set": []}, "error": false, "created": "2024-10-10T11:56:53.962988"}

  onMount(() => {
    columns = message.answer.columns;
    data = message.answer.result_set;
  });

  const formatDate = (dateString) => {
    const date = new Date(dateString); 
    const hours = String(date.getHours()).padStart(2, '0');
    const minutes = String(date.getMinutes()).padStart(2, '0');
    const seconds = String(date.getSeconds()).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    const month = String(date.getMonth() + 1).padStart(2, '0'); // Los meses son de 0 a 11
    const year = date.getFullYear();
    return `${hours}:${minutes}:${seconds} - ${day}/${month}/${year}`;
  }
</script>

<div class="row question-row">
  <span class="card question-card border-0 conversations">
    {message.question}<br>
    <p class="small">{formatDate(message.created)}</p>
  </span>
</div>

<div class="card border-0 conversations">
  <table class="table table-striped">
    <thead>
      <tr>
        {#each columns as column}
          <th>{column}</th>
        {/each}
      </tr>
    </thead>
    <tbody>
      {#each data as record}
      <tr>
        {#each columns as column}
          <td>{record[column]}</td>
        {/each}
      </tr>
      {/each}
    </tbody>
  </table>
</div>

<style>
  .conversations {
    flex: 1; /* Toma el espacio disponible */
    padding: 20px;
  }

  .card{
    padding: 10px;
    padding-left: 25px;
    padding-right: 25px;
  }

  .question-row{
    padding-left: 10px;
    padding-right: 10px;
  }

  .question-card{
    display: inline-block; 
    text-align: right;
    border: 0px solid !important;
    background-color: #F0F0F0 !important;
    padding-right: 30px;
  }

  .small, small {
    margin-bottom: 0px !important;
    font-weight: 500;
  }
</style>