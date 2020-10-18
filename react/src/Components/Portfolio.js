import React, { Component } from 'react';
import ApexChart from './ApexChart';

class Portfolio extends Component {
  render() {

    if (this.props.data) {
      var projects = this.props.data.projects.map(function (projects) {
        var projectImage = 'images/portfolio/' + projects.image;
        
        return (
          <div key={projects.title} className="columns portfolio-item">
            <div className="item-wrap">
              <a href={projects.url} title={projects.title}>
                <img alt={projects.title} src={projectImage} />
                <div className="overlay">
                  <div className="portfolio-item-meta">
                    <h5>{projects.title}</h5>
                    <p>{projects.category}</p>
                  </div>
                </div>
              </a>
            </div>
          </div>
        )
      })
    } 

    return (
      <section id="portfolio">

        <div className="row">

          <div className="twelve columns collapsed">

            <h1>Final Graphs</h1>

          </div>
        </div>
        <ApexChart/>
      </section>
    );
  }
}

export default Portfolio;
