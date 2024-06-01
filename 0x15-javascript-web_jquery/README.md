# JavaScript and jQuery Web Tasks

This repository contains a series of JavaScript and jQuery tasks designed to manipulate HTML elements. Each task must be completed and tested with the provided HTML files.

## Table of Contents
1. [No jQuery](#no-jquery)
2. [With jQuery](#with-jquery)
3. [Click and Turn Red](#click-and-turn-red)
4. [Add `.red` Class](#add-red-class)
5. [Toggle Classes](#toggle-classes)
6. [List of Elements](#list-of-elements)
7. [Change the Text](#change-the-text)
8. [Star Wars Character](#star-wars-character)
9. [Star Wars Movies](#star-wars-movies)
10. [Say Hello!](#say-hello)

## Tasks

### No jQuery
**Objective:** Update the text color of the `<header>` element to red (#FF0000) using pure JavaScript.

- **File:** `0-script.js`
- **HTML to test:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Holberton School</title>
</head>
<body>
  <header>First HTML page</header>
  <footer>Holberton School - 2017</footer>
  <script type="text/javascript" src="0-script.js"></script>
</body>
</html>
```

### With jQuery
**Objective:** Update the text color of the `<header>` element to red (#FF0000) using jQuery.

- **File:** `1-script.js`
- **HTML to test:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Holberton School</title>
  <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
<body>
  <header>First HTML page</header>
  <footer>Holberton School - 2017</footer>
  <script type="text/javascript" src="1-script.js"></script>
</body>
</html>
```

### Click and Turn Red
**Objective:** Update the text color of the `<header>` element to red (#FF0000) when the user clicks on the tag `DIV#red_header`.

- **File:** `2-script.js`
- **HTML to test:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Holberton School</title>
  <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
<body>
  <header>First HTML page</header>
  <div id="red_header">Red header</div>
  <footer>Holberton School - 2017</footer>
  <script type="text/javascript" src="2-script.js"></script>
</body>
</html>
```

### Add `.red` Class
**Objective:** Add the class `red` to the `<header>` element when the user clicks on the tag `DIV#red_header`.

- **File:** `3-script.js`
- **HTML to test:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Holberton School</title>
  <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  <style>
    .red { color: #FF0000; }
  </style>
</head>
<body>
  <header>First HTML page</header>
  <div id="red_header">Red header</div>
  <footer>Holberton School - 2017</footer>
  <script type="text/javascript" src="3-script.js"></script>
</body>
</html>
```

### Toggle Classes
**Objective:** Toggle the class of the `<header>` element between `red` and `green` when the user clicks on the tag `DIV#toggle_header`.

- **File:** `4-script.js`
- **HTML to test:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Holberton School</title>
  <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  <style>
    .red { color: #FF0000; }
    .green { color: #00FF00; }
  </style>
</head>
<body>
  <header class="green">First HTML page</header>
  <div id="toggle_header">Toggle header</div>
  <footer>Holberton School - 2017</footer>
  <script type="text/javascript" src="4-script.js"></script>
</body>
</html>
```

### List of Elements
**Objective:** Add a `<li>` element to a list when the user clicks on the tag `DIV#add_item`.

- **File:** `5-script.js`
- **HTML to test:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Holberton School</title>
  <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
<body>
  <header>First HTML page</header>
  <br />
  <div id="add_item">Add item</div>
  <br />
  <ul class="my_list">
    <li>Item</li>
  </ul>
  <footer>Holberton School - 2017</footer>
  <script type="text/javascript" src="5-script.js"></script>
</body>
</html>
```

### Change the Text
**Objective:** Update the text of the `<header>` element to "New Header!!!" when the user clicks on `DIV#update_header`.

- **File:** `6-script.js`
- **HTML to test:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Holberton School</title>
  <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
<body>
  <header>First HTML page</header>
  <br />
  <div id="update_header">Update the header</div>
  <br />
  <footer>Holberton School - 2017</footer>
  <script type="text/javascript" src="6-script.js"></script>
</body>
</html>
```

### Star Wars Character
**Objective:** Fetch the character name from the URL `https://swapi-api.alx-tools.com/api/people/5/?format=json` and display it in the HTML tag `DIV#character`.

- **File:** `7-script.js`
- **HTML to test:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Holberton School</title>
  <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
<body>
  <header>Star Wars character</header>
  <br />
  <div id="character"></div>
  <br />
  <footer>Holberton School - 2017</footer>
  <script type="text/javascript" src="7-script.js"></script>
</body>
</html>
```

### Star Wars Movies
**Objective:** Fetch and list the titles of all movies from the URL `https://swapi-api.alx-tools.com/api/films/?format=json` in the HTML tag `UL#list_movies`.

- **File:** `8-script.js`
- **HTML to test:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Holberton School</title>
  <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
<body>
  <header>Star Wars movies</header>
  <br />
  <ul id="list_movies"></ul>
  <br />
  <footer>Holberton School - 2017</footer>
  <script type="text/javascript" src="8-script.js"></script>
</body>
</html>
```

### Say Hello!
**Objective:** Fetch the translation of "hello" from `https://hellosalut.stefanbohacek.dev/?lang=fr` and display it in the HTML tag `DIV#hello`.

- **File:** `9-script.js`
- **HTML to test:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Holberton School</title>
  <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  <script type="text/javascript" src="9-script.js"></script>
</head>
<body>
  <header>Say Hello!</header>
  <br />
  <div id="hello"></div>
  <br />
  <footer>Holberton School - 2017</footer>
</body>
</html>
```

## Repository Structure
- **GitHub repository:** `alx-higher_level_programming`
- **Directory:** `0x15-javascript-web_jquery`

