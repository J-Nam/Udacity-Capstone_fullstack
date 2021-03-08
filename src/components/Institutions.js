import React, { useEffect, useState } from "react";
import {
  Avatar,
  Container,
  Flex,
  Box,
  Text,
  SimpleGrid,
} from "@chakra-ui/react";
import { AtSignIcon } from "@chakra-ui/icons";

export const Institutions = ({ accessToken }) => {
  const [institutions, setInstitutions] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  useEffect(() => {
    fetch("http://jamwithus.herokuapp.com/api/institutions", {
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        if (data.institutions !== "no data") {
          setInstitutions(data.institutions);
        }
        setIsLoading(false);
      });
  }, []);
  const institutionCards = institutions.map((i) => {
    return (
      <Flex mb={3} align="center">
        <Avatar mr={3} bg="teal.500" size="md" />
        <Box>
          <Text textTransform="capitalize">{i.name}</Text>
          <Text fontSize="sm">
            <AtSignIcon mr={1} />
            {i.location}
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
          w="80%"
          bg="gray.200"
          d="flex"
          justifyContent="center"
          alignItems="center"
          mb={3}
          fontSize="lg"
        >
          A number of institutions are with us, check out the list below!
        </Box>
        <SimpleGrid spacing={20} columns={2}>
          {institutionCards}
        </SimpleGrid>
      </Container>
    )
  );
};
