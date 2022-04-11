# File structure on the luxtronik controller

Note: `/proc` and `/sys` are note listed

```
.
├── bin
│   ├── addgroup
│   ├── adduser
│   ├── ash
│   ├── busybox
│   ├── cat
│   ├── catv
│   ├── chattr
│   ├── chgrp
│   ├── chmod
│   ├── chown
│   ├── cp
│   ├── cpio
│   ├── cttyhack
│   ├── date
│   ├── dbclient
│   ├── dd
│   ├── delgroup
│   ├── deluser
│   ├── df
│   ├── dmesg
│   ├── dnsdomainname
│   ├── dropbearconvert
│   ├── dropbearkey
│   ├── dumpkmap
│   ├── echo
│   ├── ed
│   ├── egrep
│   ├── false
│   ├── fdflush
│   ├── fgrep
│   ├── fsync
│   ├── getopt
│   ├── grep
│   ├── gunzip
│   ├── gzip
│   ├── hostname
│   ├── hush
│   ├── ionice
│   ├── ip
│   ├── ipaddr
│   ├── ipcalc
│   ├── iplink
│   ├── iproute
│   ├── iprule
│   ├── iptunnel
│   ├── kill
│   ├── linux32
│   ├── linux64
│   ├── ln
│   ├── login
│   ├── ls
│   ├── lsattr
│   ├── lzop
│   ├── makemime
│   ├── mkdir
│   ├── mknod
│   ├── mktemp
│   ├── more
│   ├── mount
│   ├── mountpoint
│   ├── msh
│   ├── mt
│   ├── mv
│   ├── netstat
│   ├── nice
│   ├── pidof
│   ├── ping
│   ├── ping6
│   ├── pipe_progress
│   ├── printenv
│   ├── ps
│   ├── pwd
│   ├── reformime
│   ├── rm
│   ├── rmdir
│   ├── rpm
│   ├── run-parts
│   ├── scp
│   ├── scriptreplay
│   ├── sed
│   ├── setarch
│   ├── sh
│   ├── sleep
│   ├── stat
│   ├── stty
│   ├── su
│   ├── sync
│   ├── tar
│   ├── touch
│   ├── true
│   ├── umount
│   ├── uname
│   ├── uncompress
│   ├── usleep
│   ├── vi
│   ├── watch
│   └── zcat
├── config
├── dev
│   ├── aijog
│   ├── ailcd
│   ├── ailed
│   ├── bootreg
│   ├── console
│   ├── cpu_dma_latency
│   ├── device
│   ├── full
│   ├── kmem
│   ├── kmsg
│   ├── loop0
│   ├── loop1
│   ├── loop2
│   ├── loop3
│   ├── loop4
│   ├── loop5
│   ├── loop6
│   ├── loop7
│   ├── mem
│   ├── mice
│   ├── mtd0
│   ├── mtd0ro
│   ├── mtdblock0
│   ├── network_latency
│   ├── network_throughput
│   ├── null
│   ├── ptmx
│   ├── ptyp0
│   ├── ptyp1
│   ├── ptyp2
│   ├── ptyp3
│   ├── ram0
│   ├── ram1
│   ├── ram2
│   ├── ram3
│   ├── random
│   ├── rtc0
│   ├── tty
│   ├── tty0
│   ├── tty1
│   ├── tty10
│   ├── tty11
│   ├── tty12
│   ├── tty13
│   ├── tty14
│   ├── tty15
│   ├── tty16
│   ├── tty17
│   ├── tty18
│   ├── tty19
│   ├── tty2
│   ├── tty20
│   ├── tty21
│   ├── tty22
│   ├── tty23
│   ├── tty24
│   ├── tty25
│   ├── tty26
│   ├── tty27
│   ├── tty28
│   ├── tty29
│   ├── tty3
│   ├── tty30
│   ├── tty31
│   ├── tty32
│   ├── tty33
│   ├── tty34
│   ├── tty35
│   ├── tty36
│   ├── tty37
│   ├── tty38
│   ├── tty39
│   ├── tty4
│   ├── tty40
│   ├── tty41
│   ├── tty42
│   ├── tty43
│   ├── tty44
│   ├── tty45
│   ├── tty46
│   ├── tty47
│   ├── tty48
│   ├── tty49
│   ├── tty5
│   ├── tty50
│   ├── tty51
│   ├── tty52
│   ├── tty53
│   ├── tty54
│   ├── tty55
│   ├── tty56
│   ├── tty57
│   ├── tty58
│   ├── tty59
│   ├── tty6
│   ├── tty60
│   ├── tty61
│   ├── tty62
│   ├── tty63
│   ├── tty7
│   ├── tty8
│   ├── tty9
│   ├── ttyp0
│   ├── ttyp1
│   ├── ttyp2
│   ├── ttyp3
│   ├── ttyS0
│   ├── ttyS2
│   ├── ttyS3
│   ├── ttyS4
│   ├── ubi0
│   ├── ubi0_0
│   ├── ubi0_1
│   ├── ubi0_2
│   ├── ubi0_3
│   ├── ubi0_4
│   ├── ubi0_5
│   ├── ubi_ctrl
│   ├── urandom
│   ├── vcs
│   ├── vcs1
│   ├── vcsa
│   ├── vcsa1
│   ├── watchdog
│   └── zero
├── etc
│   ├── bootmgr.cfg
│   ├── dropbear
│   │   ├── dropbear_dss_host_key
│   │   └── dropbear_rsa_host_key
│   ├── fstab
│   ├── inetd.conf
│   ├── init.d
│   │   └── rcS
│   ├── inittab
│   ├── localtime
│   ├── mdev.conf
│   ├── passwd
│   ├── resolv.conf
│   ├── rpc
│   ├── shadow
│   └── udhcpd.conf
├── home
│   ├── 10Min_1
│   ├── 10Min_2
│   ├── appl
│   ├── appl.cfg
│   ├── appl_param
│   ├── appl_param1
│   ├── appl_param2
│   ├── ASB.bin
│   ├── ASB_BL_Switch.bin
│   ├── ASB_bootloader.bin
│   ├── ASB.hex
│   ├── bootloader.lin
│   ├── Defines.txt
│   ├── errlog
│   ├── firmware
│   ├── HZIO.lin
│   ├── IBN.lar
│   ├── index.html
│   ├── lang_CR
│   ├── lang_cz
│   ├── lang_dan
│   ├── lang_de
│   ├── lang_ee
│   ├── lang_en
│   ├── lang_es
│   ├── lang_fr
│   ├── lang_hr
│   ├── lang_it
│   ├── lang_lt
│   ├── lang_lv
│   ├── lang_mag
│   ├── lang_ned
│   ├── lang_nor
│   ├── lang_p
│   ├── lang_pol
│   ├── lang_ro
│   ├── lang_slo
│   ├── lang_suo
│   ├── lang_sve
│   ├── lang_tr
│   ├── LD2AG.lin
│   ├── LWD45.lin
│   ├── LWD90.lin
│   ├── LWD.lin
│   ├── LWDRev.lin
│   ├── MaxIO.conf
│   ├── MSW_15.lin
│   ├── MSW_Inverter.lin
│   ├── MSW.lin
│   ├── NewProc
│   ├── ParamArchive_1648425600
│   ├── ParamArchive_1649030400
│   ├── ParamArchive_1649116800
│   ├── ParamArchive_1649203200
│   ├── ParamArchive_1649289600
│   ├── ParamArchive_1649376000
│   ├── ParamArchive_1649462400
│   ├── ParamArchive_1649548800
│   ├── ParamArchive_1649635200
│   ├── proclog
│   ├── SEC.bin
│   ├── share
│   │   ├── localtime
│   │   ├── passwd
│   │   └── shadow
│   ├── SWPH291.lin
│   ├── SWPH.lin
│   ├── SWP.lin
│   ├── timezone
│   ├── udhcpc.script
│   ├── Webserver
│   │   ├── base.css
│   │   ├── base.jpg
│   │   ├── index.html
│   │   ├── jquery.js
│   │   ├── Lux.js
│   │   ├── LuxSim.jpg
│   │   └── saveIcon.png
│   ├── Werte.IBN
│   └── wp.jar
├── lib
│   ├── ld-2.8.so
│   ├── ld-linux.so.3
│   ├── libanl-2.8.so
│   ├── libanl.so.1
│   ├── libBrokenLocale-2.8.so
│   ├── libBrokenLocale.so.1
│   ├── libc-2.8.so
│   ├── libcidn-2.8.so
│   ├── libcidn.so.1
│   ├── libcrypt-2.8.so
│   ├── libcrypt.so.1
│   ├── libc.so.6
│   ├── libdl-2.8.so
│   ├── libdl.so.2
│   ├── libgcc_s.so
│   ├── libgcc_s.so.1
│   ├── libm-2.8.so
│   ├── libmemusage.so
│   ├── libm.so.6
│   ├── libnsl-2.8.so
│   ├── libnsl.so.1
│   ├── libnss_compat-2.8.so
│   ├── libnss_compat.so.2
│   ├── libnss_dns-2.8.so
│   ├── libnss_dns.so.2
│   ├── libnss_files-2.8.so
│   ├── libnss_files.so.2
│   ├── libnss_hesiod-2.8.so
│   ├── libnss_hesiod.so.2
│   ├── libnss_nis-2.8.so
│   ├── libnss_nisplus-2.8.so
│   ├── libnss_nisplus.so.2
│   ├── libnss_nis.so.2
│   ├── libpcprofile.so
│   ├── libpthread-2.8.so
│   ├── libpthread.so.0
│   ├── libresolv-2.8.so
│   ├── libresolv.so.2
│   ├── librt-2.8.so
│   ├── librt.so.1
│   ├── libSegFault.so
│   ├── libstdc++.so
│   ├── libstdc++.so.6
│   ├── libstdc++.so.6.0.10
│   ├── libthread_db-1.0.so
│   ├── libthread_db.so.1
│   ├── libutil-2.8.so
│   ├── libutil.so.1
│   ├── libz.so
│   ├── libz.so.1
│   └── libz.so.1.2.5
├── linuxrc
├── media
├── mnt
│   ├── nfs
│   └── usb
├── opt
├── root
├── sbin
│   ├── acpid
│   ├── adjtimex
│   ├── arp
│   ├── blkid
│   ├── depmod
│   ├── devmem
│   ├── dropbear
│   ├── fbsplash
│   ├── fdisk
│   ├── findfs
│   ├── freeramdisk
│   ├── fsck
│   ├── fsck.minix
│   ├── getty
│   ├── halt
│   ├── hdparm
│   ├── hwclock
│   ├── ifconfig
│   ├── ifdown
│   ├── ifenslave
│   ├── ifup
│   ├── init
│   ├── inotifyd
│   ├── insmod
│   ├── klogd
│   ├── ldconfig
│   ├── loadkmap
│   ├── logread
│   ├── losetup
│   ├── lsmod
│   ├── lspci
│   ├── lsusb
│   ├── makedevs
│   ├── man
│   ├── mdev
│   ├── mkdosfs
│   ├── mke2fs
│   ├── mkfs.ext2
│   ├── mkfs.minix
│   ├── mkfs.vfat
│   ├── mkswap
│   ├── modprobe
│   ├── nameif
│   ├── pivot_root
│   ├── poweroff
│   ├── raidautorun
│   ├── reboot
│   ├── rmmod
│   ├── route
│   ├── runlevel
│   ├── setconsole
│   ├── slattach
│   ├── sln
│   ├── start-stop-daemon
│   ├── sulogin
│   ├── swapoff
│   ├── swapon
│   ├── switch_root
│   ├── sysctl
│   ├── syslogd
│   ├── tunctl
│   ├── tune2fs
│   ├── udhcpc
│   ├── vconfig
│   ├── watchdog
│   └── zcip
├── srv
├── tmp
├── usr
│   ├── bin
│   │   ├── [
│   │   ├── [[
│   │   ├── ar
│   │   ├── arping
│   │   ├── awk
│   │   ├── basename
│   │   ├── beep
│   │   ├── bunzip2
│   │   ├── bzcat
│   │   ├── bzip2
│   │   ├── cal
│   │   ├── catchsegv
│   │   ├── chat
│   │   ├── chpst
│   │   ├── chrt
│   │   ├── chvt
│   │   ├── cksum
│   │   ├── clear
│   │   ├── cmp
│   │   ├── comm
│   │   ├── crontab
│   │   ├── cryptpw
│   │   ├── cut
│   │   ├── dc
│   │   ├── deallocvt
│   │   ├── diff
│   │   ├── dirname
│   │   ├── dos2unix
│   │   ├── dpkg
│   │   ├── du
│   │   ├── dumpleases
│   │   ├── eject
│   │   ├── env
│   │   ├── envdir
│   │   ├── envuidgid
│   │   ├── ether-wake
│   │   ├── expand
│   │   ├── expr
│   │   ├── fdformat
│   │   ├── find
│   │   ├── fold
│   │   ├── free
│   │   ├── ftpget
│   │   ├── ftpput
│   │   ├── fuser
│   │   ├── gdbserver
│   │   ├── gencat
│   │   ├── getconf
│   │   ├── getent
│   │   ├── hd
│   │   ├── head
│   │   ├── hexdump
│   │   ├── hostid
│   │   ├── iconv
│   │   ├── id
│   │   ├── ifplugd
│   │   ├── install
│   │   ├── ipcrm
│   │   ├── ipcs
│   │   ├── kbd_mode
│   │   ├── killall
│   │   ├── killall5
│   │   ├── last
│   │   ├── ldd
│   │   ├── length
│   │   ├── less
│   │   ├── locale
│   │   ├── localedef
│   │   ├── logger
│   │   ├── logname
│   │   ├── lpq
│   │   ├── lpr
│   │   ├── lzmacat
│   │   ├── lzopcat
│   │   ├── md5sum
│   │   ├── mesg
│   │   ├── microcom
│   │   ├── mkfifo
│   │   ├── mkpasswd
│   │   ├── mtrace
│   │   ├── nc
│   │   ├── nmeter
│   │   ├── nohup
│   │   ├── nslookup
│   │   ├── od
│   │   ├── openvt
│   │   ├── passwd
│   │   ├── patch
│   │   ├── pcprofiledump
│   │   ├── pgrep
│   │   ├── pkill
│   │   ├── printf
│   │   ├── pscan
│   │   ├── readlink
│   │   ├── realpath
│   │   ├── renice
│   │   ├── reset
│   │   ├── resize
│   │   ├── rpcgen
│   │   ├── rpm2cpio
│   │   ├── rtcwake
│   │   ├── runsv
│   │   ├── runsvdir
│   │   ├── rx
│   │   ├── script
│   │   ├── seq
│   │   ├── setkeycodes
│   │   ├── setsid
│   │   ├── setuidgid
│   │   ├── sha1sum
│   │   ├── sha256sum
│   │   ├── sha512sum
│   │   ├── showkey
│   │   ├── softlimit
│   │   ├── sort
│   │   ├── split
│   │   ├── sprof
│   │   ├── strings
│   │   ├── sum
│   │   ├── sv
│   │   ├── tac
│   │   ├── tail
│   │   ├── taskset
│   │   ├── tcpsvd
│   │   ├── tee
│   │   ├── telnet
│   │   ├── test
│   │   ├── tftp
│   │   ├── tftpd
│   │   ├── time
│   │   ├── timeout
│   │   ├── top
│   │   ├── tr
│   │   ├── traceroute
│   │   ├── traceroute6
│   │   ├── tty
│   │   ├── ttysize
│   │   ├── tzselect
│   │   ├── udpsvd
│   │   ├── unexpand
│   │   ├── uniq
│   │   ├── unix2dos
│   │   ├── unlzma
│   │   ├── unlzop
│   │   ├── unzip
│   │   ├── uptime
│   │   ├── uudecode
│   │   ├── uuencode
│   │   ├── vlock
│   │   ├── volname
│   │   ├── wall
│   │   ├── wc
│   │   ├── wget
│   │   ├── which
│   │   ├── who
│   │   ├── whoami
│   │   ├── xargs
│   │   ├── xtrace
│   │   └── yes
│   ├── libexec
│   │   └── getconf
│   ├── sbin
│   │   ├── bootmgr
│   │   ├── brctl
│   │   ├── chpasswd
│   │   ├── chroot
│   │   ├── crond
│   │   ├── dhcprelay
│   │   ├── dnsd
│   │   ├── failsafe
│   │   ├── fakeidentd
│   │   ├── fbset
│   │   ├── flash_erase
│   │   ├── flash_eraseall
│   │   ├── flash_info
│   │   ├── flash_lock
│   │   ├── flash_otp_dump
│   │   ├── flash_otp_info
│   │   ├── flash_unlock
│   │   ├── ftpd
│   │   ├── httpd
│   │   ├── iconvconfig
│   │   ├── inetd
│   │   ├── loadfont
│   │   ├── lpd
│   │   ├── nscd
│   │   ├── ntpd
│   │   ├── popmaildir
│   │   ├── rdate
│   │   ├── rdev
│   │   ├── readprofile
│   │   ├── rpcinfo
│   │   ├── sendmail
│   │   ├── setfont
│   │   ├── setlogcons
│   │   ├── svlogd
│   │   ├── telnetd
│   │   ├── ubiattach
│   │   ├── ubicrc32
│   │   ├── ubicrc32.pl
│   │   ├── ubidetach
│   │   ├── ubiformat
│   │   ├── ubigen
│   │   ├── ubimirror
│   │   ├── ubimkvol
│   │   ├── ubinfo
│   │   ├── ubinize
│   │   ├── ubirmvol
│   │   ├── ubiupdatevol
│   │   ├── udhcpd
│   │   ├── usbmount
│   │   ├── zdump
│   │   └── zic
│   └── share
│       └── zoneinfo
│           └── Europe
│               └── Berlin
└── var
    └── resolv.conf
```

