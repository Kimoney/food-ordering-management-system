import React from "react";

const sizes = {
  "3xl": "text-[40px] font-semibold md:text-[38px] sm:text-4xl",
  "2xl": "text-4xl font-extrabold md:text-[34px] sm:text-[32px]",
  xl: "text-[32px] font-bold md:text-3xl sm:text-[28px]",
  "4xl": "text-[64px] font-bold md:text-5xl",
  s: "text-base font-bold",
  md: "text-xl font-bold",
  xs: "text-sm font-bold",
  lg: "text-2xl font-bold md:text-[22px]",
};

const Heading = ({ children, className = "", size = "s", as, ...restProps }) => {
  const Component = as || "h6";

  return (
    <Component className={`text-black-900 font-inter ${className} ${sizes[size]}`} {...restProps}>
      {children}
    </Component>
  );
};

export { Heading };
