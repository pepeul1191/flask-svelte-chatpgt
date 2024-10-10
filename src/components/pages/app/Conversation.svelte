<script>
import Prompt from "../../widgets/Prompt.svelte";


export let _id = '';
let promptInstance;

</script>

<svelte:head>
	<title>Nueva Conversación</title>
</svelte:head>

<div class="mb-3">
  <h4>Nueva Conversación {_id}</h4>
</div>


<div class="card border-0 conversations">
  hola
</div>

<Prompt bind:this={promptInstance} conversation_id={_id}/>

<style>
  .conversations {
    flex: 1; /* Toma el espacio disponible */
  }
</style>