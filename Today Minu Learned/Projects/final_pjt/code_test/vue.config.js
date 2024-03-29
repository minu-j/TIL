const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
    devServer: {
      proxy: { // proxyTable 설정
        '/': {
          "target":'https://search.naver.com/',
          "pathRewrite":{'^/':''},
          "changeOrigin":true,
          "secure":false
        }
      }
    }
})