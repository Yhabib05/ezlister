# EzLister

EzLister is a powerful and easy-to-use tool designed for listing directories and subdomains of a given domain. It's ideal for security researchers, web developers, and anyone interested in web reconnaissance.

I tried to make a two in one lister for an easy use for pentesting and monitoring, as they both work the same so why not combine them together.
This is just a first version of the lister, as I was just trying to learn how they work and trying to combine them in one, but more improvements are coming for sure in the future, so stay tuned.

## Features

- Directory listing: Quickly find accessible directories on a web server.
- Subdomain enumeration: Discover subdomains associated with the target domain.
- Flexible wordlists: Choose from different wordlists for targeted scanning.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

EzLister is built with Python and requires Python 3.6 or later. Ensure you have Python installed on your system. You can check your Python version by running:

```bash
python3 --version
```


### Installation
#### Clone the repository

To get started with EzLister, first clone the repository to your local machine:

```bash
git clone https://github.com/yhabib05/ezlister.git
cd ezlister
``` 

#### Install dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

#### Install EzLister

Finally, install EzLister itself. For a regular installation:

```bash
pip install .
```

## Usage

With EzLister installed, you can start using it to list directories and subdomains for a given domain. Here are the basic commands:
Basic Command Structure

```bash
ezlister [domain] [options]
```

Replace [domain] with the target domain you want to scan.
**Options:**

    -d: Use the directory lister feature.
    -s: Use the subdomain lister feature.
    -o [filename]: Output the results to a specified file. Replace [filename] with the name of your output file.

**Examples:**

To list directories for example.com:

```bash
ezlister example.com -d
```

To enumerate subdomains for example.com:

```bash
ezlister example.com -s
```

To save subdomain enumeration results of **example.com** into **results.txt**:

```bash
ezlister example.com -s -o results.txt
```

## Updating EzLister

To ensure you're using the latest version of EzLister, you can update your local repository and reinstall the tool:

```bash
git pull origin main
pip install -e .
```

## Future improvements
If I have some time, I will add a new option -q to just use the shortest wordlists and scan the domain in question for both subdomains and directories.