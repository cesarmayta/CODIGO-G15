import React,{Component} from 'react';
import axios from 'axios';

class App extends Component{
  constructor(props){
    super(props);
    this.state = ({
      alumnos : []
    })
  }

  componentDidMount(){
    axios.get('http://localhost:5000/alumno')
    .then(res=>{
      console.log(res.data.content);
    })
  }

  render(){
    return(
      <div>
        <h1>Relación de Alumnos</h1>
      </div>
    )
  }
}

export default App;