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
      series:[]
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
        </Container>
      </div>
    )
  }
}

export default App;
