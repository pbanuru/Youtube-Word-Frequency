# youtube-word-frequency

Given a YouTube video URL, this script returns the top n words spoken in the video.

Ex.
```
$ cd ~/youtube-word-frequency
$ python3 main.py

Enter the video link: https://www.youtube.com/watch?v=byTxzzztRBU
I want the to see the n most common words: 4
------------------------------------------------
1. | the  | 117
2. |  to  | 110
3. | that | 84
4. |  of  | 83
```

## Why?

This can be used to understand your or someone else's most common words. And you can see how many times you said "um"

This can also be used to compare one aspect of your speech patterns, to those of others; that aspect being word frequency.

For example, you want to see how many times Park Jimin says the word "love you army" in a video.
Then, you can run the script on a video of your own speech, scroll down enough, and compare!

---
### Details
Of course, frequency is relative to the length of the video. A short video of one person will likely have less "{some_word}"s than a longer video.

A requirement being that the video has captions. Youtube usually autogenerates captions for videos, but you have to give it sufficient time after an upload.

---

## Todo:


* Provide Support for playlists and a series of youtube videos.

* Create a GUI to improve the user experience.

## Unattended Error Todos:

* Error Handling for invalid video id

* Error Handling for videos without English Subtitles

* Error Handling for videos with no captions

* Support https://youtu.be/byTxzzztRBU style shortened links (youtu.be)