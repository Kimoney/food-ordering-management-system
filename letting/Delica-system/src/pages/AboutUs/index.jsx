import React from "react";
import { Helmet } from "react-helmet";
import { Img, Button, Text, Heading } from "../../components";
import Footer from "../../components/Footer";
import Header from "../../components/Header";

export default function AboutUsPage() {
  return (
    <>
      <Helmet>
        <title>About Delica - Your Digital Restaurant Experience</title>
        <meta
          name="description"
          content="Learn about Delica, a digital restaurant offering a variety of delicious foods including pizza, burgers, fries, and chicken. Partnered with Uber for doorstep delivery, we're dedicated to satisfying your appetite and supporting the economy."
        />
      </Helmet>
      <div className="flex w-full flex-col gap-[79px] bg-white-A700 pb-[71px] md:gap-[59px] md:pb-5 sm:gap-[39px]">
        <div className="flex flex-col items-center gap-[91px] md:gap-[68px] sm:gap-[45px]">
          {/* header section */}
          <Header className="flex items-center justify-center self-stretch bg-white-A700" />

          {/* about us section */}
          <div className="container-xs flex items-start gap-12 md:flex-col md:p-5">
            <div className="mt-[13px] flex flex-1 flex-col items-start md:self-stretch">
              <Heading size="4xl" as="h1" className="text-center !text-red-600">
                About Us
              </Heading>
              <Heading size="3xl" as="h2" className="mt-3 capitalize leading-[58px] !text-gray-900_01">
                order From Anywhere anytime.
              </Heading>
              <Text as="p" className="mt-5 leading-[26px] !text-gray-900">
                Delica is A Digital Restaurant that you can order The Four Delicious Foods that consist of a pizza, a
                burger, Fries and Chicken, and we have patnered with Uber that will deliver it to your door step. we are
                dedicate din serving your apetite and building the economy
              </Text>
              <Button
                size="sm"
                rightIcon={
                  <Img
                    src="images/img_materialsymbolsarrowforwardrounded.svg"
                    alt="material-symbols:arrow-forward-rounded"
                    className="h-[20px] w-[20px]"
                  />
                }
                className="mt-5 min-w-[157px] gap-2.5 rounded-[26px] font-medium"
              >
                Order Now
              </Button>
            </div>
            <div className="relative h-[514px] w-[48%] md:w-full">
              <div className="absolute bottom-0 left-0 right-0 top-0 m-auto h-[474px] w-[86%] rounded-tl-[10px] rounded-tr-[10px] bg-gray-100" />
              <Img
                src="images/img_rectangle_13.png"
                alt="image"
                className="absolute bottom-[0.00px] left-[0.00px] m-auto h-[246px] w-[68%] rounded-[10px] object-cover"
              />
              <Img
                src="images/img_rectangle_14.png"
                alt="image_one"
                className="absolute right-[0.12px] top-[0.00px] m-auto h-[246px] w-[68%] rounded-[10px] object-cover"
              />
            </div>
          </div>
        </div>

        {/* footer section */}
        <Footer className="flex flex-col items-start justify-end gap-[119px] bg-gray-900_03 py-[63px] md:gap-[89px] md:py-5 sm:gap-[59px]" />
      </div>
    </>
  );
}
