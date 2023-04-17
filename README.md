# plain text accounting shared expenses based on hledger POC

This project is in work in progress.  

Repository starting point issue (in French): https://github.com/stephane-klein/backlog/issues/193

Install https://hledger.org/:

```
$ mkdir bin/
$ cd bin
$ curl -LOC- https://github.com/simonmichael/hledger/releases/download/1.29.2/hledger-linux-x64.zip   # can rerun if interrupted
$ unzip hledger-linux-x64.zip; tar xvf hledger-linux-x64.tar; rm hledger-linux-x64.{zip,tar}        # github workaround, preserves permissions
$ cd -
$ hledger --version  # should show the new version
hledger 1.29.2, linux-x86_64
```

```
$ hledger check
```

```
$ hledger web
```

Go to http://127.0.0.1:5000/journal


```sh
$ pip install -r requirements.txt
```

Edit `main.journal.j2` and then execute:

```
$ ./preprocess.py > main.journal
```
