import React from "react";
import ReactDOM from "react-dom";
import App from "./App";
import { ChakraProvider } from "@chakra-ui/react";
import { Auth0Provider } from "@auth0/auth0-react";

ReactDOM.render(
  <Auth0Provider
    domain="findyourjam.us.auth0.com"
    clientId="nLZyGDXsrToWX2xsHrMoAixeKStWUDjD"
    redirectUri="http://localhost:3000/verification"
    audience="jamsessions"
    scope="profile openid email"
  >
    <ChakraProvider>
      <App />
    </ChakraProvider>
  </Auth0Provider>,
  document.getElementById("root")
);
