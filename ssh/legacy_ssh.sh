#!/bin/sh

docker build -t lagacy-ssh-client .

docker run -it --rm -v /$(pwd)/config:/etc/ssh/ssh_config -v /$(pwd):/data lagacy-ssh-client bash
