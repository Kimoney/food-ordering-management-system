import React from "react";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import { Helmet } from "react-helmet";
// import Listing from "../../components/Listing"; // Assuming Listing is in a different folder
import Listing from "pages/Listing"; // Assuming Listing is a separate page component
import { Button, Heading, Text, Img } from "../../components";
import Footer from "../../components/Footer";
import Header from "../../components/Header";

export default function Products() {
  return (
    <>
      <Helmet>
        <title>Our Menu - Explore Delica's Delicious Food Selections</title>
        <meta
          name="description"
          content="Discover Delica's menu featuring our top-rated Pizza, Hamburger, Fries, and Chicken. Indulge in a slice of heaven with our mouth-watering dishes, perfect for any appetite. Order now and savor the taste of Delica's finest."
        />
      </Helmet>
      <div className="flex w-full flex-col items-center bg-white-A700 pb-[71px] md:pb-5">
        {/* header section */}
        <Header className="flex items-center justify-center self-stretch bg-white-A700" />

        {/* featured products section */}
        <div className="container-xs mt-[58px] flex md:p-5">
          <div className="flex w-full flex-col items-center gap-[74px] bg-white-A700 p-[23px] md:gap-[55px] sm:gap-[37px] sm:p-5">
            <Heading
              size="2xl"
              as="h1"
              className="!font-montserrat !text-red-600"
            >
              Our Food
            </Heading>
            <div className="mb-6 flex gap-[35px] self-stretch md:flex-col">
              <div className="flex w-full flex-col items-start gap-[13px] bg-white-A700 p-6 shadow-sm sm:p-5">
                <Img
                  src="images/img_teenyicons_star_solid.svg"
                  alt="image"
                  className="h-[15px] w-[15px]"
                />
                <Text as="p" className="!text-black-900_7f">
                  4.5
                </Text>
                <Img
                  src="images/img_fernando_andrad.png"
                  alt="image_one"
                  className="h-[200px] w-full object-cover md:h-auto"
                />
                <Text size="lg" as="p" className="!text-black-900">
                  Pizza
                </Text>
                <Text as="p" className="!text-black-900_7f">
                  Indulge in a slice of heaven!
                </Text>
                <Heading as="h2" className="!font-extrabold">
                  ksh. 600
                </Heading>
                <Link to="/Listing">
                  <Button
                    shape="round"
                    className="w-full !rounded-[10px] sm:px-5"
                  >
                    Order now
                  </Button>
                </Link>
              </div>
              {/* Repeat this structure for other product sections */}
            </div>
          </div>
        </div>

        {/* footer section */}
        <Footer className="mt-[126px] flex flex-col items-start justify-end gap-[119px] self-stretch bg-gray-900_03 py-[63px] md:gap-[89px] md:py-5 sm:gap-[59px]" />
      </div>

      {/* Define routes to Listing and potentially other components */}
      <Routes>
        <Route path="/Listing" element={<Listing />} />
        {/* Add other routes here if needed */}
      </Routes>
    </>
  );
}
