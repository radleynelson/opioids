const path = require('path');
const glob = require('glob');

// map the entry files: { app: entry file, ... }
const entries = glob.sync("./*/scripts/__entry__.js").reduce((acc, fp) => {
    acc[fp.split(path.sep)[1]] = fp;
    return acc;
}, {});

// print our findings (just for this tutorial)
console.log(entries);
// webpack config

const VueLoaderPlugin = require('vue-loader/lib/plugin')

module.exports = {
    entry: entries,
    output: {
        path: path.resolve(__dirname),
        filename: '[name]/scripts/__bundle__.js'
    },
    module: {
        rules: [
            {
              test: /\.vue$/,
              loader: 'vue-loader'
            },
            // this will apply to both plain `.js` files
            // AND `<script>` blocks in `.vue` files
            {
              test: /\.js$/,
              loader: 'babel-loader',
              options: {
                plugins: [
                    "@babel/plugin-syntax-dynamic-import"
                ]
            }
            },
            // this will apply to both plain `.css` files
            // AND `<style>` blocks in `.vue` files
            {
              test: /\.css$/,
              use: [
                'vue-style-loader',
                'css-loader'
              ]
            },
            {
              test: /\.(png|jpg|gif)$/i,
              use: [
                {
                  loader: 'url-loader',
                  options: {
                    limit: 8192
                  }
                }
              ]
            },
            {
              test: /\.scss$/,
              use: [
                  "style-loader", // creates style nodes from JS strings
                  "css-loader", // translates CSS into CommonJS
                  "sass-loader" // compiles Sass to CSS, using Node Sass by default
              ]
          }
          ]
    },
    plugins: [
      // make sure to include the plugin for the magic
      new VueLoaderPlugin()
    ],
    resolve: {
      alias: {
        vue: 'vue/dist/vue.js'
      }
    }
};
console.log(module.exports);