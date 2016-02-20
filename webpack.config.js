var webpack = require('webpack');
var ExtractTextPlugin = require("extract-text-webpack-plugin");
var CopyPlugin = require('copy-webpack-plugin');

module.exports = {
    entry: {
        app: './siciarz/assets/js/app.js',
        editor: './siciarz/assets/js/editor.js',
        style: './siciarz/assets/css/main.less'
    },
    output: {
        path: './siciarz/assets/build',
        filename: '[name].js'
    },
    module: {
        loaders: [{
            test: /\.js$/,
            exclude: /node_modules/,
            loader: 'babel-loader',
            query: {
                presets: ['es2015', 'stage-0']
            }
        }, {
            test: /\.less$/,
            loader: ExtractTextPlugin.extract("style-loader", "css-loader!less-loader")
        },
        {
            test: /\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/,
            loader: 'url-loader?limit=10000&minetype=application/font-woff'
        }, {
            test: /\.(png|ttf|eot|svg)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
            loader: 'file-loader'
        }, {
            test: require.resolve("jquery"),
            loader: "expose?$!expose?jQuery"
        }]
    },
    plugins: [
        new webpack.ProvidePlugin({
            $: "jquery",
            jQuery: "jquery"
        }),
        new ExtractTextPlugin("style.css"),
        new CopyPlugin([
            {from: 'node_modules/epiceditor/epiceditor', to: 'epiceditor'}
        ])
    ]
};
