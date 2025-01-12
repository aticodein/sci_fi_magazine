const path = require("path");

module.exports = {
  entry: "./index.js", // Entry point for React
  output: {
    path: path.resolve(__dirname, "dist"), // Output folder
    filename: "bundle.js", // Generated JS bundle
  },
  module: {
    rules: [
      {
        test: /\.js$/, // Match JS files
        exclude: /node_modules/,
        use: {
          loader: "babel-loader", // Use Babel loader
        },
      },
    ],
  },
  resolve: {
    extensions: [".js", ".jsx"],
  },
  mode: "development", // Development mode
};
