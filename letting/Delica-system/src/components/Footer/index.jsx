import React from "react";
import { Img, Heading, Text } from "./..";

export default function Footer({ ...props }) {
  return (
    <footer {...props}>
      <div className="mx-auto mt-[71px] flex w-full max-w-[1100px] items-start md:flex-col md:p-5">
        <div className="mt-3.5 flex w-[41%] items-center justify-center gap-2.5 bg-blue_gray-100 p-2 md:w-full">
          <div className="h-[41px] w-[41px] self-end rounded-[20px] bg-red-600" />
          <Heading size="xl" as="h2" className="self-start !font-inriasans">
            <span className="text-black-900">Delica</span>
            <span className="text-red-600">.</span>
          </Heading>
        </div>
        <div className="ml-[167px] mt-[9px] flex flex-col md:ml-0">
          <ul className="flex flex-col items-start gap-[29px]">
            <li>
              <a href="Home" target="_blank" rel="noreferrer">
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
              <a href="Login" target="_blank" rel="noreferrer">
                <Text as="p">Login</Text>
              </a>
            </li>
          </ul>
        </div>
        <div className="ml-60 flex flex-col md:ml-0">
          <ul className="flex flex-col items-start gap-7">
            <li>
              <a href="Pinterest" target="_blank" rel="noreferrer">
                <Text as="p">Pinterest</Text>
              </a>
            </li>
            <li>
              <a href="Instagram" target="_blank" rel="noreferrer">
                <Text as="p">Instagram</Text>
              </a>
            </li>
            <li>
              <a href="X-spaces" target="_blank" rel="noreferrer">
                <Text as="p">X-spaces</Text>
              </a>
            </li>
            <li>
              <a href="Facebook" target="_blank" rel="noreferrer">
                <Text as="p">Facebook</Text>
              </a>
            </li>
          </ul>
        </div>
        <div className="ml-60 flex flex-col md:ml-0">
          <ul className="flex flex-col items-start gap-7">
            <li>
              <a href="Pinterest" target="_blank" rel="noreferrer">
                <Text as="p">Pinterest</Text>
              </a>
            </li>
            <li>
              <a href="Instagram" target="_blank" rel="noreferrer">
                <Text as="p">Instagram</Text>
              </a>
            </li>
            <li>
              <a href="X-spaces" target="_blank" rel="noreferrer">
                <Text as="p">X-spaces</Text>
              </a>
            </li>
            <li>
              <a href="Facebook" target="_blank" rel="noreferrer">
                <Text as="p">Facebook</Text>
              </a>
            </li>
          </ul>
        </div>
      </div>
      <div className="flex items-center justify-between gap-5 self-stretch bg-gray-900_02 px-12 pt-12 md:px-5 md:pt-5 sm:flex-col">
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
  );
}
