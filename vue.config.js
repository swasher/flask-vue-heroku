const IS_PRODUCTION = process.env.NODE_ENV === 'production';

module.exports = {
  outputDir: 'dist',
  assetsDir: 'static',
  // publicPath: IS_PRODUCTION
  //   ? 'https://test654888.herokuapp.com/'
  //   : '/',
  devServer: {
    proxy: {
      '^/*': {
        target: 'http://localhost:5000/',
      },
    },
  },
};
