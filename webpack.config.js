const path = require("path");
const webpack = require("webpack");

module.exports = {
	entry: {
		app: "./static/src/app.js"
	},
	output: {
		filename: "[name].js",
		path: path.resolve(__dirname, "static/dist")
	},
	devtool: "source-map",
	module: {
		rules: [
			{
				test: /\.jsx?$/,
				use: {
					loader: "babel-loader",
					options: {
						presets: ["es2015", "react"]
					}
				},
				exclude: "/node_modules/"
			},
			{
				test: /\.sass$/,
				use: [
					{ loader: "style-loader" },
					{ loader: "css-loader" },
					{ loader: "sass-loader" }
				],
				exclude: "/node_modules/"
			}
		]
	},
	devServer: {
		contentBase: path.join(__dirname, "./static"),
		port: 9000
	},
	plugins: [
		new webpack.ProvidePlugin({
			$: 'jquery',
			jQuery: 'jquery',
			'window.jQuery': 'jquery',
			Popper: ['popper.js', 'default'],
			Util: "exports-loader?Util!bootstrap/js/dist/util",
			Dropdown: "exports-loader?Dropdown!bootstrap/js/dist/dropdown",
		})
	],
	watch: true
}
