#siftx

siftx is a lightweight grep like command-line tools for searching and filtering text files.

It is designed to be simple, fast, and easy to extend.

##installation

```bash
pip install siftx

#usage
siftx [search:text] [path] [options]

#options

-n Show line numbers
-i Ignore_case (Case insensitive search)
-v Invert search
-c Count matching lines

#Examples
siftx search:error text.txt
siftx -n search:error text.txt
siftx -i search:error text.txt
siftx -v search:error text.txt
siftx -c search:error text.txt

#Status
This is the first public release (v0.1.0). More features will be added in the future version