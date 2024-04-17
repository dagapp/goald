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
                test: /\.(png|svg|jpg|jpeg|gif)$/i,
                type: 'asset/inline'
            }
        ]
    },
    resolve: {
        extensions: ['.js', '.jsx', '.scss'],
        alias: {
            '@': path.resolve(__dirname, 'src'),
            '@assets': path.resolve(__dirname, 'src/assets'),
            '@components': path.resolve(__dirname, 'src/components'),
        },
    },
    devServer: {
        historyApiFallback: true,
        // static: {
        //     directory: path.join(__dirname, 'public'),
        // },
        // compress: true,
        // port: 9000,
    },
}