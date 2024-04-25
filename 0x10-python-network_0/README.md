# 0x10-Python Networking #0

This repository contains solutions to Python networking tasks provided by ALX Higher Level Programming.

## Task Descriptions and Solutions

### 0. cURL body size

- **Task**: Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response.
  - The size must be displayed in bytes.
  - You have to use `curl`.
  - Please test your script in the sandbox provided, using the web server running on port 5000.

```bash
./0-body_size.sh 0.0.0.0:5000
```

### 1. cURL to the end

- **Task**: Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response.
  - Display only the body of a 200 status code response.
  - You have to use `curl`.
  - Please test your script in the sandbox provided, using the web server running on port 5000.

```bash
./1-body.sh 0.0.0.0:5000/route_1
```

### 2. cURL Method

- **Task**: Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response.
  - You have to use `curl`.
  - Please test your script in the sandbox provided, using the web server running on port 5000.

```bash
./2-delete.sh 0.0.0.0:5000/route_3
```

### 3. cURL only methods

- **Task**: Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.
  - You have to use `curl`.
  - Please test your script in the sandbox provided, using the web server running on port 5000.

```bash
./3-methods.sh 0.0.0.0:5000/route_4
```

### 4. cURL headers

- **Task**: Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response.
  - A header variable `X-School-User-Id` must be sent with the value `98`.
  - You have to use `curl`.
  - Please test your script in the sandbox provided, using the web server running on port 5000.

```bash
./4-header.sh 0.0.0.0:5000/route_5
```

### 5. cURL POST parameters

- **Task**: Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response.
  - A variable `email` must be sent with the value `test@gmail.com`.
  - A variable `subject` must be sent with the value `I will always be here for PLD`.
  - You have to use `curl`.
  - Please test your script in the sandbox provided, using the web server running on port 5000.

```bash
./5-post_params.sh 0.0.0.0:5000/route_6
```

### 6. Find a peak

- **Task**: Write a function that finds a peak in a list of unsorted integers.
  - You are not allowed to import any module.
  - Your algorithm must have the lowest complexity.
  - `6-peak.py` must contain the function.
  - `6-peak.txt` must contain the complexity of your algorithm: O(log(n)), O(n), O(nlog(n)), or O(n^2).
  - Note: there may be more than one peak in the list.

```python
./6-main.py
```

## Repository Information

- **GitHub Repository**: [alx-higher_level_programming](https://github.com/Sholycul/alx-higher_level_programming)
- **Directory**: 0x10-python-network_0
- **Files**:
  - 0-body_size.sh
  - 1-body.sh
  - 2-delete.sh
  - 3-methods.sh
  - 4-header.sh
  - 5-post_params.sh
  - 6-peak.py
  - 6-peak.txt
