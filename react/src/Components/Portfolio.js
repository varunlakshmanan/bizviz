import React, { Component } from 'react';
import ApexChart from './ApexChart';

class Portfolio extends Component {
  constructor(props) {
    super(props)
    this.state = {
      port1_dates: props.port1_dates
    }
  }
  render() {

    return (
      <div>
        <div className="row">

          <div className="twelve columns collapsed">

            <h1>Final Graphs</h1>

          </div>
        </div>
        <ApexChart port1_dates = {this.state.port1_dates}/>
      </div>
    );
  }
}

export default Portfolio;
