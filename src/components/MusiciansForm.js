import React, { useState } from "react";
import { Container, Input, Text, Button, Center } from "@chakra-ui/react";
import { useAuth0 } from "@auth0/auth0-react";

export const MusiciansForm = ({ accessToken }) => {
  const { user } = useAuth0();
  const [name, setName] = useState("");
  const [genre, setGenre] = useState("");
  const [instrument, setInstrument] = useState("");
  const [email] = useState(user.email);
  const handleOnSubmit = (e) => {
    e.preventDefault();

    fetch("http://jamwithus.herokuapp.com/api/musicians", {
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
      method: "POST",
      body: JSON.stringify({
        name: name,
        genre: genre,
        instrument: instrument,
        email: user.email,
      }),
    })
      .then((response) => response.json())
      .then((newMusician) => {
        console.log(newMusician);
        window.location.href = "/";
      });
  };

  return (
    <Container py={5}>
      <Center borderRadius="md" p={3} bg="gray.100">
        Please let us know about you!
      </Center>
      <form onSubmit={handleOnSubmit} id="first-name">
        <Text>Name</Text>
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
        <Text>Genre</Text>
        <Input
          name="genre"
          onChange={(e) => {
            e.preventDefault();
            setGenre(e.target.value);
          }}
          value={genre}
          mb={2}
          type="text"
        />
        <Text>Instrument</Text>
        <Input
          name="instrument"
          onChange={(e) => {
            e.preventDefault();
            setInstrument(e.target.value);
          }}
          value={instrument}
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
