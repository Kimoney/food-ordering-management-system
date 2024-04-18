import React from "react";
import { Helmet } from "react-helmet";
import { Img, Heading, Text, Button } from "../../components";
import CustomersTestimonial from "../../components/CustomersTestimonial";
import Header from "../../components/Header";

const data = [
  {
    descriptiontext: "The Food is so delicious and crunchy, i recommend Delica to anyone who love a taste of good food",
    nametext: "Johnson White",
    roletext: "customer",
  },
  {
    descriptiontext: "The Food is so delicious and crunchy, i recommend Delica to anyone who love a taste of good food",
    nametext: "Johnson White",
    roletext: "customer",
  },
  {
    descriptiontext: "The Food is so delicious and crunchy, i recommend Delica to anyone who love a taste of good food",
    nametext: "Johnson White",
    roletext: "customer",
  },
];
const data1 = [
  { imageone: "images/img_fernando_andrad.png", pizza: "Pizza", kshCounter: "ksh. 600" },
  { imageone: "images/img_fernando_andrad_200x198.png", pizza: "Hambuger", kshCounter: "Ksh.450" },
  { imageone: "images/img_fernando_andrad_1.png", pizza: "Fries", kshCounter: "Ksh. 200" },
  { imageone: "images/img_fernando_andrad_2.png", pizza: "Chicken", kshCounter: "Ksh. 750" },
];

