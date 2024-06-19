import React from "react"
import ReactDOM from "react-dom/client";
import App from "@app/app";

import "./reset.scss"
import "./common.scss"
import "./ui.scss"

const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
