import React from "react";
import { Helmet } from "react-helmet";
import { Text, Button, Input, Img, Heading } from "../../components";
import Footer from "../../components/Footer";
import Header from "../../components/Header";

export default function RegisterPage() {
  return (
    <>
      <Helmet>
        <title>Register for Delica Foods - Crunchy Delights Await</title>
        <meta
          name="description"
          content="Join Delica Foods and indulge in the crunchiest delights. Register now to explore our products and enjoy exclusive offers. Sign up today!"
        />
      </Helmet>
      <div className="flex w-full flex-col bg-white-A700 pb-[71px] md:pb-5">
        <div>
          {/* header section */}
          <Header className="flex items-center justify-center bg-white-A700" />
        </div>

        {/* hero section */}
        <div className="mx-auto mt-[107px] flex w-full max-w-[1086px] items-center md:flex-col md:p-5">
          <div className="relative h-[530px] w-[46%] md:h-auto md:w-full">
            <Img src="images/img_rectangle_1.png" alt="image" className="h-[530px] w-full object-cover" />
            <div className="absolute bottom-0 left-0 right-0 top-0 m-auto flex h-max w-full flex-col items-start gap-[21px] bg-black-900_bf py-[125px] pl-[125px] pr-14 md:p-5">
              <Heading size="2xl" as="h1" className="mt-[33px] !font-montserrat !font-bold !text-white-A700">
                <span className="text-white-A700">Delica</span>
                <span className="text-deep_orange-600">.</span>
              </Heading>
              <Heading size="md" as="h2" className="mb-[149px] !font-montserrat !text-white-A700">
                Crave a crunchy delight
              </Heading>
            </div>
          </div>

          {/* registration section */}
          <div className="flex flex-1 flex-col items-start gap-7 bg-white-A700 p-10 md:self-stretch sm:p-5">
            <a href="Register" target="_blank" rel="noreferrer" className="ml-[110px] md:ml-0">
              <Heading size="lg" as="h2" className="!font-montserrat">
                Register
              </Heading>
            </a>
            <div className="flex w-[51%] flex-col gap-3 self-center md:w-full">
              <div className="flex flex-col items-start gap-[5px]">
                <Text as="p" className="!text-gray-800">
                  Username
                </Text>
                <Input shape="round" type="text" name="userName" placeholder={`Username`} className="sm:pr-5" />
              </div>
              <div className="flex flex-col items-start gap-[5px]">
                <Text as="p" className="!text-gray-800">
                  Email
                </Text>
                <Input shape="round" type="email" name="email" placeholder={`Email`} className="sm:pr-5" />
              </div>
              <div className="flex flex-col items-start gap-[5px]">
                <Text as="p" className="!text-gray-800">
                  Password
                </Text>
                <Input
                  shape="round"
                  type="password"
                  name="password"
                  placeholder={`Password`}
                  suffix={<Img src="images/img_eye.svg" alt="eye" className="h-[16px] w-[16px]" />}
                  className="gap-[35px]"
                />
              </div>
              <div className="flex flex-col items-start gap-1">
                <Text as="p" className="!text-gray-800">
                  Confirm password
                </Text>
                <Input
                  shape="round"
                  type="password"
                  name="confirmpassword"
                  placeholder={`Password`}
                  suffix={<Img src="images/img_eye.svg" alt="eye" className="h-[16px] w-[16px]" />}
                  className="gap-[35px]"
                />
              </div>
              <Button color="deep_orange_600" shape="round" className="w-full !rounded-[10px] sm:px-5">
                Submit
              </Button>
            </div>
            <a href="#" className="mb-[9px] ml-[110px] md:ml-0">
              <Text as="p" className="!text-black-900_7f">
                Already have an account?
              </Text>
            </a>
          </div>
        </div>

        {/* footer section */}
        <div>
          <Footer className="mt-[146px] flex flex-col items-start justify-end gap-[119px] bg-gray-900_03 py-[63px] md:gap-[89px] md:py-5 sm:gap-[59px]" />
        </div>
      </div>
    </>
  );
}
