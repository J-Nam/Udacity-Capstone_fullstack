import React, { useState } from "react";
import { Container, Input, Text, Button, Center } from "@chakra-ui/react";
import { useAuth0 } from "@auth0/auth0-react";

export const InstitutionsForm = ({ accessToken }) => {
  const { user } = useAuth0();
  const [name, setName] = useState("");
  const [location, setLocation] = useState("");
  const [email] = useState(user.email);
  const handleOnSubmit = (e) => {
    e.preventDefault();

    fetch("http://jamwithus.herokuapp.com/api/institutions", {
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
      method: "POST",
      body: JSON.stringify({
        name: name,
        location: location,
        email: user.email,
      }),
    })
      .then((response) => response.json())
      .then((newInstitution) => {
        window.location.href = "/";
      });
  };

  return (
    <Container py={5}>
      <Center borderRadius="md" p={3} bg="gray.100">
        Please let us know about you!
      </Center>
      <form onSubmit={handleOnSubmit} id="first-name">
        <Text>Name of Institution</Text>
        <Input
          name="name"
          onChange={(e) => {
            e.preventDefault();
            setName(e.target.value);
          }}
          value={name}
          mb={2}
          type="text"
        />
        <Text>Location</Text>
        <Input
          name="location"
          onChange={(e) => {
            e.preventDefault();
            setLocation(e.target.value);
          }}
          value={location}
          mb={2}
          type="text"
        />
        <Text>Email</Text>
        <Input name="email" value={email} type="text" disabled />
        <Button type="submit" my={3}>
          Submit
        </Button>
      </form>
    </Container>
  );
};
