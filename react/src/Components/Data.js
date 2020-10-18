import React, { useState, Component } from 'react';
import InputGroup from 'react-bootstrap/InputGroup';
import FormControl from 'react-bootstrap/FormControl';
import FormGroup from 'react-bootstrap/FormGroup';
import FormLabel from 'react-bootstrap/FormLabel';
import ReactFileReader from './ReactFileReader';
import Chart from 'chart.js';
import Dropzone from 'react-dropzone';
import Portfolio from './Portfolio';
import csv from 'csv';
import ApexChart from './ApexChart';
import ReactLoading from 'react-loading';


class Data extends Component {
  constructor(props) {
    super(props);
    this.months = [
      'January',
      'February',
      'March',
      'April',
      'May',
      'June',
      'July',
      'August',
      'September',
      'October',
      'November',
      'December',
    ]

    this.state = {
      step: 'form',
      submitted: false,
      time: 10, 
      advertising: 0,
      wages: 0,
      fixed_costs: 0,
      other_costs: 0,
      sector: 0,
      online: 0,
      file: null,
      baseline: null, 
      projection: null,
      port1:  [
        {
          name: "Series 1",
          data: [
            {
              x: "02-10-2017 GMT",
              y: 34
            },
            {
              x: "02-11-2017 GMT",
              y: 43
            },
            {
              x: "02-12-2017 GMT",
              y: 31
            },
            {
              x: "02-13-2017 GMT",
              y: 43
            },
            {
              x: "02-14-2017 GMT",
              y: 33
            },
            {
              x: "02-15-2017 GMT",
              y: 52
            }
          ]
        }
      ], 
      port2: null, 
      port3: null
    }

    this.backButton = this.backButton.bind(this);
    this.handleTimeChange = this.handleTimeChange.bind(this);
    this.handleAdvertisingChange = this.handleAdvertisingChange.bind(this);
    this.handleWagesChange = this.handleWagesChange.bind(this);
    this.handleFixedChange = this.handleFixedChange.bind(this);
    this.handleOtherChange = this.handleOtherChange.bind(this);
    this.handleSectorChange = this.handleSectorChange.bind(this);
    this.handleOnlineChange = this.handleOnlineChange.bind(this);
    this.changePortfolio1 = this.changePortfolio1.bind(this);
    this.changePortfolio2 = this.changePortfolio2.bind(this);
    this.changePortfolio3 = this.changePortfolio3.bind(this);
    this.changeBaseline = this.changeBaseline.bind(this);
    this.changeProjection = this.changeProjection.bind(this);
    this.handleSubmitChange = this.handleSubmitChange.bind(this);
    this._enterData = this._enterData.bind(this);
  }
  _enterData(event) {
    event.preventDefault();
    this.setState({step: 'loading'});
    console.log(JSON.stringify({
          'time': this.state.time,
          'advertising': this.state.advertising,
          'wages': this.state.wages,
          'fixed_costs': this.state.fixed_costs,
          'other_costs': this.state.other_costs,
          'online': this.state.online,
          'sector':this.state.sector,
          'file_path': this.state.file
        })) 
    fetch("http://localhost:5000/getEstimatedRevenue", {
        method: "POST",
        headers : {
          'Content-Type': 'application/json',
          'accept':'application/json'
        },
        body : JSON.stringify({
          'time': this.state.time,
          'advertising': this.state.advertising,
          'wages': this.state.wages,
          'fixed_costs': this.state.fixed_costs,
          'other_costs': this.state.other_costs,
          'online': this.state.online,
          'sector':this.state.sector,
          'file_path': this.state.file
        })
    }) .then(response => {
        console.log(response.responseText)
        console.log(response)
        return response.json();
    }) .then(res => {

          var baseline_list = []
          var projection_list = []
          console.log(res)
          for (var key in res) {
            if (key === "baseline") {
              for (var timekey in res[key]) {
                var time = timekey
                for (var timePoint in res[key][timekey]) {
                  var new_dict = {}
                  new_dict["x"] = timePoint
                  new_dict["y"] = res[key][timekey][timePoint]
                  baseline_list.push(new_dict)
                }
              }
            }
            else {
              for (var timekey in res[key]) {
                var time = timekey
                console.log(res[key][timekey])
                var new_dict = {}
                new_dict["x"] = time
                new_dict["y"] = res[key][timekey]
                projection_list.push(new_dict)
              }
            }
          }
          this.changeBaseline(baseline_list);
          this.changeProjection(projection_list);
          console.log(this.state.baseline);
          console.log(this.state.projection);
    }) .catch(function(error) {
        console.log('There has been a problem: ' + error.message);
        throw error;
    })
    fetch("http://localhost:5000/getStockData", {
        method: "POST",
        headers : {
          'Content-Type': 'application/json',
          'accept':'application/json'
        },
        body : JSON.stringify({
          'time': this.state.time,
          'advertising': this.state.advertising,
          'wages': this.state.wages,
          'fixed_costs': this.state.fixed_costs,
          'other_costs': this.state.other_costs,
          'online': this.state.online,
          'sector':this.state.sector,
          'file_path': this.state.file
        })
    }) .then(response => {
        console.log(response)
        return response.json();
    }) .then(res => {
            var portfolio1 = []
            var portfolio2 = []
            var portfolio3 = []
            for (var portfolio in res) {
              var key = portfolio
              var curr_value = portfolio
              if (curr_value === "low_risk") {
                for (var timekey in res[key]) {
                  var time = timekey
                  for (var timePoint in res[key][timekey]) {
                    var new_dict = {}
                    new_dict["x"] = timePoint
                    new_dict["y"] = res[key][timekey][timePoint]
                    portfolio1.push(new_dict)
                  }
                }
              }
              else {
                if ((curr_value === "medium_risk")) {
                  for (var timekey in res[key]) {
                    var time = timekey
                    for (var timePoint in res[key][timekey]) {
                      var new_dict = {}
                      new_dict["x"] = timePoint
                      new_dict["y"] = res[key][timekey][timePoint]
                      portfolio2.push(new_dict)
                    }
                  }
                }
                else {
                  for (var timekey in res[key]) {
                    var time = timekey
                    for (var timePoint in res[key][timekey]) {
                      var new_dict = {}
                      new_dict["x"] = timePoint
                      new_dict["y"] = res[key][timekey][timePoint]
                      portfolio3.push(new_dict)
                    }
                  }
                }
              }
            }
            this.changePortfolio1(portfolio1);
            console.log(this.state.port1)
            this.changePortfolio2(portfolio2);
            console.log(this.state.port2)
            this.changePortfolio3(portfolio3);
            console.log(this.state.port3)
            this.setState({step: 'performance'});
    }) .catch(function(error) {
        console.log(error);
        this.setState({step: 'form'});
    })
  };

