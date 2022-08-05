import { useState,useEffect } from 'react'
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Table,Container,Button,Form} from 'react-bootstrap';

import './App.css'

function App() {
  const [alumnos,setAlumnos] = useState([]);
  const [nombre,setNombre] = useState('');
  const [email,setEmail] = useState('');


  useEffect(()=>{
    axios.get('http://localhost:5000/alumno')
    .then(res=>{
      console.log(res.data);
      setAlumnos(res.data);
    })
  },[]);

  function guardar(e){
    e.preventDefault();
    let datos = {
      nombre:nombre,
      email:email
    }
    axios.post('http://localhost:5000/alumno',datos)
    .then(res=>{
      var temp = alumnos;
      temp.push(res.data);
      setNombre('');
      setEmail('');
      setAlumnos(temp);
    }).catch((error)=>{
      console.log(error.toString());
    })
  }

  function eliminar(cod){
    let rpta = window.confirm("esta seguro?");
    if (rpta){
      axios.delete('http://localhost:5000/alumno/'+cod)
      .then(res=>{
        var temp = alumnos.filter((alumno)=> alumno.alumno_id !== cod);
        setAlumnos(temp);
      })
    }
  }

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
                  <Button variant="danger" onClick={()=>eliminar(alumno.alumno_id)}>Eliminar</Button>
                  </td>
                </tr>
              )
            })}
          </tbody>
        </Table>
        <br/>
        <Form onSubmit={guardar}>
          <Form.Group className='mb-3'>
            <Form.Label>Nombre:</Form.Label>
            <Form.Control type="text" value={nombre} onChange={(e)=> setNombre(e.target.value)} />
          </Form.Group>
          <Form.Group className='mb-3'>
            <Form.Label>Email:</Form.Label>
            <Form.Control type="text" value={email} onChange={(e)=> setEmail(e.target.value)} />
          </Form.Group>
          <Button variant="primary" type="submit">
            GUARDAR
          </Button>
        </Form>
      </Container>
    </div>
  )
}

export default App
