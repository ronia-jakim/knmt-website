function toggleDarkMode() {
  let docBody = document.body

  let themeIcon = document.getElementById("dark-theme")
  const lightIcon = '/assets/img/light.svg'
  const darkIcon = '/assets/img/moon.svg'

  const dataTheme = docBody.getAttribute("data-theme")

  if (dataTheme === "dark") {
    themeIcon.setAttribute("src", lightIcon)
    
    docBody.setAttribute("data-theme", "light")
  }
  else {
    themeIcon.setAttribute("src", darkIcon)
    
    docBody.setAttribute("data-theme", "dark")
  }
}
