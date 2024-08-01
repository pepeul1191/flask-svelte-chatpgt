<script>
  import { navigate } from 'svelte-routing';
  import { dataStore } from '../../stores/session_stores';
  import { onMount } from 'svelte';
  
  let session;

  const signOut = (e) => {
    let name = 'authToken';
    document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/; secure; samesite=strict`;
    window.location.replace('/user/sign-out');
  }

  onMount(() => {
    dataStore.subscribe(value => {
      console.log(value);
      if(value != null){
        session = value
      }
    })
  });
</script>

<style></style>

<nav class="navbar navbar-expand px-3 border-bottom">
  <button class="btn" id="sidebar-toggle" type="button">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="navbar-collapse navbar">
    <ul class="navbar-nav">
      <li class="nav-item dropdown">
        <a href="/" data-bs-toggle="dropdown" class="nav-icon pe-md-0">
          <!-- Verificar si session y session.jwt están definidos -->
          {#if session && session.image_url}
            <img src="{session.image_url}" class="avatar img-fluid rounded" alt="">
          {:else}
            <img src="/assets/img/profile.jpg" class="avatar img-fluid rounded" alt="">
          {/if}
        </a>
        <div class="dropdown-menu dropdown-menu-end">
          <a class="dropdown-item" href="/profile" on:click|preventDefault={() => {navigate('/profile')}}>
            Mi Perfil
          </a>
          <a href="/" class="dropdown-item">Setting</a>
          <a class="dropdown-item" on:click|preventDefault={signOut} href="/user/sign-out">Salir</a>
        </div>
      </li>
    </ul>
  </div>
</nav>