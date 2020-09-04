var getChildren = require("./childscript");

module.exports = {
  title: "Full Stack Development with Python and Flask in 2020",
  description: "The complete course notes and guide.",
  themeConfig: {
    nav: [
      { text: "Home", link: "/" },
      {
        text: "Get the course",
        link:
          "https://www.udemy.com/course/complete-python-postgresql-database-course/?referralCode=B3ED9B12EBC114C0C306",
      },
    ],
    sidebar: [
      {
        title: "Start here",
        path: "/",
      },
      {
        title: "Section 1: Welcome to the Course",
        path: "/section01/",
        children: getChildren("section01", "lectures"),
      },
      {
        title: "Section 2: Python Refresher",
        path: "/section02/",
      },
      {
        title: "Section 3: Website Basics",
        path: "/section03/",
        children: getChildren("section03", "lectures"),
      },
      {
        title: "Section 4: Page Structure with HTML",
        path: "/section04/",
        children: getChildren("section04", "lectures"),
      },
      {
        title: "Section 5: Page Style with CSS",
        path: "/section05/",
        children: getChildren("section05", "lectures"),
      },
      {
        title: "Section 6: Project 1: Micro Blog (design+site)",
        path: "/section06/",
        children: getChildren("section06", "lectures"),
      },
      {
        title: "Section 7: Introduction to Flask and MongoDB",
        path: "/section07/",
        children: getChildren("section07", "lectures"),
      },
    ],
    sidebarDepth: 0,
  },
  markdown: {
    extendMarkdown: (md) => {
      md.use(require("markdown-it-footnote"));
    },
  },
};
