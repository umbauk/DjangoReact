/*
 * Contains functions which call the back-end
 */

import axios from "axios";

const register = (fields) => {
  return axios.post("/api/users/register", fields);
};

const login = async (fields) => {
  fields = {
    username: fields.email,
    password: fields.password
  }
  const res = await axios.post("/api/login/", fields)
  console.log(res)
  localStorage.setItem('token', res.data.access)
  return res
};

const getUser = async () => {
  const response = await axios.get(`/api/current_user/`);
  return response.data;
};

const logOutUser = () => {
  return axios.post("/api/users/logout");
};

const getAllMessages = async () => {
  const response = await axios.get("/api/customers");
  return response.data;
};

const createNewCustomer = (fields) => {
  return axios.post("/api/customers/create", fields);
};

const sendMessage = async (content, customerId) => {
  return axios.post("/api/messages/send", { content, customerId });
};

export {
  register,
  login,
  getUser,
  logOutUser,
  getAllMessages,
  createNewCustomer,
  sendMessage,
};
