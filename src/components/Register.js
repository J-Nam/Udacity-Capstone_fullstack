import React from "react";
import { Link as ReactLink } from "react-router-dom";

import { Container, Button, Box, Text } from "@chakra-ui/react";

export const Register = () => {
  return (
    <Container>
      <Text>Are you signing up as</Text>
      <Box>
        <ReactLink to="/register/institutions">
          <Button>Instution</Button>
        </ReactLink>
        <ReactLink to="/register/musicians">
          <Button>Musician</Button>
        </ReactLink>
      </Box>
    </Container>
  );
};
