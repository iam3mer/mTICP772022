module.exports = {
  transpileDependencies: [
    'vuetify'
  ],

  devServer: {
    proxy: "http://127.0.0.1:2021"
  }
}
