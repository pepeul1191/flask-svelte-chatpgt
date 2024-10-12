<svelte:options accessors={true} />
<script>
  import axios from 'axios';
  import { createEventDispatcher } from 'svelte';
  export let conversation = {};

  export let question = '';
  const dispatch = createEventDispatcher();

  const sendQuestionClick = () => {
    axios.post('/api/v1/questions', {
      question: question,
      conversation: conversation,
    })
    .then(response => {
      response.data.quiestion = question;
      dispatch('questionSent', response.data);
      question = '';
    })
    .catch(error => {
      console.error('Error al enviar la pregunta:', error);
      // Aquí puedes manejar el error
    });
  }

  const handleKeyDown = (event) => {
    if (event.key === 'ArrowUp') {
      dispatch('searchUp');
    } else if (event.key === 'ArrowDown') {
      dispatch('searchDown');
    }
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
      on:keydown={handleKeyDown}
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