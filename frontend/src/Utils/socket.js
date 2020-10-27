/*
 * Establishes connection to the socket server
 */

import io from "socket.io-client";

const connect = (userId) => {
  const url =
    process.env.NODE_ENV === "production"
      ? process.env.REACT_APP_SERVER_URL
      : process.env.DEV_SERVER_URL;
  return io(url, { query: { userId } });
};

export default connect;
