# Snippets and Code Examples

We have various repos full of code to extract complex datasets... but sometimes all you need is a couple of lines of code to grab something important. When someone does something clever and (hopefully) repeatable, we put it here. So, here you go, have fun!

## Harvest videos from a youtube account

Install [youtube-dl](https://github.com/rg3/youtube-dl) (instructions in link, or in Arch Linux `yaourt -S youtube-dl`, doubtless similar in other Linuxes).

Then, in shell:

```sh
youtube-dl -o '%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' -f 'bestvideo[height<=480]+bestaudio/best[height<=480]' --yes-playlist https://www.youtube.com/user/USEPAgov/playlists
```
## 
