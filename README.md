# ansible

Automate apache2 server with Ansible

## Configuration

First create a file with all domains you want like this example.
Create a file like [**test.config**](./test.config)

Then, execute the command below to start configuration

```sh
# ./automate.sh [File] 
# So, the file is : test.config

./automate.sh test.config
```

> The execution file (index.yaml) may take a long time

To make sure the configuration is done successfuly, the final message is : **Configuration done !**
