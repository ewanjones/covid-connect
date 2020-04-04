const path = require('path');
const merge = require('webpack-merge');

const baseConfig = require('./core.webpack.js');


const outputDirectory = 'dist';


module.exports = merge(baseConfig, {
    mode: 'production',
    output: {
        path: path.join(__dirname, outputDirectory),
        filename: 'bundle.js'
    },
})
