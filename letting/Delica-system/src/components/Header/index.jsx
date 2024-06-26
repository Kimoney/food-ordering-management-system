import React from "react";
import { NavLink } from "react-router-dom";
import { Button, Heading } from "./..";

export default function Header({ ...props }) {
  return (
    <header {...props}>
      <div className="container-xs flex items-center justify-between gap-5 md:flex-col md:p-5">
        <div className="flex w-[16%] items-center justify-center gap-2.5 bg-blue_gray-100 p-2 md:w-full">
          <div className="h-[41px] w-[41px] self-end rounded-[20px] bg-red-600" />
          <Heading size="xl" as="h2" className="self-start !font-inriasans">
            <span className="text-black-900">Delica</span>
            <span className="text-red-600">.</span>
          </Heading>
        </div>
        <div className="flex w-[46%] items-center justify-between gap-5 pl-5 md:w-full sm:flex-col">
          <ul className="flex flex-wrap gap-[52px] md:gap-5">
            <li>
              <NavLink to="/" activeClassName="active">
                <Heading as="h6" className="!font-inriasans !text-black-900_7f">
                  Home
                </Heading>
              </NavLink>
            </li>
            <li>
              <NavLink to="/products" activeClassName="active">
                <Heading as="h6" className="!font-inriasans !text-black-900_7f">
                  Products
                </Heading>
              </NavLink>
            </li>
            <li>
              <NavLink to="/customers" activeClassName="active">
                <Heading as="h6" className="!font-inriasans !text-black-900_7f">
                  Customers
                </Heading>
              </NavLink>
            </li>
            <li>
              <NavLink to="/aboutus" activeClassName="active">
                <Heading as="h6" className="!font-inriasans !text-black-900_7f">
                  About Us
                </Heading>
              </NavLink>
            </li>
          </ul>
          <NavLink to="/register" activeClassName="active">
            <Button
              color="black_900"
              size="sm"
              shape="round"
              className="min-w-[80px] font-inriasans font-bold"
            >
              Register
            </Button>
          </NavLink>
        </div>
      </div>
    </header>
  );
}
