const IS_PRODUCTION = process.env.NODE_ENV === 'production';

module.exports = {
  assetsDir: 'static',
  publicPath: IS_PRODUCTION
    ? 'https://test654888.herokuapp.com/'
    : '/',
};
