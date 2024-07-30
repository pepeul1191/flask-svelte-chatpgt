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
	<title>Crear Cuenta</title>
</svelte:head>

<div class="container mt-5">
  <div class="row justify-content-center mb-4">
    <Logo size=48 color='#0000002d'/>
  </div>
  <div class="row justify-content-center">
    <div class="col-md-4">
      <div class="card">
        <div class="card-header">
          <h3 class="text-center">Agregar Cuenta</h3>
        </div>
        <div class="card-body">
          <form>
            <div class="mb-3">
              <label for="username" class="form-label">Usuario</label>
              <input type="text" class="form-control" id="username" required>
            </div>
            <div class="mb-3">
              <label for="email" class="form-label">Correo Electrónico</label>
              <input type="email" class="form-control" id="email" required>
            </div>
            <div class="mb-3">
              <label for="password" class="form-label">Contraseña</label>
              <input type="password" class="form-control" id="password" required>
            </div>
            <div class="mb-3">
              <label for="confirm-password" class="form-label">Confirmar Contraseña</label>
              <input type="password" class="form-control" id="confirm-password" required>
            </div>
            <button type="submit" class="btn btn-primary w-100">Crear</button>
          </form>
          <div class="text-center mt-3 {messageClass}">
            {message}
          </div>
          <div class="text-center mt-3">
            <a class="navbar-brand" href="/login" on:click|preventDefault={() => {navigate('/login')}}>Ingresar</a>
            <span class="mx-2">|</span>
            <a class="navbar-brand" href="/reset-password" on:click|preventDefault={() => {navigate('/reset-password')}}>Recuperar Contraseña</a>
          </div>
        </div>
        <div class="card-footer text-center">
          <small>&copy; 2024 Your Brand</small>
        </div>
      </div>
    </div>
  </div>
</div>