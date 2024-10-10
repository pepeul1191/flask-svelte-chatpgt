<script>
  import axios from 'axios';
  export let conversation_id = '';
  let question = '';

  const sendQuestionClick = () => {
    // Realizar la solicitud POST
    axios.post('/api/v1/question', {
      question: question,
      conversation_id: conversation_id,
    })
    .then(response => {
      console.log('Pregunta enviada:', response.data);
      // Aquí puedes manejar la respuesta, como limpiar el input
      questionInput.value = ''; // Limpiar el input
    })
    .catch(error => {
      console.error('Error al enviar la pregunta:', error);
      // Aquí puedes manejar el error
    });
  }
</script>

<div class="mb-5">
  <div class="input-group">
    <input
      type="text"
      class="form-control"
      placeholder="Cuál es su pregunta?"
      aria-label="Cuál es su pregunta?"
      aria-describedby="button-send"
      id="question-input"
      bind:value={question} 
    />
    <button
      class="btn btn-primary"
      id="button-send"
      style="width: 120px;"
      on:click={sendQuestionClick} 
    >
      <i class="fa fa-paper-plane-o" aria-hidden="true" style="margin-right: 5px;"></i>
      Enviar
    </button>
  </div>
</div>

<style>

</style>