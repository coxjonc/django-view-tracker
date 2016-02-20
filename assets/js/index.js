var ReactDOM = require('react-dom')
var App = require('./app')
var React = require('react')

ReactDOM.render(<App url={'/api/bylines/'}/>, document.getElementById('application'))
