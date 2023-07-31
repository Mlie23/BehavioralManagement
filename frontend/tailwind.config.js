module.exports = {
  mode: "jit",
  // These paths are just examples, customize them to match your project structure
  purge: ["./public/**/*.html", "./src/**/*.{js,jsx,ts,tsx,vue}"],
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        blue: "#87B3C2", //teagreen (old names)
        champagne: "#F7E4C7", //beige
        cornsilk: "#FAF8EE", // cornsilk
        lightbrown: "#FAEBD5",
        buff: "#E2A07C", // burnt sienna
        brown: "#D0662C", // sienna
        darkblue: "#6CA1B2",
      },
    },
  },
  plugins: [],
};
