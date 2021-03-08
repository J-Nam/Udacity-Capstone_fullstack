import React, { useState } from "react";
import { Container, Input, Button, Center, Text } from "@chakra-ui/react";
import { useAuth0 } from "@auth0/auth0-react";

export const SessionsForm = ({ accessToken }) => {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [location, setLocation] = useState("");
  const [schedule, setSchedule] = useState("");
  const [imgURL, setImgURL] = useState("");

  const { user } = useAuth0();
  const handleOnSubmit = (e) => {
    e.preventDefault();
    console.log("from session from");

    fetch("http://jamwithus.herokuapp.com/api/sessions", {
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
      method: "POST",
      body: JSON.stringify({
        institution_email: user.email,
        title: title,
        description: description,
        location: location,
        schedule: schedule,
        imgURL: imgURL,
      }),
    })
      .then((response) => response.json())
      .then((newSession) => {
        console.log(newSession);
        window.location.href = "/sessions";
      });
  };

  return (
    <Container py={5}>
      <Center borderRadius="md" p={3} bg="gray.100">
        Please let us know what you are planning in detail!
      </Center>
      <form onSubmit={handleOnSubmit} id="first-name">
        <Text>Title</Text>
        <Input
          name="title"
          onChange={(e) => {
            e.preventDefault();
            setTitle(e.target.value);
          }}
          value={title}
          mb={2}
          type="text"
        />
        <Text>Description</Text>
        <Input
          name="description"
          onChange={(e) => {
            e.preventDefault();
            setDescription(e.target.value);
          }}
          value={description}
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
          placeholder="City, Province, Country "
        />
        <Text>Schedule</Text>
        <Input
          name="schedule"
          onChange={(e) => {
            e.preventDefault();
            setSchedule(e.target.value);
          }}
          value={schedule}
          mb={2}
          type="text"
          placeholder="YYYY-MM-DD HH:MM:SS"
        />
        <Text>Img</Text>
        <Input
          name="imgURL"
          onChange={(e) => {
            e.preventDefault();
            setImgURL(e.target.value);
          }}
          value={imgURL}
          type="text"
          placeholder="If you leave this field blank, we will use a default image"
        />
        <Button type="submit" my={3}>
          Submit
        </Button>
      </form>
    </Container>
  );
};
