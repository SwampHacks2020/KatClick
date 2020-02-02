import React, { Component } from 'react'
import Upload from './Upload'

export class LandingPage extends Component {
    render() {
        return (
              <div className="App">
                    <Title />
                    <Cat />
                    <Upload_/>
  
                    <div className="flier"></div>
                    <div className="balloonCat"></div>
                    <div className="coinCat"></div>
                    <div className="ninjaCat"></div>
                    <div className="pianoCat"></div>
                    <div className="pirateCat"></div>
              </div>
        )
      }
    }
  
    // title component
    function Title() {
      return (
          <div className="Title">katClick</div>
      );
    }
  
    // kitty komponent
    function Cat() {
        return (
          <div className="cat" />
        );
    }     
  
    // upload button component
    function Upload_() {
        return (
          <div className="uploadContainer">
              <input type="file" name="file"/>
  
              <button className="uploadButton" type="button">
                  <div className="uploadText">Upload</div>
              </button>
          </div>
        );
    }

    export default LandingPage;
  
  
  
    // on button click
    /*
    function uploadFile() {
        return (
          
        );
    }
    */
  
    // card component
