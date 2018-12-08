# lonstart

## Preamble

This code was not written by me. A github user by the handle of "nerdvsgeek"
wrote it, or at least packaged it and put together these instructions.  I was
fortunate enough to have cloned his repo and got Legacy of Norrath working.

For whatever reasons, he deleted his repo, quit the LoN server, and as far as I
know is no longer playing.  I'm moving his code with minor enhancements to my
own repo so it doesn't get lost. 

With that said, here it is.

## Original Readme 

Follows is `nerdvsgeek`'s original readme, more or less without modification,
except for a few minor markdown enhancements.

---

Legacy of Norrath (EQ Emu Server) game client startup script for Linux.

Quick Notes for configuring on Ubuntu 18.04. Other distributions may need to be adapted.

1. Add the i386 architecture to Ubuntu Linux

`sudo dpkg --add-architecture i386`


2. Install necessary software

`sudo apt install steam wine32 cabextract p7zip-rar p7zip-full`


3. Get the current winetricks script

```
sudo wget -O /usr/local/bin/winetricks https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks
sudo chmod +x /usr/local/bin/winetricks
```


4. Download Wine Gecko (embedded browser) from:

```
cd ~/Downloads
wget http://dl.winehq.org/wine/wine-gecko/2.47/wine_gecko-2.47-x86.msi
```


5. Set environment variables

```
WINEARCH="win32"
WINEPREFIX="${HOME}/.local/${WINEARCH}/lon"
export WINEARCH WINEPREFIX

mkdir -p $WINEPREFIX
mkdir -p $WINEPREFIX/drive_c/lon

echo $WINEARCH
wineboot
```

```
wine msiexec /i ~/Downloads/wine_gecko-2.47-x86.msi
wineboot
```

```
winetricks win7
winetricks d3dx9 d3dx9_30 d3dx9_43 corefonts
winetricks dotnet45
wineboot
```

```
xdg-open $WINEPREFIX/drive_c/lon
```


6. Copy `loginproxy.py` into the lon directory we just opened in the file manager.

7. Copy the LoNClient folder from the extracted LoNClient.rar into the lon directory.

8. Copy the lonpatcher.exe into the LoNClient directory.

9. Copy the eqhost.txt.proxy into the LoNClient directory.

10. Copy the lon script into your path - ${HOME}/.local/bin may exist and be in your path depending on your distribution.

Run the game with the lon script - it will start and stop the loginproxy.
