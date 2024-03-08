// In src/pages/SignUp.js
import React from "react";
import { useHistory, Link } from "react-router-dom";
import { Formik, Form, Field, ErrorMessage } from "formik";
import * as Yup from "yup";

function SignUp() {
  const history = useHistory();

  const initialValues = {
    name: "",
    email: "",
    password: "",
    organization: "",
  };

  const validationSchema = Yup.object({
    name: Yup.string().required("Required"),
    email: Yup.string().email("Invalid email address").required("Required"),
    password: Yup.string().required("Required"),
    organization: Yup.string().required("Required"),
  });

  const handleSubmit = async (values, { setSubmitting }) => {
    // Implement the logic to send values to your backend server
    try {
      const response = await fetch("http://127.0.0.1:5555/users", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(values),
      });
      if (!response.ok) throw new Error("Signup failed");
      history.push("/login"); // Redirect to login page upon successful signup
    } catch (error) {
      console.error("Signup error:", error);
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <main className="form-container">
      <div className="text-center">
        <h1 className="block text-2xl font-bold">Sign up</h1>
        <p className="mt-2">
          Already have an account?{" "}
          <Link to="/login" className="text-primary-color">
            Sign in here
          </Link>
        </p>
      </div>

      <Formik
        initialValues={initialValues}
        validationSchema={validationSchema}
        onSubmit={handleSubmit}
      >
        {({ isSubmitting }) => (
          <Form className="grid-single-column">
            <Field
              name="name"
              type="text"
              placeholder="Name"
              className="form-group input"
            />
            <ErrorMessage
              name="name"
              component="div"
              className="text-red-500 text-xs"
            />

            <Field
              name="email"
              type="email"
              placeholder="Email"
              className="form-group input"
            />
            <ErrorMessage
              name="email"
              component="div"
              className="text-red-500 text-xs"
            />

            <Field
              name="organization"
              type="text"
              placeholder="Organization"
              className="form-group input"
            />
            <ErrorMessage
              name="organization"
              component="div"
              className="text-red-500 text-xs"
            />

            <Field
              name="password"
              type="password"
              placeholder="Password"
              className="form-group input"
            />
            <ErrorMessage
              name="password"
              component="div"
              className="text-red-500 text-xs"
            />

            <button type="submit" disabled={isSubmitting} className="button">
              Get started
            </button>
          </Form>
        )}
      </Formik>
    </main>
  );
}

export default SignUp;
