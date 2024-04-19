// import React from "react";
// import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
// import Home from "pages/Home";
// import NotFound from "pages/NotFound";
// import Register from "pages/Register";
// import Customers from "pages/Customers";
// import Landingpage from "pages/Landingpage";
// import Products from "pages/Products";
// import AboutUsPage from "pages/AboutUs";

// function PRoutes() {
  
//     const [user, setUser] = useState(null);
  
//     useEffect(() => {
//       fetch("/check_session").then((response) => {
//         if (response.ok) {
//           response.json().then((user) => setUser(user));
//         }
//       });
//     }, []);
//   return (
//     <Router>
//       <Routes>
//         <Route path="/" element={<Landingpage />} />
//         <Route path="/register" element={<Register onLogin={setUser} />} />
//         <Route path="/customers" element={<Customers />} />

//         <Route path="/products" element={<Products />} />
//         <Route path="/aboutus" element={<AboutUsPage />} />
//         <Route path="*" element={<NotFound />} />
//       </Routes>
//     </Router>
//   );
// }

// export default PRoutes;
import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "pages/Home";
import NotFound from "pages/NotFound";
import Register from "pages/Register";
import Customers from "pages/Customers";
import Landingpage from "pages/Landingpage";
import Products from "pages/Products";
import AboutUsPage from "pages/AboutUs";

function PRoutes() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetch(" http://127.0.0.1:5000/check_session").then((response) => {
      if (response.ok) {
        response.json().then((user) => setUser(user));
      }
    });
  }, []);

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Landingpage />} />
        <Route path="/register" element={<Register onLogin={setUser} />} />
        <Route path="/customers" element={<Customers />} />

        {/* Pass the user state to the Products component */}
        <Route path="/products" element={<Products user={user} />} />
        
        <Route path="/aboutus" element={<AboutUsPage />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </Router>
  );
}

export default PRoutes;
