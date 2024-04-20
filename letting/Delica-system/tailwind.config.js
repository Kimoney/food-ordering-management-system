module.exports = {
  mode: "jit",
  content: ["./src/**/**/*.{js,ts,jsx,tsx,html,mdx}", "./src/**/*.{js,ts,jsx,tsx,html,mdx}"],
  darkMode: "class",
  theme: {
    screens: { md: { max: "1050px" }, sm: { max: "550px" } },
    extend: {
      colors: {
        white: { A700: "#ffffff" },
        deep_orange: { 600: "#f24e1e" },
        blue_gray: { 100: "#d2cdcd", 300: "#98a2b3", 900: "#343434", "300_7f": "#98a2b37f" },
        black: { 900: "#000000", "900_7f": "#0000007f", "900_bf": "#000000bf" },
        gray: {
          100: "#f2f2f2",
          300: "#e0e0e0",
          500: "#9e9e9e",
          700: "#696969",
          800: "#424242",
          900: "#1e1e1e",
          "900_03": "#101828",
          "900_02": "#0f1728",
          "900_01": "#141414",
        },
        red: { 600: "#f52020" },
      },
      boxShadow: { xs: "5px 5px 5px 0px #0000003f", sm: "4px 4px 5px 0px #0000003f" },
      fontFamily: { inter: "Inter", inriasans: "Inria Sans", montserrat: "Montserrat" },
      backgroundImage: { gradient: "radial-gradient(350deg, #ffd684,#e73315)" },
    },
  },
  plugins: [require("@tailwindcss/forms")],
};
