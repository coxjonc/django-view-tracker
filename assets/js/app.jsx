var React = require('react')

module.exports = React.createClass({
    loadBylinesFromServer: function() {
        $.ajax({
            url: this.props.url,
            datatype: 'json',
            success: function(data) {
                this.setState({data:data});
            }.bind(this)
        })
    },
    getInitialState: function() {
        return {data: []};
    },

    componentDidMount: function() {
        this.loadBylinesFromServer();
    },
    render: function(){
        if (this.state.data) {
            console.log(this.state.data)
            var bylineNodes = this.state.data.map(function(byline){
                return <li>{byline.name}</li>
            })
        }
        return (
            <div>
                <h1>Hello, React!</h1>
                <ul>
                {bylineNodes}
                </ul>
            </div>
    )}
})
