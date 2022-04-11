#!/bin/sh

docker run -it --rm -v /$(pwd)/config:/etc/ssh/ssh_config -v /$(pwd):/data lagacy-ssh-client bash
