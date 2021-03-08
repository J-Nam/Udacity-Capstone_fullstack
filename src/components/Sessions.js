import React, { useState, useEffect } from "react";
import { Container, Button, Box, Text, SimpleGrid } from "@chakra-ui/react";
import { Link as ReactLink } from "react-router-dom";
import { useAuth0 } from "@auth0/auth0-react";

import { SessionCard } from "./SessionCard";

export const Sessions = ({ accessToken }) => {
  const { user } = useAuth0();
  const [session, setSession] = useState([]);
  const [isInstitution, setIsInstitution] = useState(false);
  const [isLodding, setIsLodding] = useState(true);

  useEffect(() => {
    fetch(`http://jamwithus.herokuapp.com/api/sessions/${user.email}`, {
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        if (data.sessions !== "no data") {
          setIsInstitution(data.isInstitution);
          setSession(data.sessions);
        }
        setIsLodding(false);
      });
  }, []);

  const sessions = session.map((session) => {
    return <SessionCard session={session} />;
  });
  return (
    !isLodding && (
      <>
        <Container maxW="container.lg" py={3}>
          {isInstitution ? (
            <Box bg="teal.200" p={3}>
              <Text display="flex" justifyContent="center">
                Want to list a new session?
              </Text>
              <Box mt={3} display="flex" justifyContent="center">
                <ReactLink to="/sessions/new">
                  <Button>CREATE</Button>
                </ReactLink>
              </Box>
            </Box>
          ) : null}
          <SimpleGrid my={5} columns={[2, 2, 3, 4, 4]} spacing={3}>
            {sessions}
          </SimpleGrid>
        </Container>
      </>
    )
  );
};
