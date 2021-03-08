import React from "react";
import {
  useDisclosure,
  Box,
  Image,
  Badge,
  Button,
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalFooter,
  ModalBody,
  ModalCloseButton,
} from "@chakra-ui/react";
import { EmailIcon } from "@chakra-ui/icons";
import { useAuth0 } from "@auth0/auth0-react";
import { Link as ReactLink } from "react-router-dom";

export const SessionCard = ({ session }) => {
  const { user, getAccessTokenSilently } = useAuth0();
  const email = user.email;
  const { isOpen, onOpen, onClose } = useDisclosure();

  const handleOnClick = (e) => {
    e.preventDefault();
    const getAccessToken = async () => {
      try {
        const accessToken = await getAccessTokenSilently({
          audience: "jamsessions",
        });
        fetch(`http://jamwithus.herokuapp.com/api/sessions/${session.id}`, {
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
          method: "Delete",
        })
          .then((res) => res.json())
          .then((data) => {
            console.log(data);
            window.location.href = "/sessions";
          });
      } catch (e) {
        console.log(e.message);
      }
    };
    getAccessToken();
  };
  return (
    <Box maxW="sm" borderWidth="1px" borderRadius="lg" overflow="hidden">
      <Image
        src={
          session.imgURL
            ? session.imgURL
            : "https://images.unsplash.com/photo-1603219950587-b4f3f7ee87e7?ixid=MXwxMjA3fDB8MHx0b3BpYy1mZWVkfDJ8YWV1NnJMLWo2ZXd8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=60"
        }
        alt="session_image"
      />

      <Box p="6">
        <Box d="flex" alignItems="baseline">
          <Badge borderRadius="full" px="2" colorScheme="teal">
            {session.is_open ? "open" : "close"}
          </Badge>
          <Box
            color="gray.500"
            fontWeight="semibold"
            letterSpacing="wide"
            fontSize="xs"
            textTransform="uppercase"
            ml="2"
          >
            {session.location}
          </Box>
        </Box>

        <Box
          textTransform="capitalize"
          mt="1"
          fontWeight="semibold"
          as="h4"
          lineHeight="tight"
        >
          {session.title}
        </Box>
        <Box isTruncated>{session.description}</Box>

        <Box d="flex" mt="2" alignItems="center">
          <Box as="span" color="gray.600" fontSize="sm">
            {session.schedule}
          </Box>
        </Box>
      </Box>
      <Button w="100%" onClick={onOpen}>
        Show more
      </Button>

      <Modal isOpen={isOpen} onClose={onClose}>
        <ModalOverlay />
        <ModalContent>
          <ModalHeader textTransform="uppercase">{session.title}</ModalHeader>
          <ModalCloseButton />
          <ModalBody>
            <Box>
              <Image
                src={
                  session.imgURL
                    ? session.imgURL
                    : "https://images.unsplash.com/photo-1603219950587-b4f3f7ee87e7?ixid=MXwxMjA3fDB8MHx0b3BpYy1mZWVkfDJ8YWV1NnJMLWo2ZXd8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=60"
                }
                alt="session_image"
              />

              <Box p="6">
                <Box d="flex" alignItems="baseline">
                  <Badge borderRadius="full" px="2" colorScheme="teal">
                    {session.is_open ? "open" : "close"}
                  </Badge>
                  <Box
                    color="gray.500"
                    fontWeight="semibold"
                    letterSpacing="wide"
                    fontSize="xs"
                    textTransform="uppercase"
                    ml="2"
                  >
                    {session.location}
                  </Box>
                </Box>
                <Box>{session.description}</Box>

                <Box d="flex" mt="2" alignItems="center">
                  <Box as="span" color="gray.600" fontSize="sm">
                    {session.schedule}
                  </Box>
                </Box>
                <Box>
                  <EmailIcon /> {session.institution_email}
                </Box>
              </Box>
            </Box>
          </ModalBody>
          <ModalFooter>
            {email === session.institution_email && (
              <>
                <ReactLink to={`/sessions/${session.id}/update`}>
                  <Button colorScheme="yellow" mr={3} onClick={onClose}>
                    Update
                  </Button>
                </ReactLink>
                <Button onClick={handleOnClick} colorScheme="red">
                  Delete
                </Button>
              </>
            )}
          </ModalFooter>
        </ModalContent>
      </Modal>
    </Box>
  );
};
