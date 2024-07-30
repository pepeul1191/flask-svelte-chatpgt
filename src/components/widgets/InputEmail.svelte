<script>
  export let value = "";
  export let label = "";
  export let id = "";
  export let validations = [];
  let isValid = true;
  let message = '';

  export const validate = () => {
    message = ''; 
    validations.forEach(validation => {
      // validation
      if(validation.type == 'notEmpty'){
        if (value.trim() === ''){
          message = validation.message || 'Debe de llenar este campo';
          isValid = false;
        }else{
          isValid = true;
        }
      }
      if(isValid && validation.type == 'maxLength'){
        //console.log('emptyOrMaxLength')
        if(value.length > validation.length){
          message = validation.message || 'Superó la cantidad máxima de caracteres';
          isValid = false;
        }else{
          isValid = true;
        }
      }
      /*
      if(isValid && validation.type == 'custom'){
        validation.func(value).then(resp => {
          if(resp == false){
            validationMessage = validation.message;
            valid = false;
            validationMessageClass = 'text-danger';
          }else{
            validationMessage = '';
            validationMessageClass = '';
            valid = true;
          }
        });
      }
      */
      if(isValid && validation.type == 'email'){
        var regex = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        if(regex.test(value) == false){
          message = validation.message || 'Correo no válido';
          isValid = false;
        }else{
          isValid = true;
        }
      }
    });
  };
</script>

<div>
  <label for={id} class="form-label">{label}</label>
  <input
    type="email"
    class="form-control { !isValid ? 'is-invalid' : '' }"
    id={id}
    bind:value={value}
    required
    on:input={validate} >
  {#if isValid == false}
    <div class="{ !isValid ? 'text-danger' : '' }">
      {message}
    </div>
  {/if}
</div>

<style>
  /* Aquí puedes agregar estilos personalizados si es necesario */

  .is-invalid {
    border-color: #dc3545;
  }

  .text-danger{
    margin-top: 5px;
    color: #842029;
  }
</style>
