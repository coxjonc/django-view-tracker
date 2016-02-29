var path = require('path')
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')
var ExtractTextPlugin = require('extract-text-webpack-plugin')

module.exports = {
	context: __dirname,
	
	entry: './assets/js/index',
	
	output: {
		path: path.resolve('./assets/bundles/'),
		filename: '[name].js',
	},
	
	plugins: [
		new BundleTracker({filename: './webpack-stats.json'}),
		new webpack.ProvidePlugin({
			$: 'jquery',
			jQuery: 'jquery',
			'window.jQuery': 'jquery'
		}),
                new ExtractTextPlugin('styles.css')
	],
	
	module: {
		loaders: [
		  { test: /\.jsx?$/,
		  	exclude: /node_modules/,
		  	loader: 'babel-loader',
		  	query: {
		  		presets: ['react']
		  	}
		  },
		  {
		    test: /\.css?$/,
		    loader: ExtractTextPlugin.extract('style-loader', 'css-loader')
		  },
		  { test: /\.eot(\?v=\d+\.\d+\.\d+)?$/, loader: "file" },
		  { test: /\.(woff|woff2)$/, loader:"url?prefix=font/&limit=5000" },
		  { test: /\.ttf(\?v=\d+\.\d+\.\d+)?$/, loader: "url?limit=10000&mimetype=application/octet-stream" },
	          { test: /\.svg(\?v=\d+\.\d+\.\d+)?$/, loader: "url?limit=10000&mimetype=image/svg+xml" }
		]
	},
	
	resolve: {
		modulesDirectories: ['node_modules', 'bower_components'],
		extensions: ['', '.js', '.jsx'],
	},
}

