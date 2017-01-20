

Example usage as a CLI:
```python3 download_ftp_tree ftp.something.com /some/directory .```
The code above will look for a directory called /some/directory/ on the ftp
host, and then duplicate the directory and its entire contents into the local
current working directory.

Additional options are available for authentication and more. See help:
```python3 download_ftp_tree -h```