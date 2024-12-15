<script>
  import { onMount } from 'svelte';
  import axios from 'axios';
  import Prompt from "../../widgets/Prompt.svelte";
  import ConversationEntry from "../../widgets/ConversationEntry.svelte";

  export let _id = '';
  let title = '';
  let conversationName = '';
  let conversationPlaceholder = '';
  let promptInstance;
  let conversationEntries = [];
  let messages = [];
  let actualQuestionIndex = 0;

  onMount(() => {
    const searchTopicPlaceholders = [
      '¿Cuál es el tema que quiere buscar?',
      'Ingrese el tema de su interés',
      '¿Sobre qué tema desea información?',
      'Escriba el tema que quiere explorar',
      '¿Qué área le gustaría investigar?',
      'Ingrese el tema que desea discutir',
      '¿Qué pregunta tiene sobre el tema?',
      'Indique el tema que le interesa',
      '¿De qué tema quiere saber más?',
      'Escriba el tema que le gustaría consultar'
    ];
    conversationPlaceholder = searchTopicPlaceholders[Math.floor(Math.random() * searchTopicPlaceholders.length)];

    if(conversationName == ''){
      
    }
    fetchOne();
  });
  
  const fetchOne = () => {
    axios.get(`/api/v1/conversations/${_id}`)
      .then(response => {
        const data = response.data;
        console.log(data)
        conversationEntries = data.messages;
        conversationName = data.name;
        conversationEntries = conversationEntries;
        actualQuestionIndex = conversationEntries.length;
        title = 'Continuar';
      })
      .catch(error => {
        console.log(error.response.status);
        console.error('Error en listar las conversaciones del usuario:', error);
        if(error.response.status == 404){
          title = 'Nueva';
        }
      });
  }

  const handleQuestionSent = (event) => {
    let message = event.detail;
    conversationEntries = [...conversationEntries, message];
    title = 'Continuar';
  }

  const searchUp = (event) => {
    if(actualQuestionIndex >= 0){
      if(actualQuestionIndex - 1 > 0){
        actualQuestionIndex--;
        const q = conversationEntries[actualQuestionIndex].question;
        promptInstance.question = q
      }
    }
  }

  const searchDown = (event) => {
    if(actualQuestionIndex < conversationEntries.length){
      if(actualQuestionIndex + 1 < conversationEntries.length){
        actualQuestionIndex++;
        const q = conversationEntries[actualQuestionIndex].question;
        promptInstance.question = q
      }else if(actualQuestionIndex < conversationEntries.length){
        promptInstance.question = ''
      }
    }
  }

  const updateName = () => {
    
  }
</script>

<svelte:head>
	<title>{title} Conversación</title>
</svelte:head>

<div class="mb-3">
  <h4>{title} Conversación</h4>
</div>

<div class="row">
  <div class="col">
    <div class="input-group mb-3">
      <span class="input-group-text">Nombre de la Conversación</span>
      <input
        type="text"
        class="form-control"
        placeholder="{conversationPlaceholder}"
        aria-label=""
        aria-describedby="button-send"
        bind:value={conversationName}
      />
      <button class="btn btn-success" id="button-send" style="width: 120px;" on:click={updateName} >
        <i class="fa fa-check" aria-hidden="true" style="margin-right: 5px;"></i>
        Guardar
      </button>
    </div>
  </div>
</div>

{#each conversationEntries as entry}
  <ConversationEntry message={entry} conversation_id={_id} />
{/each}

<Prompt 
  bind:this={promptInstance} 
  conversation={{_id: _id, name: conversationName}} 
  on:questionSent={handleQuestionSent}  
  on:searchUp={searchUp}
  on:searchDown={searchDown} 
/>

<style>
</style>