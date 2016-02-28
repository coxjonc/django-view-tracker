var React = require('react')
var Article = require('./article')
var CardArticleTitle = require('./card-article-title')

module.exports = React.createClass({
        loadDataFromServer: function() {
            $.ajax({
                url: '/api/bylines/' + this.props.params.pk + '/',
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
            this.loadDataFromServer();
        },
        render: function() { 
            if (this.state.data.length!=0) {    
            var articleNodes = this.state.data.articles.map(function(article){
                    console.log(article)    
                    return <CardArticleTitle url={article}/>
                })
            }
            return (
                    <div className="row top-buffer">
                    <div className="col-md-8">
                        {articleNodes}
                    </div>
                    </div>
                   )
            }
        })

/*        <div className="row top-buffer">
        <div className="col-md-8">
            <h2>{byline.name} <Router.Link to="/author"><button className="btn btn-primary">View author details</button></Router.Link> </h2>
                <ul className="list-group">
                    <CardArticleTitle url={byline.most_viewed_all_time}/>
                    <li className="list-group-item">All time views: {byline.all_views}</li>
                    <li className="list-group-item">Rank: {byline.all_time_rank}</li>
                </ul>
        </div>
        </div>
    }*/
