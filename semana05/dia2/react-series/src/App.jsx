import React,{Component} from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import Table from 'react-bootstrap/Table';
import Container from 'react-bootstrap/Container';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';

class App extends Component{
  constructor(props){
    super(props);
    this.state = ({
      series:[],
      pos:null,
      titulo:'Nuevo',
      id:0,
      nombre:'',
      fecha:'',
      rating:'0',
      categoria:''
    })
    this.cambioNombre = this.cambioNombre.bind(this);
    this.cambioFecha = this.cambioFecha.bind(this);
    this.cambioRating = this.cambioRating.bind(this);
    this.cambioCategoria = this.cambioCategoria.bind(this);
    this.guardar = this.guardar.bind(this);
  }

  cambioNombre(e){
    //console.log("nombre : " + e.target.value);
    this.setState({
      nombre : e.target.value
    })
  }

  cambioFecha(e){
    //console.log("nombre : " + e.target.value);
    this.setState({
      fecha : e.target.value
    })
  }

  cambioRating(e){
    //console.log("nombre : " + e.target.value);
    this.setState({
      rating : e.target.value
    })
  }

  cambioCategoria(e){
    //console.log("nombre : " + e.target.value);
    this.setState({
      categoria : e.target.value
    })
  }

  componentDidMount(){
    axios.get('http://localhost:8000/serie/')
    .then(res =>{
      console.log(res.data)
      this.setState({
        series: res.data
      })
    })
  }

  guardar(e){
    e.preventDefault();
    const datos = {
      nombre:this.state.nombre,
      fecha_registro:this.state.fecha,
      rating:this.state.rating,
      categoria:this.state.categoria
    }

    axios.post('http://localhost:8000/serie/',datos)
    .then(res=>{
      this.state.series.push(res.data);
      var temp = this.state.series;
      this.setState({
        id:0,
        nombre:'',
        fecha:'',
        rating:0,
        categoria:'',
        series:temp
      });
    }).catch((error)=>{
      console.log(error.toString());
    })
  }

  render(){
    return(
      <div>
        <Container>
        <h1>Series</h1>
        <Table striped bordered hover variant="dark">
          <thead>
            <tr>
              <th>#</th>
              <th>Nombre</th>
              <th>Fecha</th>
              <th>Rating</th>
              <th>Categoria</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {this.state.series.map((serie,index)=>{
              return(
                <tr key={serie.id}>
                  <td>{serie.id}</td>
                  <td>{serie.nombre}</td>
                  <td>{serie.fecha_registro}</td>
                  <td>{serie.rating}</td>
                  <td>{serie.categoria}</td>
                  <td></td>
                </tr>
              )
            })}
          </tbody>
        </Table>
        <br/>
        <h1>Nueva Serie</h1>
        <Form onSubmit={this.guardar}>
          <Form.Group className='mb-3'>
            <Form.Label>Nombre:</Form.Label>
            <Form.Control type="text" value={this.state.nombre} onChange={this.cambioNombre}/>
          </Form.Group>
          <Form.Group className='mb-3'>
            <Form.Label>Fecha:</Form.Label>
            <Form.Control type="text" value={this.state.fecha} onChange={this.cambioFecha}/>
          </Form.Group>
          <Form.Group className='mb-3'>
            <Form.Label>Rating:</Form.Label>
            <Form.Control type="text" value={this.state.rating} onChange={this.cambioRating}/>
          </Form.Group>
          <Form.Group className='mb-3'>
            <Form.Label>Categoria:</Form.Label>
            <Form.Control type="text" value={this.state.categoria} onChange={this.cambioCategoria}/>
          </Form.Group>
          <Button variant="primary" type="submit">
            Guardar
          </Button>
        </Form>
        </Container>
      </div>
    )
  }
}

export default App;
