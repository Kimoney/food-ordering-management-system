import React from "react";
import { useRoutes } from "react-router-dom";
import Home from "pages/Home";
import NotFound from "pages/NotFound";
import Register from "pages/Register";
import Customers from "pages/Customers";
import Landingpage from "pages/Landingpage";
import Products from "pages/Products";
import AboutUs from "pages/AboutUs";

const ProjectRoutes = () => {
  let element = useRoutes([
    { path: "/", element: <Home /> },
    { path: "*", element: <NotFound /> },
    {
      path: "register",
      element: <Register />,
    },
    {
      path: "customers",
      element: <Customers />,
    },
    {
      path: "landingpage",
      element: <Landingpage />,
    },
    {
      path: "products",
      element: <Products />,
    },
    {
      path: "aboutus",
      element: <AboutUs />,
    },
  ]);

  return element;
};

export default ProjectRoutes;
