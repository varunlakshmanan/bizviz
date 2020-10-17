import React, { Component } from 'react';

class About extends Component {
  render() {

    if(this.props.data){
      var name = this.props.data.name;
      var profilepic= "images/"+this.props.data.image;
      var bio = this.props.data.bio;
      var street = this.props.data.address.street;
      var city = this.props.data.address.city;
      var state = this.props.data.address.state;
      var zip = this.props.data.address.zip;
      var phone= this.props.data.phone;
      var email = this.props.data.email;
      var resumeDownload = this.props.data.resumedownload;
    }

    return (
      <section id="about">
      <div className="row">
         <div className="nine columns main-col">
            <h2>Inspiration</h2>
            <p>{'With the onset of Covid-19, small businesses all over the world are struggling to make the profits necessary to stay open. In the hope of keeping the business running, it can become a common mistake to spend more and more money in vain when an alternative option could be more fruitful.'}</p>
         </div>
         <div className="nine columns main-col">
            <h2>Our Solution</h2>
            <p>{'While putting more money into an existing business may make sligtly more profit, there may still be a net existing loss. Instead, our app allows small businesses to choose a portion of their usual input cost and visualize whether it would be more lucrative in various investment portfolios over a given period of time.'}</p>
         </div>
         <div className="nine columns main-col">
            <p>
               <a href={'#data'} className="button"><i className="fa fa-download"></i>Enter Data</a>
            </p>

         </div>
      </div>
      </section>
    );
  }
}

export default About;
