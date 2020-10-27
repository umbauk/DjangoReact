/*
 * Contains functions which call the back-end
 */

import axios from "axios";

const register = async (fields) => {
  fields = {
    first_name: fields.firstName,
    last_name: fields.lastName,
    email: fields.email,
    password: fields.password
  }
  const res = await axios.post("/api/users/register", fields);
  console.log(res)
  // return res
};

const login = async (fields) => {
  const res = await axios.post("/api/users/login/", fields)
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
