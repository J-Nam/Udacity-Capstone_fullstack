import React from "react";
import { Container, Button, Flex, Box } from "@chakra-ui/react";

export const Verification = ({ email, accessToken }) => {
  const handleOnclick = (e) => {
    const type = e.target.id;

    fetch(`http://jamwithus.herokuapp.com/api/verification/${type}/${email}`, {
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.success === true) {
          window.location.href = "/";
        } else {
          type === "institution"
            ? (window.location.href = "/register/institutions")
            : (window.location.href = "/register/musicians");
        }
      });
  };
  return (
    <Container>
      <Box
        my={3}
        h={100}
        w="100%"
        bg="gray.200"
        d="flex"
        justifyContent="center"
        alignItems="center"
        mb={3}
        fontSize="lg"
      >
        Are you signing in as...
      </Box>
      <Flex justify="space-around">
        <Button colorScheme="teal" id="institution" onClick={handleOnclick}>
          institution
        </Button>
        <Button colorScheme="teal" id="music" onClick={handleOnclick}>
          musician
        </Button>
      </Flex>
    </Container>
  );
};
