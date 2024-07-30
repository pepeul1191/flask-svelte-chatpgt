<script>
  import { onMount } from 'svelte';
  import { navigate } from 'svelte-routing';
  import Logo from '../../svgs/Logo.svelte';
  import InputText from '../../widgets/InputText.svelte';
  import InputPassword from '../../widgets/InputPassword.svelte';

  let username = ''; let usernameInput;
  let password = ''; let passwordInput;
  let message = '';
  let messageClass = '';
  
  onMount(() => {

  });

  const access = (event) => {
    event.preventDefault();
    // run validations
    usernameInput.validate();
    passwordInput.validate();
    // if ok, ajax
    if(usernameInput.isValid && passwordInput.isValid){
      alert('AJAX');
    }
  }
</script>
<style>

</style>

<svelte:head>
	<title>Ingresar al Sistema</title>
</svelte:head>
<div class="container mt-5">
  <div class="row justify-content-center mb-4">
    <Logo size=48 color='#0000002d'/>
  </div>
  <div class="row justify-content-center">
    <div class="col-md-4">
      <div class="card">
        <div class="card-header">
          <h3 class="text-center">Bienvenido</h3>
        </div>
        <div class="card-body">
          <form>
            <div class="mb-3">
              <!-- 
              <label for="username" class="form-label">Usuario</label>
              <input type="text" class="form-control" id="username" required bind:value={user}>
              -->
              <InputText 
                id="username" 
                label="Usuario" 
                bind:value={username} 
                bind:this={usernameInput}
                onInputValidation={false}
                validations = {[
                  {type: 'notEmpty', message: 'Ingresar un usuario'},
                ]} />
            </div>
            <div class="mb-3">
              <InputPassword 
                id="password" 
                label="Contraseña" 
                bind:value={password} 
                bind:this={passwordInput}
                onInputValidation={false}
                validations = {[
                  {type: 'notEmpty', message: 'Ingresar una contraseña'},
                ]} />
            </div>
            <button  class="btn btn-primary w-100" on:click={access}>Ingresar</button>
          </form>
          <div class="text-center mt-3 {messageClass}">
            {message}
          </div>
          <div class="text-center mt-3">
            <a class="navbar-brand" href="/reset-password" on:click|preventDefault={() => {navigate('/reset-password')}}>Recuperar Contraseña</a>
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