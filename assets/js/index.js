var ReactDOM = require('react-dom')
var React = require('react')
var Router = require('react-router')
var App = require('./app')
var Author = require('./author')
require('../css/bootstrap.min.css')

var BylineHandler = React.createClass({
    render: function() {
        return <App url='/api/bylines/' />
    }
})

ReactDOM.render((
    <Router.Router history={Router.hashHistory}>
        <Router.Route path='/' component={BylineHandler}/>
        <Router.Route path='/author/:pk' component={Author}/>
    </Router.Router>
), document.getElementById('app'))