  backButton() {
    this.setState({step: 'form'});
  }

  handleTimeChange(event) {
    this.setState({time: event.target.value});
  }

  handleAdvertisingChange(event) {
    this.setState({advertising: parseFloat(event.target.value)});
  }
  handleWagesChange(event) {
    this.setState({wages: parseFloat(event.target.value)});
  }
  handleFixedChange(event) {
    this.setState({fixed_costs: parseFloat(event.target.value)});
  }
  handleOtherChange(event) {
    this.setState({other_costs: parseFloat(event.target.value)});
  }
  handleSectorChange(event) {
    this.setState({sector: event.target.value});
  }
  handleOnlineChange(event) {
    this.setState({online: event.target.value});
  }
  handleSubmitChange() {
    this.setState({submitted: true})
  }
  changePortfolio1(port_dict) {
    this.setState({port1: port_dict })
  }
  changePortfolio2(port_dict) {
    this.setState({port2: port_dict })
  }
  changePortfolio3(port_dict) {
    this.setState({port3: port_dict })
  }
  changeBaseline(port_dict) {
    this.setState({baseline: port_dict})
  }
  changeProjection(port_dict) {
    this.setState({projection: port_dict})
  }
  

  onDrop(files) {

    this.setState({ files });

    var file = files[0];

    const reader = new FileReader();
    reader.onload = () => {
      csv.parse(reader.result, (err, data) => {

        var userList = [];

        for (var i = 0; i < data.length; i++) {
          const year = data[i][0];
          const month = data[i][1];
          const advertising = data[i][2];
          const wages = data[i][3];
          const fixed_cost = data[i][4];
          const other_cost = data[i][5];
          const online = data[i][6];
          const revenue = data[i][7];
          const newUser = { "year": year, "month": month, "advertising": advertising, "wages": wages, "fixed_costs": fixed_cost, "other_costs": other_cost, "online": online, "revenue": revenue};
          userList.push(newUser);
        };
        this.setState({file: userList})
        console.log(this.state.file)
      });
      
    };

    reader.readAsBinaryString(file);
  }

