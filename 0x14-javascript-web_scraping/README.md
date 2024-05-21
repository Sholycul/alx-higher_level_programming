# JavaScript Web Scraping

This repository contains a set of JavaScript scripts for various web scraping and file manipulation tasks. Each script demonstrates different functionalities using modules like `fs` for file operations and `request` for HTTP requests. Below are the tasks and instructions on how to use each script.

## Tasks

### 0. Readme

**Script**: `0-readme.js`

**Description**: Reads and prints the content of a file.

**Usage**:
```bash
node 0-readme.js <file path>
```

**Example**:
```bash
$ cat cisfun
C is super fun!
$ node 0-readme.js cisfun
C is super fun!
$ node 0-readme.js doesntexist
{ Error: ENOENT: no such file or directory, open 'doesntexist'
    at Error (native)
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist' }
```

### 1. Write me

**Script**: `1-writeme.js`

**Description**: Writes a string to a file.

**Usage**:
```bash
node 1-writeme.js <file path> <string to write>
```

**Example**:
```bash
$ node 1-writeme.js my_file.txt "Python is cool"
$ cat my_file.txt
Python is cool
```

### 2. Status code

**Script**: `2-statuscode.js`

**Description**: Displays the status code of a GET request.

**Usage**:
```bash
node 2-statuscode.js <URL>
```

**Example**:
```bash
$ node 2-statuscode.js https://alx-intranet.hbtn.io/status
code: 200
$ node 2-statuscode.js https://alx-intranet.hbtn.io/doesnt_exist
code: 404
```

### 3. Star wars movie title

**Script**: `3-starwars_title.js`

**Description**: Prints the title of a Star Wars movie where the episode number matches a given integer.

**Usage**:
```bash
node 3-starwars_title.js <movie ID>
```

**Example**:
```bash
$ node 3-starwars_title.js 1
A New Hope
$ node 3-starwars_title.js 5
Attack of the Clones
```

### 4. Star wars Wedge Antilles

**Script**: `4-starwars_count.js`

**Description**: Prints the number of movies where the character "Wedge Antilles" is present.

**Usage**:
```bash
node 4-starwars_count.js <API URL>
```

**Example**:
```bash
$ node 4-starwars_count.js https://swapi-api.alx-tools.com/api/films
3
```

### 5. Loripsum

**Script**: `5-request_store.js`

**Description**: Gets the contents of a webpage and stores it in a file.

**Usage**:
```bash
node 5-request_store.js <URL> <file path>
```

**Example**:
```bash
$ node 5-request_store.js http://loripsum.net/api loripsum
$ cat loripsum
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit...</p>
```

### 6. How many completed?

**Script**: `6-completed_tasks.js`

**Description**: Computes the number of tasks completed by user ID.

**Usage**:
```bash
node 6-completed_tasks.js <API URL>
```

**Example**:
```bash
$ node 6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
{ '1': 11, '2': 8, '3': 7, '4': 6, '5': 12, '6': 6, '7': 9, '8': 11, '9': 8, '10': 12 }
```

## Repository Structure

```
alx-higher_level_programming/
└── 0x14-javascript-web_scraping/
    ├── 0-readme.js
    ├── 1-writeme.js
    ├── 2-statuscode.js
    ├── 3-starwars_title.js
    ├── 4-starwars_count.js
    ├── 5-request_store.js
    └── 6-completed_tasks.js
```

## Dependencies

- [Node.js](https://nodejs.org/)
- [request](https://www.npmjs.com/package/request) module (Install using `npm install request`)

## Author

This repository is maintained by [Shola](https://github.com/Sholycul).
