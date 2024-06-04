/* This script is the page for the Login page */
import React from "react";
import Form from "../components/Form";

function Login() {
  return <Form route="/api/token/" method="login" />;
}

export default Login;
