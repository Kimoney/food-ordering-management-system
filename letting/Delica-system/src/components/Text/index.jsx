import React from "react";

const sizes = {
  xs: "text-xs font-normal",
  lg: "text-2xl font-normal md:text-[22px]",
  s: "text-base font-normal",
  md: "text-xl font-normal",
};

const Text = ({ children, className = "", as, size = "s", ...restProps }) => {
  const Component = as || "p";

  return (
    <Component className={`text-blue_gray-300_7f font-inriasans ${className} ${sizes[size]}`} {...restProps}>
      {children}
    </Component>
  );
};

export { Text };
