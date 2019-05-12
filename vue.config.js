const IS_PRODUCTION = process.env.NODE_ENV === 'production';

module.exports = {
  assetsDir: 'static',
  outputDir: 'dist',
  // publicPath: IS_PRODUCTION
  //   ? 'https://test654888.herokuapp.com/'
  //   : '/',
};
