var React = require('react')
var Router = require('react-router')
require('../css/bootstrap.min.css')
var CardArticleTitle = require('./card-article-title')

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
            var bylineNodes = this.state.data.map(function(byline){
                var pkLink = '/author/'.concat(byline.pk)
                return(
                    <div className="row top-buffer">
                    <div className="col-md-8">
                        <h2>{byline.name} 
                            <Router.Link to={pkLink}>
                                <button className="btn btn-primary btn-padded">All articles</button>
                            </Router.Link> 
                        </h2>
                            <ul className="list-group">
                                <CardArticleTitle url={byline.most_viewed_all_time}/>
                                <li className="list-group-item">All time views: {byline.all_views}</li>
                                <li className="list-group-item">Rank: {byline.all_time_rank}</li>
                            </ul>
                    </div>
                    </div>
                )
            })
            return (
                <div className="bylineInfo">
                    {bylineNodes}
                </div>
            )
        }
    }
})
