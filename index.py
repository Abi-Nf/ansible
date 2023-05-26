from argparse import ArgumentParser as AP

parser = AP(description="Parse the file to config")

parser.add_argument("file", type=str,nargs="+",metavar="str")

args = parser.parse_args().file[0]

file = open(args,"r").read()

lines = file.splitlines()

script = ""

for line in lines:
    split = line.split(" ")
    packet = f"""<virtualHost *:{split[2]}>
    serverAdmin admin@ansible_default.com
    ServerName {split[0]}
    DocumentRoot var/www/{split[0].split(".")[1]}
</virtualHost>
"""
    open(f"/etc/apache2/sites-available/{split[2]}-ansible-default.conf","w").write(packet)
    open(f"/etc/apache2/sites-enabled/{split[2]}-ansible-default.conf","w").write(packet)
    
    get = f"""
    - name: The site index file for {split[0]} to apache configuration
      copy:
        src: {split[1]}
        dest: /var/www/html/{split[0].split(".")[1]}.html
"""
    script+=get




build = f"""
---
- name: configuring Apache server
  hosts: localhost
  tasks:
    - name: Install Apache if not exist
      package:
       name : apache2
       state: present

    - name: Start Apache server
      service:
       name: apache2
       state: started

    {script}

    - name: Restart apache server
      service:
        name: apache2
        state: restarted
"""


open("index.yml","w").write(build)