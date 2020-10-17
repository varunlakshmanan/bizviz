import React, { Component } from 'react';
import ParticlesBg  from "particles-bg";

class Header extends Component {
  render() {

    if(this.props.data){
       var project = this.props.data.project;
    }

    return (
      <header id="home">
      <ParticlesBg type="circle" bg={true} />
      <nav id="nav-wrap">
         <a className="mobile-btn" href="#nav-wrap" title="Show navigation">Show navigation</a>
	      <a className="mobile-btn" href="#home" title="Hide navigation">Hide navigation</a>

         <ul id="nav" className="nav">
            <li className="current"><a className="smoothscroll" href="#home">Home</a></li>
            <li><a className="smoothscroll" href="#about">Description</a></li>
	         <li><a className="smoothscroll" href="#data">Data</a></li>
            <li><a className="smoothscroll" href="#portfolio">Results</a></li>
            <li><a className="smoothscroll" href="#contact">Contact</a></li>
         </ul>
      </nav>

      <div className="row banner">
      
         <div className="banner-text">
            <h1 className="responsive-headline">HackGT7 Project</h1>
            <h3>Made by Nishant Ravi, Varun Lakshmanan, Yash Patel, Pranav Pusarla.</h3>
            <hr />
            <ul className="social">
               <a href={"#about"} className="button btn project-btn"><i className="fa fa-book"></i>Get Started</a>
               <a href={'https://github.com/varunlakshmanan/hackgt7'} className="button btn github-btn"><i className="fa fa-github"></i>Github</a>
            </ul>
         </div>
      </div>

      <p className="scrolldown">
         <a className="smoothscroll" href="#about"><i className="icon-down-circle"></i></a>
      </p>

   </header>
    );
  }
}

export default Header;
