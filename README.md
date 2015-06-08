## dockermaster version 15.6.8
```
dockermaster version 15.6.8
Usage: dockermaster COMMAND [OPTIONS]
AVAILABLE COMMANDS AND OPTIONS:
run            Create and run containers
 -n <n>        Number of nodes (default: 1)
 -h <hostname> Base hostname (default: node)
 -d <domain>   Domain (default: localdomain)
stop [<node>]  Stop containers, all if none supplied
start [<node>] Start containers, all if none supplied
rm [<node>]    Remove containers, all if none supplied
list           Print list of containers
help           Print this help summary page
version        Print version number
EXAMPLES:
Start single container centos-server.test.wandisco.com:
  dockermaster run -h centos-server -d test.wandisco.com
Start 5 containers vm1, vm2... vm5 using image wandisco/centos:latest:
  dockermaster run -n 5 -h vm -i wandisco/centos:latest
Stop container called node12:
  dockermaster stop node12
Remove all containers:
  dockermaster rm
```
