var React = require('react')

module.exports = React.createClass({
    loadDataFromServer: function(){
        $.ajax({
            url: this.props.url, 
            datatype: 'json', 
            success: function(data){
                this.setState({data:data})
            }.bind(this)
        })
    },

    getInitialState: function(){
        return {data:[]}
    },

    componentDidMount: function() {
        this.loadDataFromServer()
    },
    
    render: function() {
        return (
            <h1>{this.state.data.title}</h1> 
        )
    }
        
    
})
