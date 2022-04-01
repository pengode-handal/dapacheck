# dapacheck
Mass DA PA Checker

# Installation
<details open>
<summary> pydroid / Linux</summary>

- ```bash
  $ apt update && apt upgrade
  ```

- ```bash
  $ apt install python git -y
  ```

- ```bash
  $ git clone https://github.com/pengode-handal/dapacheck
  ```

- ```bash
  $ pip3 install requests
  ```
- ```bash
  $ pip3 install bs4
  ```

# Usage

<p>for help</p>

- ```bash
  $ python3 dapa.py -h/--help
  ```
<p>for scanning the web</p>

- ```bash
  $ python3 dapa.py -d/--domain [the domain]
  Example
  $ python3 dapa.py -d google.com
  ```

<p>for mass scanning</p>

- ```bash
  $ python3 dapa.py -f/--file [the list]
  Example
  $ python3 dapa.py -f list
  ```
