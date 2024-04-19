import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "pages/Home";
import NotFound from "pages/NotFound";
import Register from "pages/Register";
import Customers from "pages/Customers";
import Landingpage from "pages/Landingpage";
import Products from "pages/Products";
import AboutUsPage from "pages/AboutUs";

function PRoutes() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Landingpage />} />
        <Route path="/register" element={<Register />} />
        <Route path="/customers" element={<Customers />} />

        <Route path="/products" element={<Products />} />
        <Route path="/aboutus" element={<AboutUsPage />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </Router>
  );
}

export default PRoutes;
