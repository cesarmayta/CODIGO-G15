import { useState,useEffect } from 'react'
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Table,Container,Button,Form} from 'react-bootstrap';

import './App.css'

function App() {
  const [alumnos,setAlumnos] = useState([]);

  useEffect(()=>{
    axios.get('http://localhost:5000/alumno')
    .then(res=>{
      console.log(res.data);
      setAlumnos(res.data);
    })
  })

  return (
    <div className="App">
      <Container>
        <Table striped bordered hover variant="dark">
          <thead>
            <tr>
              <th>#</th>
              <th>Nombre</th>
              <th>Email</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {alumnos.map((alumno,index)=>{
              return (
                <tr key={alumno.alumno_id}>
                  <td>{alumno.alumno_id}</td>
                  <td>{alumno.alumno_nombre}</td>
                  <td>{alumno.alumno_email}</td>
                  <td>

                  </td>
                </tr>
              )
            })}
          </tbody>
        </Table>
      </Container>
    </div>
  )
}

export default App
