import React from "react";
import { RatingBar, Text, Heading, Img } from "./..";

export default function CustomersTestimonial({
  descriptiontext = "The Food is so delicious and crunchy, i recommend Delica to anyone who love a taste of good food",
  nametext = "Johnson White",
  roletext = "customer",
  ...props
}) {
  return (
    <div {...props}>
      <div className="mt-[21px] flex flex-col items-center gap-[34px] self-stretch pb-[11px]">
        <Img src="images/img_rectangle_1_100x100.png" alt="circleimage" className="h-[100px] w-[100px] rounded-[50%]" />
        <Text size="md" as="p" className="text-center !text-blue_gray-900">
          {descriptiontext}
        </Text>
        <div className="ml-[73px] flex flex-col items-center gap-1.5 self-start md:ml-0">
          <Heading size="xs" as="h1" className="text-center">
            {nametext}
          </Heading>
          <Text size="xs" as="p" className="text-center !text-gray-700">
            {roletext}
          </Text>
        </div>
      </div>
      <RatingBar
        value={5}
        isEditable={true}
        color="#f24e1e"
        activeColor="#f24e1e"
        size={25}
        className="mb-[21px] flex justify-between"
      />
    </div>
  );
}
