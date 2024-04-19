import React from "react";
import { Helmet } from "react-helmet";
import { Heading } from "../../components";
import CustomersTestimonial from "../../components/CustomersTestimonial";
import Footer from "../../components/Footer";
import Header from "../../components/Header";

const data = [
  {
    descriptiontext:
      "The Food is so delicious and crunchy, i recommend Delica to anyone who love a taste of good food",
    nametext: "Johnson White",
    roletext: "customer",
  },
  {
    descriptiontext:
      "The Food is so delicious and crunchy, i recommend Delica to anyone who love a taste of good food",
    nametext: "Dennis Kipkirui",
    roletext: "customer",
  },
  {
    descriptiontext:
      "The Food is so delicious and crunchy, i recommend Delica to anyone who love a taste of good food",
    nametext: "John Kimani",
    roletext: "customer",
  },
];

export default function CustomersPage() {
  return (
    <>
      <Helmet>
        <title>Customer Reviews - Delica Foods Testimonials</title>
        <meta
          name="description"
          content="Read customer reviews and testimonials for Delica Foods. Discover why our food is recommended for its delicious and crunchy taste. Join our satisfied customers!"
        />
      </Helmet>
      <div className="flex w-full flex-col items-center bg-white-A700 pb-[62px] md:pb-5">
        {/* header section */}
        <Header className="flex items-center justify-center self-stretch bg-white-A700" />

        {/* customer reviews section */}
        <div className="container-xs mt-[81px] flex flex-col items-center gap-[38px] md:p-5">
          <Heading
            size="2xl"
            as="h1"
            className="text-center !font-montserrat !text-red-600"
          >
            Customer reviews
          </Heading>
          <div className="flex gap-[61px] self-stretch bg-white-A700 p-[11px] md:flex-col">
            {data.map((d, index) => (
              <CustomersTestimonial
                {...d}
                key={"testimonial" + index}
                className="flex w-full flex-col items-center justify-center gap-[43px] bg-white-A700 shadow-xs md:p-5"
              />
            ))}
          </div>
        </div>

        {/* footer section */}
        <Footer className="mt-[47px] flex flex-col items-start justify-end gap-[119px] self-stretch bg-gray-900_03 py-[63px] md:gap-[89px] md:py-5 sm:gap-[59px]" />
      </div>
    </>
  );
}
