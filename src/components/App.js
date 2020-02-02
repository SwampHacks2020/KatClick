import React, { Component} from 'react'
import {Route, Switch} from 'react-router-dom';
import '../index.css'
import LandingPage from './LandingPage'
import LoadingPage from './LoadingPage'
import ResultsPage from './ResultsPage'

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            loading: false
        }
    }

    render() {
        return (
        <Switch>
            <Route exact path="/" component = {LandingPage}/>
            <Route exact path="/loading" component = {LoadingPage}/>
            <Route exact path="/results" component = {ResultsPage}/>
        </Switch>
        )
    }
}

export default App;
// const APPS = {
//     LandingPage,
//     LoadingPage,
//     ResultsPage
// }

// // // switch between pages
// // function renderAppInElement(el) {
// //     var App = APPS[el.id];
// //     if (!App) return;
  
// //     // get props from elements data attribute, like the post_id
// //     const props = Object.assign({}, el.dataset);
  
// //     ReactDOM.render(<App {...props} />, el);
// //   }
  
// //   document
// //     .querySelectorAll('.__react-root')
// //     .forEach(renderAppInElement)