<script lang="ts">
import { onMount } from 'svelte';
import { Router, Route } from 'svelte-routing';
import Sidebar from '../widgets/Sidebar.svelte';
import Navbar from '../widgets/Navbar.svelte';
import ThemeToggle from '../widgets/ThemeToggle.svelte';
import Footer from '../widgets/Footer.svelte';
import Home from '../pages/app/Home.svelte';
import Level from '../pages/app/Level.svelte';
import ConversationList from '../pages/app/ConverstationList.svelte';
import Profile from '../pages/app/Profile.svelte';
import { getSession } from '../../services/user_service.js';
import { dataStore } from '../../stores/session_stores.js';

export let basepath = '/';

onMount(() => {
  const sidebarToggle = document.querySelector('#sidebar-toggle');
  if (sidebarToggle) {
    sidebarToggle.addEventListener('click', () => {
      document.querySelector('#sidebar').classList.toggle('collapsed');
    });
  }
  getSession().then((resp) => {
    console.log(resp)
    dataStore.set(resp.data.jwt);
    console.log(dataStore)
  }).catch((resp) =>  {
    console.error(resp.status)
    console.error(resp)
  })
});
</script>

<style></style>

<div class="wrapper">
  <Sidebar />
  <div class="main">
    <Navbar />
    <main class="content px-3 py-2">
      <div class="container-fluid">
        <Router basepath="{basepath}">
          <Route path="/" component={Home} />
          <Route path="/level" component={Level} />
          <Route path="/profile" component={Profile} />
          <Route path="/conversations" component={ConversationList} />
        </Router>
      </div>
    </main>
    <ThemeToggle />
    <Footer />
  </div>
</div>