  render() {
      const fontSize = 5;
      if (this.state.step === "form") {
        return (
          <section id="data">
          <form onSubmit = {this._enterData}>
            <div className="row education">
              <div className="three columns header-col">
                  <h1><span>Time Span</span></h1>
              </div>
              
                <div className="nine columns main-col">
                    <div className="row item">
                      <input type="text" defaultValue="" size="25" id="Time Span" name="Time Span" value={this.state.value} onChange={this.handleTimeChange}/>
                    </div>
                </div>
            </div>


            <div className="row work">

              <div className="three columns header-col">
                  <h1><span>Advertising</span></h1>
              </div>

              <div className="nine columns main-col">
                <div className="row item">
                  <input value={this.state.value} onChange={this.handleAdvertisingChange} type="text" defaultValue="" size="25" id="Advertising Amount" name="Advertising Amount" o/>
                </div>
              </div>
            </div>

            <div className="row work">

              <div className="three columns header-col">
                  <h1><span>Wages</span></h1>
              </div>

              <div className="nine columns main-col">
                <div className="row item">
                  <input value={this.state.value} onChange={this.handleWagesChange} type="text" defaultValue="" size="25" id="Wage Amount" name="Wage Amount" o/>
                </div>
              </div>
            </div>

            <div className="row work">

              <div className="three columns header-col">
                  <h1><span>Fixed Costs</span></h1>
              </div>

              <div className="nine columns main-col">
                <div className="row item">
                  <input value={this.state.value} onChange={this.handleFixedChange} type="text" defaultValue="" size="25" id="Fixed Amount" name="Fixed Amount" o/>
                </div>
              </div>
            </div>

            <div className="row work">

              <div className="three columns header-col">
                  <h1><span>Other Costs</span></h1>
              </div>

              <div className="nine columns main-col">
                <div className="row item">
                  <input value={this.state.value} onChange={this.handleOtherChange} type="text" defaultValue="" size="25" id="Other Amount" name="Other Amount" o/>
                </div>
              </div>
            </div>

            <div className="row work">

              <div className="three columns header-col">
                  <h1><span>Sector</span></h1>
              </div>

              <div className="nine columns main-col">
                <div className="row item">
                  <input value={this.state.value} onChange={this.handleSectorChange} type="text" defaultValue="" size="25" id="Sector Amount" name="Sector Amount" o/>
                </div>
              </div>
            </div>

            <div className="row work">

              <div className="three columns header-col">
                  <h1><span>Online</span></h1>
              </div>

              <div className="nine columns main-col">
                <div className="row item">
                  <input value={this.state.value} onChange={this.handleOnlineChange} type="text" defaultValue="" size="25" id="Online Amount" name="Online Amount" o/>
                </div>
              </div>
            </div>


            <div className="row skill">

              <div className="three columns header-col">
                  <h1><span>CSV File</span></h1>
              </div>

              <div align="center" oncontextmenu="return false">
                <br /><br /><br />
                <div className="dropzone">
                  <Dropzone accept=".csv" onDropAccepted={this.onDrop.bind(this)}>            
                  </Dropzone>
                  <br /><br /><br />
                </div>
                <h2>Upload or drop your <font size={fontSize} color="#00A4FF">CSV</font><br /> file here.</h2>
              </div>
            </div>

            <div className="row skill">

              <div className="three columns header-col">
                  <h1><span></span></h1>
              </div>

              <div className="nine columns main-col">
                <div className="row item">
                  <input align="center" type="submit" value="Submit" />                </div>
              </div>
            </div>
          </form>
      </section>
    );
      }
      else {
        if (this.state.step === "loading") {
          return (
              <section id="data">
              <form onSubmit = {this._enterData}>
                <div className="row education">
                  <div className="three columns header-col">
                      <h1><span>Time Span</span></h1>
                  </div>
                  
                    <div className="nine columns main-col">
                        <div className="row item">
                          <input type="text" defaultValue="" size="25" id="Time Span" name="Time Span" value={this.state.value} onChange={this.handleTimeChange}/>
                        </div>
                    </div>
                </div>


                <div className="row work">

                  <div className="three columns header-col">
                      <h1><span>Advertising</span></h1>
                  </div>

                  <div className="nine columns main-col">
                    <div className="row item">
                      <input value={this.state.value} onChange={this.handleAdvertisingChange} type="text" defaultValue="" size="25" id="Advertising Amount" name="Advertising Amount" o/>
                    </div>
                  </div>
                </div>

                <div className="row work">

                  <div className="three columns header-col">
                      <h1><span>Wages</span></h1>
                  </div>

                  <div className="nine columns main-col">
                    <div className="row item">
                      <input value={this.state.value} onChange={this.handleWagesChange} type="text" defaultValue="" size="25" id="Wage Amount" name="Wage Amount" o/>
                    </div>
                  </div>
                </div>

                <div className="row work">

                  <div className="three columns header-col">
                      <h1><span>Fixed Costs</span></h1>
                  </div>

                  <div className="nine columns main-col">
                    <div className="row item">
                      <input value={this.state.value} onChange={this.handleFixedChange} type="text" defaultValue="" size="25" id="Fixed Amount" name="Fixed Amount" o/>
                    </div>
                  </div>
                </div>

                <div className="row work">

                  <div className="three columns header-col">
                      <h1><span>Other Costs</span></h1>
                  </div>

                  <div className="nine columns main-col">
                    <div className="row item">
                      <input value={this.state.value} onChange={this.handleOtherChange} type="text" defaultValue="" size="25" id="Other Amount" name="Other Amount" o/>
                    </div>
                  </div>
                </div>

                <div className="row work">

                  <div className="three columns header-col">
                      <h1><span>Sector</span></h1>
                  </div>

                  <div className="nine columns main-col">
                    <div className="row item">
                      <input value={this.state.value} onChange={this.handleSectorChange} type="text" defaultValue="" size="25" id="Sector Amount" name="Sector Amount" o/>
                    </div>
                  </div>
                </div>

                <div className="row work">

                  <div className="three columns header-col">
                      <h1><span>Online</span></h1>
                  </div>

                  <div className="nine columns main-col">
                    <div className="row item">
                      <input value={this.state.value} onChange={this.handleOnlineChange} type="text" defaultValue="" size="25" id="Online Amount" name="Online Amount" o/>
                    </div>
                  </div>
                </div>


                <div className="row skill">

                  <div className="three columns header-col">
                      <h1><span>CSV File</span></h1>
                  </div>

                  <div align="center" oncontextmenu="return false">
                    <br /><br /><br />
                    <div className="dropzone">
                      <Dropzone accept=".csv" onDropAccepted={this.onDrop.bind(this)}>            
                      </Dropzone>
                      <br /><br /><br />
                    </div>
                    <h2>Upload or drop your <font size={fontSize} color="#00A4FF">CSV</font><br /> file here.</h2>
                  </div>
                </div>

              <div className="row skill">

                <div className="three columns header-col">
                    <h1><span></span></h1>
                </div>

                  <div className="nine columns main-col">
                    <div className="row item">
                      <input align="center" type="submit" value="Submit" />   
                      <br />
              <br />
              <br />
              <br />
              {/* <Row> */}
                {/* <Col med='5' />
                <Col med='2'> */}
                  <ReactLoading align="center" type='spin' color='#0984e3'/>
                  <br />
                  <p style={{width: 230, marginLeft: -80}}>Finding investments right for you</p>
                {/* </Col>
                <Col med='5' /> */}
              {/* </Row> */}             
                  </div>
                </div>

              </div>
              </form>
              
          </section>
          );
      } else {
        return (
          <section id="data">
          <form onSubmit = {this._enterData}>
            <div className="row education">
              <div className="three columns header-col">
                  <h1><span>Time Span</span></h1>
              </div>
              
                <div className="nine columns main-col">
                    <div className="row item">
                      <input type="text" defaultValue="" size="25" id="Time Span" name="Time Span" value={this.state.value} onChange={this.handleTimeChange}/>
                    </div>
                </div>
            </div>


            <div className="row work">

              <div className="three columns header-col">
                  <h1><span>Advertising</span></h1>
              </div>

              <div className="nine columns main-col">
                <div className="row item">
                  <input value={this.state.value} onChange={this.handleAdvertisingChange} type="text" defaultValue="" size="25" id="Advertising Amount" name="Advertising Amount" o/>
                </div>
              </div>
            </div>

            <div className="row work">

              <div className="three columns header-col">
                  <h1><span>Wages</span></h1>
              </div>

              <div className="nine columns main-col">
                <div className="row item">
                  <input value={this.state.value} onChange={this.handleWagesChange} type="text" defaultValue="" size="25" id="Wage Amount" name="Wage Amount" o/>
                </div>
              </div>
            </div>

            <div className="row work">

              <div className="three columns header-col">
                  <h1><span>Fixed Costs</span></h1>
              </div>

              <div className="nine columns main-col">
                <div className="row item">
                  <input value={this.state.value} onChange={this.handleFixedChange} type="text" defaultValue="" size="25" id="Fixed Amount" name="Fixed Amount" o/>
                </div>
              </div>
            </div>

            <div className="row work">

              <div className="three columns header-col">
                  <h1><span>Other Costs</span></h1>
              </div>

              <div className="nine columns main-col">
                <div className="row item">
                  <input value={this.state.value} onChange={this.handleOtherChange} type="text" defaultValue="" size="25" id="Other Amount" name="Other Amount" o/>
                </div>
              </div>
            </div>

            <div className="row work">

              <div className="three columns header-col">
                  <h1><span>Sector</span></h1>
              </div>

              <div className="nine columns main-col">
                <div className="row item">
                  <input value={this.state.value} onChange={this.handleSectorChange} type="text" defaultValue="" size="25" id="Sector Amount" name="Sector Amount" o/>
                </div>
              </div>
            </div>

            <div className="row work">

              <div className="three columns header-col">
                  <h1><span>Online</span></h1>
              </div>

              <div className="nine columns main-col">
                <div className="row item">
                  <input value={this.state.value} onChange={this.handleOnlineChange} type="text" defaultValue="" size="25" id="Online Amount" name="Online Amount" o/>
                </div>
              </div>
            </div>


            <div className="row skill">

              <div className="three columns header-col">
                  <h1><span>CSV File</span></h1>
              </div>

              <div align="center" oncontextmenu="return false">
                <br /><br /><br />
                <div className="dropzone">
                  <Dropzone accept=".csv" onDropAccepted={this.onDrop.bind(this)}>            
                  </Dropzone>
                  <br /><br /><br />
                </div>
                <h2>Upload or drop your <font size={fontSize} color="#00A4FF">CSV</font><br /> file here.</h2>
              </div>
            </div>
            <input align="center" type="submit" value="Submit" />
          </form>
          <section id = "results">
            <ApexChart baseline = {this.state.baseline} projection = {this.state.projection} portfolio1 = {this.state.port1} portfolio2 = {this.state.port2} portfolio3 = {this.state.port3}/>
            <div className="row work">

              <div className="three columns header-col">
                  <h1><span>Low Risk Portfolio: </span></h1>
              </div>

              <div className="nine columns main-col">
                <div className="row item">
                  <h2><span>TDTF + BIV + PZA</span></h2>
                </div>
              </div>
            </div>
            <div className="row work">

              <div className="three columns header-col">
                  <h1><span>Medium Risk Portfolio: </span></h1>
              </div>

              <div className="nine columns main-col">
                <div className="row item">
                  <h2><span>GOOGL + URI + MSFT</span></h2>
                </div>
              </div>
            </div>
            <div className="row work">

              <div className="three columns header-col">
                  <h1><span>High Risk Portfolio: </span></h1>
              </div>

              <div className="nine columns main-col">
                <div className="row item">
                  <h2><span>AMZN + NVDA + AAPL</span></h2>
                </div>
              </div>
            </div>
          </section>
      </section>
    );
      }
    } 
  }
}

export default Data;
