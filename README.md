![[banner.png]]

# About crtsh-it
___
Crtsh-it is a subdomain enumeration tool that makes a call to crt.sh, which is a website that hosts a database of certificate that have been logged by certificate transparency. The tool will scrape all available URLs that are discovered and output them in a convenient format. This tool can also optionally resolve each of the URLs to find out which domains are active. 

It's pronounced "search it".

# Setup
___
### Step 1: Install Python 3
```bash
apt install python3 python3-pip
```

### Step 2: Clone the repository
```bash
git clone <repo>
```

### Step 3: Move to the correct directory
```bash
cd <path>
```

### Step 4: Install requirements
```bash
python3 pip install -r requirements.txt
```


# Using crtsh-it
___

```
usage: crtsh-it.py [-h] -d DOMAIN [-r] [-v] [-q]
```

| Short | Long      | Description                                   |
| ----- | --------- | --------------------------------------------- |
| -h    | --help    | Displays usage information.                   |
| -d    | --domain  | Domain name to be targeted.                   |
| -r    | --resolve | Resolves each discovered subdomain.           |
| -v    | --verbose | Gives more detailed information about errors. |
| -q    | --quiet   | Outputs less text to the terminal.            |

### Example
```bash 
$ python3 crtsh-it.py -d example.com -r 
```

# License
___

# Credits
___
- [A3h1nt](https://github.com/A3h1nt) for developing Subcert, the inspiration for this script.
