![alt text](https://raw.githubusercontent.com/whitekr0w/crtsh-it/main/images/banner.png "crtsh-it logo")

# About crtsh-it
Crtsh-it is a subdomain enumeration tool that makes a call to crt.sh, which is a website that hosts a database of certificates that have been logged by certificate transparency. The tool will scrape all available URLs that are discovered and output them in a convenient format. This tool can also optionally resolve each of the URLs to find out which domains are active. 

**It's pronounced "search it". >:(**

# Setup
### Step 1: Install Python 3
```bash
apt install python3 python3-pip
```

### Step 2: Clone the repository
```bash
git clone https://github.com/whitekr0w/crtsh-it.git
```

### Step 3: Move to the correct directory
```bash
cd crtsh-it
```

### Step 4: Install requirements
```bash
python3 pip install -r requirements.txt
```


# Using crtsh-it

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
Crtsh-it is licensed by the GNU General Public License v3.0.

# Credits
- [A3h1nt](https://github.com/A3h1nt) for developing Subcert, the inspiration for this script.
