var path = require('path');

module.exports = {
  entry: './exam/static/js/index.js',
  output: {
    filename: 'bundle.js',
    path: path.join(__dirname, 'exam/static/js/dist')
  }
};