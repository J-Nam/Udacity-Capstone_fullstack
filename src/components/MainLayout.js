import React from "react";
import {
  Container,
  Button,
  Text,
  Heading,
  Box,
  Image,
  Flex,
} from "@chakra-ui/react";
import { Link as ReactLink } from "react-router-dom";

export const MainLayout = () => {
  return (
    <Container maxW="container.sm" mt={3}>
      <Heading d="flex" justifyContent="center">
        Jam With Us
      </Heading>
      <Image
        my={3}
        src="https://images.unsplash.com/photo-1514320291840-2e0a9bf2a9ae?ixid=MXwxMjA3fDB8MHxzZWFyY2h8M3x8bXVzaWN8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=60"
      ></Image>
      <Text>
        Are you looking for musicians for an event that you are planning? Are
        you looking for an event where you can jam with other talents and give
        back to community at the same time? We are here for you guys!👋
      </Text>
      <Flex align="center" justify="space-between" py={5} px={2}>
        <ReactLink to="/institutions">
          <Button colorScheme="teal">Institutions</Button>
        </ReactLink>
        <Box fontSize="lg">
          <Text d="flex" justifyContent="center" bg="gray.200">
            👈 Go check out who are joining us! 👉
          </Text>
        </Box>
        <ReactLink to="/musicians">
          <Button colorScheme="teal">Musicians</Button>
        </ReactLink>
      </Flex>
    </Container>
  );
};
