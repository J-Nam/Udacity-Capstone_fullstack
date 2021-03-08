import React, { useEffect, useState } from "react";
import {
  Avatar,
  Container,
  Flex,
  Box,
  Text,
  SimpleGrid,
} from "@chakra-ui/react";

export const Musicians = ({ accessToken }) => {
  const [musicians, setMusicians] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    fetch("http://jamwithus.herokuapp.com/api/musicians", {
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.musicians !== "no data") {
          setMusicians(data.musicians);
        }
        setIsLoading(false);
      });
  }, []);
  const musicianCards = musicians.map((m) => {
    return (
      <Flex mb={3} align="center">
        <Avatar mr={3} bg="teal.500" size="md" />
        <Box>
          <Text textTransform="capitalize">{m.name}</Text>
          <Text fontSize="sm">
            🎵
            {m.genre} 😊
            {m.instrument} ✉️
            {m.email}
          </Text>
        </Box>
      </Flex>
    );
  });

  return (
    isLoading && <h1>Loading...</h1>,
    !isLoading && (
      <Container centerContent my={5} maxW="container.lg">
        <Box
          h={100}
          w="100%"
          bg="gray.200"
          d="flex"
          justifyContent="center"
          alignItems="center"
          mb={3}
          fontSize="lg"
        >
          Here are musicians who are joining us! Check out the list below.
        </Box>
        <SimpleGrid spacing={15} columns={2}>
          {musicianCards}
        </SimpleGrid>
      </Container>
    )
  );
};
