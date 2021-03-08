import React, { useEffect, useState } from "react";
import { Flex, Link, Box, Spacer } from "@chakra-ui/react";
import {
  BrowserRouter as Router,
  Link as ReactLink,
  Switch,
  Route,
} from "react-router-dom";
import { ChevronRightIcon } from "@chakra-ui/icons";

import { useAuth0 } from "@auth0/auth0-react";
import LoginButton from "./components/LoginButton";
import LogoutButton from "./components//LogoutButton";

import { Sessions } from "./components//Sessions";
import { Institutions } from "./components//Institutions";
import { Musicians } from "./components//Musicians";
import { SessionsForm } from "./components//SessionsForm";
import { Register } from "./components//Register";
import { InstitutionsForm } from "./components//InstitutionsForm";
import { MusiciansForm } from "./components//MusiciansForm";
import { Verification } from "./components//Verification";
import { MainLayout } from "./components/MainLayout";
import { SessionsUpdate } from "./components/SessionsUpdate";

const App = () => {
  const {
    user,
    isAuthenticated,
    isLoading,
    getAccessTokenSilently,
  } = useAuth0();

  const [accessToken, setAccessToken] = useState("");

  useEffect(() => {
    const getAccessToken = async () => {
      try {
        const accessToken = await getAccessTokenSilently({
          audience: "jamsessions",
        });
        setAccessToken(accessToken);
        console.log(accessToken);
      } catch (e) {
        console.log(e.message);
      }
    };
    getAccessToken();
  });

  if (isLoading) {
    return <div>Loading ...</div>;
  }

  return (
    <Router>
      <Flex px={3} py={3} borderBottom="1px" borderColor="black.200">
        <Link mr={3} as={ReactLink} to="/">
          Home
        </Link>
        <Link mr={3} as={ReactLink} to="/sessions">
          Sessions
        </Link>
        <Spacer />
        <Box>
          {isAuthenticated ? (
            <Flex>
              <Box mr={3}>
                User <ChevronRightIcon /> {user.email}
              </Box>
              <LogoutButton />
            </Flex>
          ) : (
            <>
              <LoginButton />
            </>
          )}
        </Box>
      </Flex>
      <Switch>
        <Route path="/" component={MainLayout} exact></Route>
        <Route path="/verification" exact>
          <Verification
            email={user ? user.email : null}
            accessToken={accessToken}
          />
        </Route>
        <Route path="/sessions" exact>
          <Sessions accessToken={accessToken} />
        </Route>
        <Route path="/sessions/:session_id/update" exact>
          <SessionsUpdate accessToken={accessToken} />
        </Route>
        <Route path="/institutions" exact>
          <Institutions accessToken={accessToken} />
        </Route>
        <Route path="/musicians" exact>
          <Musicians accessToken={accessToken} />
        </Route>
        <Route path="/sessions/new" exact>
          <SessionsForm accessToken={accessToken} />
        </Route>
        <Route path="/register" exact component={Register}></Route>
        <Route path="/register/institutions" exact>
          <InstitutionsForm accessToken={accessToken} />
        </Route>
        <Route path="/register/musicians" exact>
          <MusiciansForm accessToken={accessToken} />
        </Route>
      </Switch>
    </Router>
  );
};

export default App;