export default function LandingpagePage() {
  return (
    <>
      <Helmet>
        <title>Order Food Online - Delica Digital Restaurant</title>
        <meta
          name="description"
          content="Delica is your go-to digital restaurant for ordering pizza, burgers, fries, and chicken. Enjoy 4.5-star meals delivered to your doorstep. Order now and satisfy your appetite!"
        />
      </Helmet>
      <div className="flex w-full flex-col items-center bg-white-A700 pb-[71px] md:pb-5">
        {/* header section */}
        <Header className="flex items-center justify-center self-stretch bg-white-A700" />
        <div className="mx-auto mt-[114px] flex w-full max-w-[1159px] flex-col gap-[38px] md:p-5">
          {/* hero section */}
          <div>
            <div className="flex items-center justify-between gap-5 bg-white-A700 p-6 md:flex-col sm:p-5">
              <div className="ml-12 flex w-[48%] flex-col items-start gap-[29px] md:ml-0 md:w-full">
                <Heading size="3xl" as="h1" className="!font-inriasans !font-bold">
                  <span className="text-black-900">Delica</span>
                  <span className="text-red-600">. Foods</span>
                </Heading>
                <Heading as="h2" className="!font-inriasans leading-[120%] tracking-[-0.32px]">
                  This is a website for a fictional company that develops app that provides features and services for
                  its users
                </Heading>
                <Button size="sm" shape="round" className="w-full font-inriasans font-bold sm:px-5">
                  Get Your order now
                </Button>
              </div>
              <div className="relative mr-12 h-[383px] w-[37%] md:mr-0 md:w-full">
                <div className="absolute left-[0.00px] top-[0.00px] m-auto flex w-[93%] flex-col items-end">
                  <Img
                    src="images/img_jema_luis_285_09.png"
                    alt="jemaluis285_one"
                    className="relative z-[2] mr-[9px] h-[100px] w-[100px] rounded-[50px] object-cover md:mr-0"
                  />
                  <div className="relative mt-[-66px] flex items-center self-stretch">
                    <Img
                      src="images/img_18514975_2.png"
                      alt="circleimage"
                      className="relative z-[3] mb-[33px] h-[100px] w-[100px] self-end rounded-[50%]"
                    />
                    <div className="relative ml-[-50px] flex flex-1 flex-col items-center justify-end rounded-[150px] bg-gradient px-14 py-[75px] md:p-5">
                      <Img
                        src="images/img_5d8s_msa7_210608.png"
                        alt="5d8smsaseven"
                        className="mb-[23px] mt-14 h-[70px] w-[80%] rounded-[35px] object-cover"
                      />
                    </div>
                  </div>
                </div>
                <Img
                  src="images/img_2192_1.png"
                  alt="image"
                  className="absolute bottom-[-0.95px] right-[0.21px] m-auto h-[100px] w-[36%] rounded-[50px] object-cover"
                />
              </div>
            </div>

            {/* about section */}
            <div className="relative mt-[183px] h-[1175px] md:h-auto">
              <div className="w-full">
                <div className="relative z-[4] pl-[791px] md:pl-5">
                  <Img
                    src="images/img_rectangle_14.png"
                    alt="image_one"
                    className="h-[246px] w-full rounded-[10px] object-cover md:h-auto"
                  />
                </div>
                <div className="relative mt-[-232px] flex flex-col">
                  <div className="relative z-[5] flex w-[50%] flex-col items-start md:w-full">
                    <Heading size="4xl" as="h3" className="text-center !text-red-600">
                      About Us
                    </Heading>
                    <Heading size="3xl" as="h4" className="mt-3 capitalize leading-[58px] !text-gray-900_01">
                      order From Anywhere anytime.
                    </Heading>
                    <Text as="p" className="mt-5 leading-[26px] !text-gray-900">
                      Delica is A Digital Restaurant that you can order The Four Delicious Foods that consist of a
                      pizza, a burger, Fries and Chicken, and we have patnered with Uber that will deliver it to your
                      door step. we are dedicate din serving your apetite and building the economy
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
                  <div className="relative mt-[-148px]">
                    <div className="relative z-[6] flex flex-col items-end pl-14 pr-[170px] md:px-5">
                      <Img
                        src="images/img_rectangle_13.png"
                        alt="image_two"
                        className="h-[246px] w-[39%] rounded-[10px] object-cover"
                      />
                    </div>
                    <div className="relative mt-[-20px] flex flex-col items-center gap-[74px] bg-white-A700 p-[23px] md:gap-[55px] sm:gap-[37px] sm:p-5">
                      <Heading size="2xl" as="h5" className="!font-montserrat !text-red-600">
                        Our Food
                      </Heading>
                      <div className="mb-6 flex gap-[35px] self-stretch md:flex-col">
                        {data1.map((d, index) => (
                          <div
                            key={"listpizza" + index}
                            className="flex w-full flex-col items-start gap-[13px] bg-white-A700 p-6 shadow-sm sm:p-5"
                          >
                            <Img src="images/img_teenyicons_star_solid.svg" alt="image" className="h-[15px] w-[15px]" />
                            <Text as="p" className="!text-black-900_7f">
                              4.5
                            </Text>
                            <Img src={d.imageone} alt="image_one" className="h-[200px] w-full object-cover md:h-auto" />
                            <div className="flex flex-col items-start gap-[13px] self-stretch">
                              <Text size="lg" as="p" className="!text-black-900">
                                {d.pizza}
                              </Text>
                              <Text as="p" className="!text-black-900_7f">
                                Indulge in a slice of heaven!
                              </Text>
                              <Heading as="h6" className="!font-extrabold">
                                {d.kshCounter}
                              </Heading>
                              <Button shape="round" className="w-full !rounded-[10px] sm:px-5">
                                Order now
                              </Button>
                            </div>
                          </div>
                        ))}
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div className="absolute right-[3%] top-[20.00px] m-auto h-[474px] w-[40%] rounded-tl-[10px] rounded-tr-[10px] bg-gray-100" />
            </div>

            {/* customer reviews section */}
            <div className="relative z-[1] mt-[-1px] flex flex-col items-center px-[395px] md:px-5">
              <Heading size="2xl" as="h1" className="text-center !font-montserrat !text-red-600">
                Customer reviews
              </Heading>
            </div>
          </div>

          {/* testimonials section */}
          <div className="flex gap-[61px] bg-white-A700 p-[11px] md:flex-col">
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
        <footer className="mt-[59px] flex flex-col gap-3.5 self-stretch bg-gray-900_03 py-[63px] md:py-5">
          <div className="mt-[71px] flex items-start pb-[105px] pl-[105px] pr-14 md:flex-col md:px-5 md:pb-5">
            <div className="ml-[13px] mt-3.5 flex w-[30%] items-center justify-center gap-2.5 bg-blue_gray-100 p-2 md:ml-0 md:w-full">
              <div className="h-[41px] w-[41px] self-end rounded-[20px] bg-red-600" />
              <Heading size="xl" as="h2" className="self-start !font-inriasans">
                <span className="text-black-900">Delica</span>
                <span className="text-red-600">.</span>
              </Heading>
            </div>
            <div className="ml-[167px] mt-[9px] flex flex-col md:ml-0">
              <ul className="flex flex-col items-start gap-[29px]">
                <li>
                  <a href="#">
                    <Text as="p">Home</Text>
                  </a>
                </li>
                <li>
                  <a href="#">
                    <Text as="p">Our food</Text>
                  </a>
                </li>
                <li>
                  <a href="#">
                    <Text as="p">Customer Reviews</Text>
                  </a>
                </li>
                <li>
                  <a href="#">
                    <Text as="p">Login</Text>
                  </a>
                </li>
              </ul>
            </div>
            <div className="ml-60 flex flex-col md:ml-0">
              <ul className="flex flex-col items-start gap-7">
                <li>
                  <a href="#">
                    <Text as="p">Pinterest</Text>
                  </a>
                </li>
                <li>
                  <a href="#">
                    <Text as="p">Instagram</Text>
                  </a>
                </li>
                <li>
                  <a href="#">
                    <Text as="p">X-spaces</Text>
                  </a>
                </li>
                <li>
                  <a href="#">
                    <Text as="p">Facebook</Text>
                  </a>
                </li>
              </ul>
            </div>
            <div className="ml-60 flex flex-col md:ml-0">
              <ul className="flex flex-col items-start gap-7">
                <li>
                  <a href="#">
                    <Text as="p">Pinterest</Text>
                  </a>
                </li>
                <li>
                  <a href="#">
                    <Text as="p">Instagram</Text>
                  </a>
                </li>
                <li>
                  <a href="#">
                    <Text as="p">X-spaces</Text>
                  </a>
                </li>
                <li>
                  <a href="#">
                    <Text as="p">Facebook</Text>
                  </a>
                </li>
              </ul>
            </div>
          </div>
          <div className="flex items-center justify-between gap-5 bg-gray-900_02 px-12 pt-12 md:px-5 md:pt-5 sm:flex-col">
            <Heading as="h6" className="ml-16 mt-[3px] self-start !text-blue_gray-300 md:ml-0">
              © 2024 Delica. Foods. All rights reserved.
            </Heading>
            <div className="mr-16 flex w-[18%] justify-between gap-5 md:mr-0 sm:w-full">
              <Img src="images/img_social_icon.png" alt="socialicon_one" className="h-px object-cover" />
              <Img src="images/img_vector.png" alt="vector_one" className="h-px object-cover" />
              <Img src="images/img_social_icon_blue_gray_300.png" alt="socialicon" className="h-px object-cover" />
              <Img
                src="images/img_social_icon_blue_gray_300_1x24.png"
                alt="socialicon_five"
                className="h-px object-cover"
              />
              <Img src="images/img_vector_blue_gray_300.png" alt="vector_three" className="h-px object-cover" />
            </div>
          </div>
        </footer>
      </div>
    </>
  );
}
