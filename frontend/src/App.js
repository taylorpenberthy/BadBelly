import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  constructor() {
    super()
    this.state = {
      recipes: []
    }
  }
  componentDidMount() {
      fetch('http://127.0.0.1:8000/api/')
      .then(response => {
        return response.json()
      }
      
      ).then(recipe => {
        this.setState({
          recipes: recipe
        })
      }
      ).catch(err => {
        console.error(err)
 
  })}

  render() {
    return (
      <div>
        {this.state.recipes.map(item => (
          <div key={item.id}>
            <h1>{item.title}</h1>
            <span>{item.ingredients}</span>
          </div>
        ))}
      </div>
  );
}
}

export default App;
