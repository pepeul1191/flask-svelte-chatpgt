<script>
  import { onMount } from 'svelte';
  import * as XLSX from 'xlsx';
  
  export let message = {};
  export let conversationId = '';
  let data = [];
  let columns = [];
  let rows = [];

  // {"_id": ObjectId, "question": String, "answer": {"_id": "670807559d305cfce425ffb7", "query": "SELECT players.name AS player_name, nations.name AS nation_name \n      FROM players \n      JOIN nations ON players.nation_id = nations.id \n      WHERE players.sex_id = 1 LIMIT 100;", "result_set": []}, "error": false, "created": "2024-10-10T11:56:53.962988"}

  onMount(() => {
    columns = message.answer.columns;
    data = message.answer.result_set;
    setRows();
  });

  let pagination = {
    show: true,
    step: 10,
    page: 1,
    numberPages: 5
  };

  const setRows = () => {
    if (pagination.show) {
      rows = data.slice((pagination.page - 1) * pagination.step, pagination.page * pagination.step);
    } else {
      rows = data;
    }
  };

  // Llama a setRows cuando la página cambie
  $: setRows(); 

  const changeReport = () => {
    dispatch('changeReport');
  };

  const shareReport = () => {
    dispatch('shareReport');
  };

  const downloadReport = () => {
    const worksheet = XLSX.utils.json_to_sheet(data);
    const workbook = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(workbook, worksheet, 'reporte');
    XLSX.writeFile(workbook, `${conversationId} - ${new Date().getTime()}.xlsx`);
  };

  const handleStepChange = (event) => {
    pagination.step = +event.target.value;
    setRows();
  };

  const goBegin = () => {
    pagination.page = 1;
    setRows();
  };

  const goPrevious = () => {
    if (pagination.page > 1) {
      pagination.page--;
      setRows();
    }
  };

  const goNext = () => {
    if (pagination.page < pagination.numberPages) {
      pagination.page++;
      setRows();
    }
  };

  const goLast = () => {
    pagination.page = pagination.numberPages;
    setRows();
  };

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
    <p class="small">{formatDate(message.created_at)}</p>
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
      {#each rows as row}
      <tr>
        {#each columns as column}
          <td>{row[column]}</td>
        {/each}
      </tr>
      {/each}
    </tbody>
    <tfoot>
      <tr>
        <td colspan="20">
          <div class="row">
            <div class="col-sm-8">
              <button class="btn btn-secondary" on:click={changeReport} style="margin-right: 10px;">
                <i class="fa fa-line-chart" aria-hidden="true" style="margin-right: 5px;"></i>Presentación
              </button>
              <button class="btn btn-secondary" on:click={shareReport} style="margin-right: 10px;">
                <i class="fa fa-share-alt" aria-hidden="true" style="margin-right: 5px;"></i>Compartir
              </button>
              <button class="btn btn-secondary" on:click={downloadReport} style="margin-right: 10px;">
                <i class="fa fa-exclamation-triangle" aria-hidden="true" style="margin-right: 5px;"></i>Alerta
              </button>
              <button class="btn btn-secondary" on:click={downloadReport} style="margin-right: 10px;">
                <i class="fa fa-download" aria-hidden="true" style="margin-right: 5px;"></i>Descargar
              </button>
              <button class="btn btn-warning" on:click={downloadReport} style="margin-right: 10px;">
                <i class="fa fa-code" aria-hidden="true" style="margin-right: 5px;"></i>Editar
              </button>
              <button class="btn btn-danger" on:click={downloadReport} style="margin-right: 10px;">
                <i class="fa fa-times" aria-hidden="true" style="margin-right: 5px;"></i>Eliminar
              </button>
            </div>
            {#if pagination.show}
              <div class="col-sm-4" style="text-align: right;">
                <label style="margin-right: 10px;">Filas por página:</label>
                <select on:change={handleStepChange} value="10" class="pagination-select" style="">
                  <option value="10">10</option>
                  <option value="15">15</option>
                  <option value="20">20</option>
                  <option value="25">25</option>
                  <option value="30">30</option>
                  <option value="35">35</option>
                  <option value="40">40</option>
                </select>
                {#if pagination.page !== 1}
                  <i class="fa fa-angle-double-left footer-icon pagination-btn" on:click={goBegin} aria-hidden="true"></i>
                  <i class="fa fa-angle-left footer-icon pagination-btn" on:click={goPrevious} aria-hidden="true"></i>
                {/if}
                <label class="pagination-number">{pagination.page} / {pagination.numberPages}</label>
                {#if pagination.page !== pagination.numberPages}
                  <i class="fa fa-angle-right footer-icon pagination-btn" on:click={goNext} aria-hidden="true"></i>
                  <i class="fa fa-angle-double-right footer-icon pagination-btn" on:click={goLast} aria-hidden="true"></i>
                {/if}
              </div>
            {/if}
          </div>
        </td>
      </tr>
    </tfoot>    
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

  .pagination-select{
    border: 0px;
    background-color: transparent; 
    width: 65px; 
    height: 22px;
    text-align: center;
  }

  .pagination-select option{
    text-align: center;
  }

  .table>:not(caption)>*>* {
    padding: .35rem .5rem;
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

  .pagination-number{
    margin-left: 2.5px;
    margin-right: 2.5px;
    top: -2px;
    position: relative;
    font-weight: 600;
  }

  .pagination-btn:hover{
    cursor: pointer;
  }

  .pagination-btn{
    padding-left: 2.5px; 
    padding-right: 2.5px; 
    text-align: left;
    font-size: 20px;
    font-weight: 400;
  }
</style>