<script>
  import { onMount } from 'svelte';
  import { navigate } from 'svelte-routing';
  import Logo from '../../svgs/Logo.svelte';
  
  let message = '';
  let messageClass = '';

  onMount(() => {

  });
</script>
<style></style>

<svelte:head>
	<title>Recuperar Contraseña</title>
</svelte:head>

<div class="container mt-5">
  <div class="row justify-content-center mb-4">
    <Logo size=48 color='#0000002d'/>
  </div>
  <div class="row justify-content-center">
    <div class="col-md-4">
      <div class="card">
        <div class="card-header">
          <h3 class="text-center">Olvidó su Contraseña</h3>
        </div>
        <div class="card-body">
          <form>
            <div class="mb-3">
              <label for="email" class="form-label">Correo Electrónico</label>
              <input type="email" class="form-control" id="email" required>
            </div>
            <button type="submit" class="btn btn-primary w-100">Enviar Correo</button>
          </form>
          <div class="text-center mt-3 {messageClass}">
            {message}
          </div>
          <div class="text-center mt-3">
            <a class="navbar-brand" href="/login" on:click|preventDefault={() => {navigate('/login')}}>Ingresar</a>
            <span class="mx-2">|</span>
            <a class="navbar-brand" href="/sign-up" on:click|preventDefault={() => {navigate('/sign-up')}}>Crear Cuenta</a>
          </div>
        </div>
        <div class="card-footer text-center">
          <small>&copy; 2024 Your Brand</small>
        </div>
      </div>
    </div>
  </div>
</div>