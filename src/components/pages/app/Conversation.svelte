<script>
  import { onMount } from 'svelte';
  import Prompt from "../../widgets/Prompt.svelte";
  import ConversationEntry from "../../widgets/ConversationEntry.svelte";

  export let _id = '';
  let conversationName = '';
  let conversationPlaceholder = '';
  let promptInstance;
  let conversationEntries = [];

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
  }); 

  const handleQuestionSent = (event) => {
    let message = event.detail;
    conversationEntries = [...conversationEntries, message];
  }
</script>

<svelte:head>
	<title>Nueva Conversación</title>
</svelte:head>

<div class="mb-3">
  <h4>Nueva Conversación</h4>
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
    </div>
  </div>
</div>

{#each conversationEntries as entry}
  <ConversationEntry message={entry}/>
{/each}

<Prompt 
  bind:this={promptInstance} 
  conversation={{_id: _id, name: conversationName}} 
  on:questionSent={handleQuestionSent}   
/>

<style>
</style>