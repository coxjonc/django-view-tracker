var React = require('react')

module.exports = React.createClass({
    loadTitleFromServer: function() {
        $.ajax({
            url: this.props.url,
            datatype: 'json',
            success: function(data){
               this.setState({data:data}) 
            }.bind(this)
        })
    },

    componentDidMount: function() {
        this.loadTitleFromServer();
    },

    getInitialState: function() {
        return {data:[]}
    },

    render: function() {
        return (
            <li className="list-group-item">
            <p><a href={this.state.data.url}>
                 {this.state.data.title} 
            </a> ({this.state.data.views})</p>
            </li>
        )
    }
})
