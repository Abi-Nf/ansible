# ansible

Automate apache2 server with Ansible

## Configuration

First create a file with all domains you want like this example.
Create a file like **`domains.config`** and write something like this in

NB : your config should be : [`domain`] [`directory`] [`port`]
And your apache site directory will be like /var/www/[file config name (ike `domains` in this example)]

```makefile
www.example.org /tmp/example.html 4000
www.test.com /tmp/test.html 4500
www.google.com /tmp/google.html 2000
web.facebook.com /tmp/facebook.html 3000
```

Then, execute the command below to start configuration

```sh
# automate [File] 
# So, the file is : domains.config

automate domains.config
```

To make sure the configuration is done successfuly, the final message is : **Configuration done !**
