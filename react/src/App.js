import React, {useState, useEffect, Component } from 'react';
import $ from 'jquery';
import './App.css';
import Header from './Components/Header';
import Footer from './Components/Footer';
import About from './Components/About';
import Data from './Components/Data';
import Contact from './Components/Contact';

class App extends Component {

  constructor(props){
    super(props);
    this.state = {
      foo: 'bar',
      resumeData: {}
    };


  }

  render() {
    return (
      <div className="App">
        <Header data={this.state.resumeData.main}/>
        <About data={this.state.resumeData.main}/>
        <Data data={this.state.resumeData.data}/>
        <Footer data={this.state.resumeData.main}/>
      </div>
    );
  }
}

export default App;
