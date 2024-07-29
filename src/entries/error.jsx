import React from 'react';
import { Container, Row, Col, Button } from 'react-bootstrap';
import ReactDOM from 'react-dom/client';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../assets/css/error.css'; 

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
      <div class="col-md-12 d-flex align-items-center justify-content-center half-height">
        <h1 class="display-1 fw-bold error-heading">404</h1>
      </div>
      <div class="col-md-12 d-flex justify-content-center half-height background bg-dark">
        <div class="text-center">
          <p class="lead">Parece que has llegado a una página que no existe.</p>
          <a href="/" class="btn btn-light">
            <i class="fa fa-home"></i>
            Volver a la página principal
          </a>
        </div>
      </div>
    </div>
  </React.StrictMode>
)
