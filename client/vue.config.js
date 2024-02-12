const webpack = require('webpack');
const { defineConfig } = require('@vue/cli-service');
module.exports = defineConfig({
  configureWebpack: config => {
    return {
      node: {
        __filename: true,
        __dirname: true
      },
      plugins: [
        new webpack.NormalModuleReplacementPlugin(/settings$/, function(resource) {
          resource.request = resource.request.replace(/settings$/, `settings/${process.env.NODE_ENV}`);
        })
      ],
      output: {
        libraryExport: 'default'
      },
    };
  },

  chainWebpack: chain => {
    chain.module.rule('images')
        .test(/\.(svg|jpe?g|gif|png|webp|avif|ico)(\?.*)?$/)
        .type('javascript/auto')
        .use('url-loader')
        .loader('url-loader')
        .options({
          esModule: false,
          limit: 32768,
          name: `assets/[name].[hash:8].[ext]`
        })
    chain.module.rule('videos')
        .test(/\.(mp4|webm|mov)(\?.*)?$/)
        .type('javascript/auto')
        .use('url-loader')
        .loader('url-loader')
        .options({
          esModule: false,
          limit: 32768,
          name: `assets/media/[name].[hash:8].[ext]`
        })
  },

  css: {
    sourceMap: true
  }
})
