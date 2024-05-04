const path = require('path');

module.exports = {
    module: {
        rules: [
            {
                test: /\.jsx?$/,
                exclude: [
                    /node_modules/,
                    /public/
                ],
                use: {
                    loader: "babel-loader"
                }
            },
            {
                test: /\.scss$/i,
                use: [
                    "style-loader",
                    "css-loader",
                    {
                        loader: "sass-loader",
                    }
                ]
            },
            {
                test: /\.svg$/,
                use: [
                    '@svgr/webpack'
                ],
            },
            {
                test: /\.(png|jpg|jpeg|gif)$/i,
                type: 'asset/inline'
            }
        ]
    },
    resolve: {
        extensions: ['.js', '.jsx', '.scss'],
        alias: {
            '@': path.resolve(__dirname, 'src'),
            '@shared': path.resolve(__dirname, 'src/shared'),
            '@components': path.resolve(__dirname, 'src/components'),
        },
    },
    performance: {
        hints: false,
        maxEntrypointSize: 512000,
        maxAssetSize: 512000
    },
    devServer: {
        historyApiFallback: true,
        port: 8001,
    },
}
