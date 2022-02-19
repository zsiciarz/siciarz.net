const path = require('path');
const webpack = require('webpack');
const ExtractTextPlugin = require("extract-text-webpack-plugin");

module.exports = {
    entry: {
        app: './siciarz/assets/js/app.js',
        style: './siciarz/assets/css/main.less'
    },
    output: {
        path: path.resolve(__dirname, './siciarz/assets/build'),
        filename: '[name].js'
    },
    module: {
        rules: [{
            test: /\.js$/,
            exclude: /node_modules/,
            loader: 'babel-loader',
            options: {
                presets: ['es2015', 'stage-0']
            }
        }, {
            test: /\.less$/,
            loader: ExtractTextPlugin.extract({
                fallback: 'style-loader',
                use: 'css-loader!less-loader'
            })
        },
        {
            test: /\.(png|woff|woff2|eot|ttf|svg)$/,
            loader: 'url-loader',
            options: {
                'limit': 100000
            }
        }]
    },
    plugins: [
        new ExtractTextPlugin("style.css")
    ]
};
