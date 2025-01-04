# PhotoFilmStrip Changelog

## 4.0.0b5 (2025-01-04)

### Other changes

**setup.py: Update files to be included in dist files**

[1d542](https://github.com/tsitle/photofilmstrip/commit/1d542db367d1741) tsitle *2025-01-03 10:48:04*


**Add README*.md**

[2356c](https://github.com/tsitle/photofilmstrip/commit/2356cd3d9ecf6cc) tsitle *2025-01-03 10:47:28*


**Update run scripts related stuff**

[94c65](https://github.com/tsitle/photofilmstrip/commit/94c6507c363799d) tsitle *2024-12-31 12:55:51*


**MANIFEST.in: Add make.bat**

[59065](https://github.com/tsitle/photofilmstrip/commit/59065f30862a18e) tsitle *2024-12-31 10:42:09*


**Add y-*.sh scripts**

[4daf9](https://github.com/tsitle/photofilmstrip/commit/4daf9af273c5647) tsitle *2024-12-29 19:07:44*


**Fix MS Windows Portable Exe and add build target 'sdist_interpreterportzip'**

[aa11e](https://github.com/tsitle/photofilmstrip/commit/aa11e778685dae2) tsitle *2024-12-29 12:25:20*


**ActionI18N.py: Add search path for locales**

[c9777](https://github.com/tsitle/photofilmstrip/commit/c977772c820a6ac) tsitle *2024-12-26 17:21:14*


**Update build stuff (Makefiles and setup.py)**

[bdbd5](https://github.com/tsitle/photofilmstrip/commit/bdbd559d5d7f9d7) tsitle *2024-12-26 17:21:06*


**setup.py: Rename build targets and classes for WinPortable***

[4875d](https://github.com/tsitle/photofilmstrip/commit/4875d6a19a9f80a) tsitle *2024-12-25 19:37:16*


**setup.py: Update support for GStreamer in WinPortableExe**

[565b4](https://github.com/tsitle/photofilmstrip/commit/565b4f218ee71f0) tsitle *2024-12-25 19:26:13*


**requirements_dev.txt: Remove cx_freeze**

[bafe1](https://github.com/tsitle/photofilmstrip/commit/bafe11918bf8ca3) tsitle *2024-12-25 19:23:10*


**ArtProvider.py: Replace wx.svg with cairosvg**

[bc8d7](https://github.com/tsitle/photofilmstrip/commit/bc8d7f2e9efc3f1) tsitle *2024-12-25 19:22:32*


**Update Makefiles to use virtualenv**

[355b9](https://github.com/tsitle/photofilmstrip/commit/355b9aa0dec88a6) tsitle *2024-12-19 13:33:43*


**util.py: Add more search paths for docs and data**

[02cb9](https://github.com/tsitle/photofilmstrip/commit/02cb93d81dc43cc) tsitle *2024-12-19 13:31:38*


**PILBackend.py: Small improvements**

[e7ac4](https://github.com/tsitle/photofilmstrip/commit/e7ac449d77c420c) tsitle *2024-12-19 12:08:19*


**PILBackend.py: Fix uninitialized variables**

[c06f4](https://github.com/tsitle/photofilmstrip/commit/c06f48ec3a6875e) tsitle *2024-12-19 12:08:03*


**ActionAutoPath.py: Fix uninitialized variable**

[47b6c](https://github.com/tsitle/photofilmstrip/commit/47b6c700526f22c) tsitle *2024-12-19 12:06:41*


**Update .po* files**

[1aae5](https://github.com/tsitle/photofilmstrip/commit/1aae5ac63f5cf22) tsitle *2024-12-18 17:19:22*


**Change application description**

[8b249](https://github.com/tsitle/photofilmstrip/commit/8b2496d575ef8b0) tsitle *2024-12-18 17:19:21*


**Change application website**

[9816a](https://github.com/tsitle/photofilmstrip/commit/9816a7ff16a21eb) tsitle *2024-12-18 17:19:19*


**Change application authors**

[08738](https://github.com/tsitle/photofilmstrip/commit/08738f8ce541057) tsitle *2024-12-18 17:19:19*


**UpdateChecker.py: Deactivate Update Check**

[bc527](https://github.com/tsitle/photofilmstrip/commit/bc52762b7995aad) tsitle *2024-12-18 17:19:18*


**WxProjectFile.py: Fix language in string**

[dfaf1](https://github.com/tsitle/photofilmstrip/commit/dfaf146df53e635) tsitle *2024-12-18 17:19:16*


**ProjectFile.py: Improve support for replacing image paths**

[d01e3](https://github.com/tsitle/photofilmstrip/commit/d01e31cf9a291bd) tsitle *2024-12-18 17:19:16*


**Add initial support for Python 3.12**

[1840c](https://github.com/tsitle/photofilmstrip/commit/1840ce616f7f545) tsitle *2024-12-18 17:19:15*


## 4.0.0b4 (2024-01-01)

### Other changes

**use native disabled icons within menu bar**

* fixes menubar issues with wxPython-4.2.x 

[8a3fa](https://github.com/tsitle/photofilmstrip/commit/8a3fa37aa4b946d) jensgoe *2024-01-01 22:16:48*

**fixes gnome notifications for finished jobs**


[02cf3](https://github.com/tsitle/photofilmstrip/commit/02cf3e6c6340c0f) jensgoe *2024-01-01 22:15:25*

**update dependencies**

* - cx_freeze 6.15.12 
* - pillow 10.1.0 
* - removed py2exe 
* - enable 32bit and 64bit build 

[464c9](https://github.com/tsitle/photofilmstrip/commit/464c95581ea2161) jensgoe *2023-12-29 12:05:24*


**Merge pull request #110 from PhotoFilmStrip/fix_portrait_resolution**

* fixed output resolution for projects in portrait mode 
* fixes #109 

[cdec0](https://github.com/tsitle/photofilmstrip/commit/cdec0fa69320a23) jensgoe *2023-08-20 06:11:01*

**fixed output resolution for projects in portrait mode**


[98aa4](https://github.com/tsitle/photofilmstrip/commit/98aa40f7f7c0699) jensgoe *2023-08-20 06:09:07*

**use wxPython 4.1.1 due to menu bar issues**


[62a5d](https://github.com/tsitle/photofilmstrip/commit/62a5d1fc80b9b9f) jensgoe *2022-12-28 22:22:24*

**disable python37 build**


[67e02](https://github.com/tsitle/photofilmstrip/commit/67e0208d64c535b) jensgoe *2022-12-25 07:40:02*

**include all typelibs**


[56760](https://github.com/tsitle/photofilmstrip/commit/56760d2ce62c7db) jensgoe *2022-12-25 07:39:49*

**moved forward from deprecated optparse to argparse**


[83ee1](https://github.com/tsitle/photofilmstrip/commit/83ee1a4124f48c2) jensgoe *2022-12-25 07:17:53*

**updated translations from catalog**


[16a6c](https://github.com/tsitle/photofilmstrip/commit/16a6c49853639c4) jensgoe *2022-12-23 14:11:52*

**updated german translation**


[ad8ec](https://github.com/tsitle/photofilmstrip/commit/ad8ecff51772782) jensgoe *2022-12-23 14:11:32*

**updated i18n catalog**


[39beb](https://github.com/tsitle/photofilmstrip/commit/39bebbafb79f714) jensgoe *2022-12-23 14:11:23*

**Merge pull request #108 from PhotoFilmStrip/fixes_story_projects**

* Fixes story projects 
* closes #45 

[ecde2](https://github.com/tsitle/photofilmstrip/commit/ecde2b4ccf0cbe4) jensgoe *2022-12-23 13:58:22*

**Merge pull request #107 from PhotoFilmStrip/portrait_mode**

* Portrait mode 
* closes #74 
* closes #92 

[47089](https://github.com/tsitle/photofilmstrip/commit/47089168911f772) jensgoe *2022-12-23 13:57:15*

**Fix for videos in portrait mode**


[3f3b7](https://github.com/tsitle/photofilmstrip/commit/3f3b707c4fe5683) jensgoe *2022-12-23 13:47:13*

**apply bitrate from selected profile**


[b34a2](https://github.com/tsitle/photofilmstrip/commit/b34a2b38579d812) jensgoe *2022-12-23 12:53:38*

**add setting to adjust level for audio stream**


[04ee1](https://github.com/tsitle/photofilmstrip/commit/04ee102a339605d) jensgoe *2022-12-23 12:16:06*

**double click opens file with system app**


[0aee1](https://github.com/tsitle/photofilmstrip/commit/0aee1b4033c9dcd) jensgoe *2022-12-23 12:12:43*

**CLI considers portrait mode**


[2b109](https://github.com/tsitle/photofilmstrip/commit/2b109e24208e2bb) jensgoe *2022-11-10 22:10:09*

**Refactoring**


[004bd](https://github.com/tsitle/photofilmstrip/commit/004bd490cf1908b) jensgoe *2022-11-10 22:09:24*

**removed unnecessary constructor calls**


[74903](https://github.com/tsitle/photofilmstrip/commit/749030033a22b96) jensgoe *2022-11-10 21:41:12*

**checkbox option for portrait mode**


[790cb](https://github.com/tsitle/photofilmstrip/commit/790cb4fca58d72f) jensgoe *2022-11-10 21:40:22*

**preparation for portrait mode**


[f1327](https://github.com/tsitle/photofilmstrip/commit/f13273166f0e879) jensgoe *2022-11-09 22:37:04*

**pydev project file removed**


[bbc1d](https://github.com/tsitle/photofilmstrip/commit/bbc1d9a4da0f424) jensgoe *2022-06-04 16:04:14*

**Merge pull request #99 from PhotoFilmStrip/fix-issue98**

* fixes #98 

[11294](https://github.com/tsitle/photofilmstrip/commit/11294b3c1c315ab) jensgoe *2022-06-04 16:01:32*

**round floats to int in picture rectangles**


[73106](https://github.com/tsitle/photofilmstrip/commit/731061206927989) jensgoe *2022-06-04 15:53:41*

**round floats to int before passing them to wx-api**


[92630](https://github.com/tsitle/photofilmstrip/commit/92630066b7b7fe2) jensgoe *2022-06-04 15:37:29*

**round floats to int before passing them to wx-api**


[bac22](https://github.com/tsitle/photofilmstrip/commit/bac223cb29a1461) jensgoe *2022-06-04 15:32:47*

**bump year in about dialog**


[937f8](https://github.com/tsitle/photofilmstrip/commit/937f881bf566e10) jensgoe *2022-06-04 14:51:03*

**process dialog result correctly**


[04bb6](https://github.com/tsitle/photofilmstrip/commit/04bb64e60ef5008) jensgoe *2022-06-04 14:51:03*

**build for python 3.9**


[42754](https://github.com/tsitle/photofilmstrip/commit/427541472bbdeb6) jensgoe *2021-11-05 23:26:02*

**updated vm image for azure build**


[8357d](https://github.com/tsitle/photofilmstrip/commit/8357dad945c154c) jensgoe *2021-11-05 23:25:50*

**Merge pull request #97 from PhotoFilmStrip/fix_close_app_keeps_process_running**

* remove deprecated camelCase method isAlive vs is_alive in python39 

[e234d](https://github.com/tsitle/photofilmstrip/commit/e234d694152d7f3) jensgoe *2021-11-04 07:13:29*

**remove deprecated camelCase method isAlive vs is_alive in python39**


[9b73c](https://github.com/tsitle/photofilmstrip/commit/9b73c0b35ff47f7) jensgoe *2021-05-27 06:18:08*

**Merge pull request #94 from PhotoFilmStrip/fix_browse_audio**

* use proper method to retrieve audio files 

[126df](https://github.com/tsitle/photofilmstrip/commit/126dfeb7f43c2cf) jensgoe *2021-02-03 23:12:34*

**use proper method to retrieve audio files**


[1ccfc](https://github.com/tsitle/photofilmstrip/commit/1ccfc1c06ec30a2) jensgoe *2021-02-03 23:10:12*

**set cx_Freeze to 6.4.2**

* issue_875 

[ec686](https://github.com/tsitle/photofilmstrip/commit/ec686a6403aeea3) jensgoe *2021-01-12 22:53:08*

**Added builtin audio file**


[e0150](https://github.com/tsitle/photofilmstrip/commit/e0150771321bfc7) jensgoe *2021-01-10 13:38:35*

**Updated new builtin audio file**


[090fe](https://github.com/tsitle/photofilmstrip/commit/090fe4bec3295a4) jensgoe *2021-01-10 13:32:48*

**Added new builtin audio file**

* arranged by knorke 

[460d6](https://github.com/tsitle/photofilmstrip/commit/460d63656a2d400) jensgoe *2021-01-07 06:43:17*

**Merge pull request #89 from PhotoFilmStrip/configure-audio**

* optimze usability the configure audio dialog 

[a9c2c](https://github.com/tsitle/photofilmstrip/commit/a9c2c9c1d7b8c58) jensgoe *2020-11-24 22:46:27*

**show error if project has invalid/missing audio files when start rendering**


[f1b83](https://github.com/tsitle/photofilmstrip/commit/f1b8354202a29c9) jensgoe *2020-11-21 16:40:47*

**fixing deadlock when playing invalid audio files**


[d23fc](https://github.com/tsitle/photofilmstrip/commit/d23fc4484fc3230) jensgoe *2020-11-21 16:39:58*

**detect svg files correctly**


[ac9c9](https://github.com/tsitle/photofilmstrip/commit/ac9c96dbc1abb84) jensgoe *2020-11-21 16:38:36*

**usability improved**


[b12c5](https://github.com/tsitle/photofilmstrip/commit/b12c50facf31385) jensgoe *2020-11-21 16:38:08*

**only show the basename of the audio files**


[60d94](https://github.com/tsitle/photofilmstrip/commit/60d943759047998) jensgoe *2020-11-21 14:13:51*

**mark project as changed after modifying project audio**

* fixes #87 

[da1eb](https://github.com/tsitle/photofilmstrip/commit/da1ebe49d176f15) jensgoe *2020-11-21 14:12:58*

**fix for bug report dialog**

* fixes #86 

[66b4a](https://github.com/tsitle/photofilmstrip/commit/66b4ac3e8ddab14) jensgoe *2020-11-21 14:12:58*


## 4.0.0b3 (2020-11-18)

### Other changes

**bump version suffix**


[02da1](https://github.com/tsitle/photofilmstrip/commit/02da1a1644da0ed) jensgoe *2020-11-18 21:48:09*

**Merge pull request #85 from PhotoFilmStrip/svg-icons**

* Use SVG format for all icons 

[e761c](https://github.com/tsitle/photofilmstrip/commit/e761c3d9019245e) jensgoe *2020-11-18 21:46:09*

**bump year in about dialog**


[f0abe](https://github.com/tsitle/photofilmstrip/commit/f0abed5817fde69) jensgoe *2020-11-17 23:06:00*

**Merge pull request #84 from PhotoFilmStrip/fix-logging-in-frozen-mode**

* Fix logging in frozen mode 

[0b65d](https://github.com/tsitle/photofilmstrip/commit/0b65d8f6c14f88a) jensgoe *2020-11-17 23:01:12*

**redirect stdout and stderr to logging**


[fe04b](https://github.com/tsitle/photofilmstrip/commit/fe04b98282be950) jensgoe *2020-11-17 23:00:03*

**enable logging to file in frozen mode**


[b5b21](https://github.com/tsitle/photofilmstrip/commit/b5b214d4451f06e) jensgoe *2020-11-17 22:59:28*

**insert pid and thread name in log, set default to level to INFO**


[1cb75](https://github.com/tsitle/photofilmstrip/commit/1cb75a4690ddbe4) jensgoe *2020-11-17 22:58:12*

**removed unused code**


[8b342](https://github.com/tsitle/photofilmstrip/commit/8b34206d014577c) jensgoe *2020-11-16 23:00:03*

**use disabled icon for job queue**


[efdf9](https://github.com/tsitle/photofilmstrip/commit/efdf9aa8fc19a4e) jensgoe *2020-11-16 22:57:27*

**use better icon in dialog**


[c12bb](https://github.com/tsitle/photofilmstrip/commit/c12bba8f1821a6c) jensgoe *2020-11-16 22:43:13*

**fixed syntax error**


[cb17b](https://github.com/tsitle/photofilmstrip/commit/cb17b3fd9b14a0e) jensgoe *2020-11-16 22:43:00*

**removed duplicate files**


[8566a](https://github.com/tsitle/photofilmstrip/commit/8566a55fec8e6e9) jensgoe *2020-11-16 22:39:33*

**pass size to ArtProvider**


[b4367](https://github.com/tsitle/photofilmstrip/commit/b43670248914484) jensgoe *2020-11-16 22:37:34*

**minor improvements**


[17bc1](https://github.com/tsitle/photofilmstrip/commit/17bc1798ab176e1) jensgoe *2020-11-16 22:27:45*

**retrieve icons with updated names**


[896b9](https://github.com/tsitle/photofilmstrip/commit/896b977b1499115) jensgoe *2020-11-16 08:04:03*

**svg files for disabled icons**


[6e10a](https://github.com/tsitle/photofilmstrip/commit/6e10a27bed4a693) jensgoe *2020-11-16 07:39:11*

**app icon as svg**


[a20cd](https://github.com/tsitle/photofilmstrip/commit/a20cd786c0b78a7) jensgoe *2020-11-16 06:49:19*

**ArtProvider can handle svg files**


[04d1d](https://github.com/tsitle/photofilmstrip/commit/04d1d6e7e3234dc) jensgoe *2020-11-16 06:43:25*

**embed images as base64 data**


[f9994](https://github.com/tsitle/photofilmstrip/commit/f9994ed895e6280) jensgoe *2020-11-16 06:42:52*

**fixed double file extension**


[0479b](https://github.com/tsitle/photofilmstrip/commit/0479b62d0595b65) jensgoe *2020-11-15 22:25:57*

**replaced png files with svg files**


[0f8db](https://github.com/tsitle/photofilmstrip/commit/0f8dbc103c46218) jensgoe *2020-11-15 22:25:32*


## 4.0.0b2 (2020-11-04)

### Other changes

**bump version suffix to beta2**


[df3ee](https://github.com/tsitle/photofilmstrip/commit/df3ee8897f248c0) jensgoe *2020-11-04 23:06:31*

**updated german translation**


[9be24](https://github.com/tsitle/photofilmstrip/commit/9be246b5c0aad80) jensgoe *2020-11-04 22:58:57*

**updated gettext catalogs**


[55283](https://github.com/tsitle/photofilmstrip/commit/55283a5d1d7f4f6) jensgoe *2020-11-04 22:58:46*

**fixed typo**


[943c3](https://github.com/tsitle/photofilmstrip/commit/943c3a0df0c322a) jensgoe *2020-11-04 22:58:27*

**updated gettext catalogs**


[f9738](https://github.com/tsitle/photofilmstrip/commit/f9738bfd64235f1) jensgoe *2020-11-04 22:41:13*

**updated old style unicode strings**


[0496d](https://github.com/tsitle/photofilmstrip/commit/0496dcdd9caaba3) jensgoe *2020-11-04 22:25:52*

**azure pipeline**


[d9ed9](https://github.com/tsitle/photofilmstrip/commit/d9ed903dd7fcb50) jensgoe *2020-11-03 22:41:26*

**Merge pull request #83 from PhotoFilmStrip/mpeg2enc_to_avenc**

* replaced mpeg2enc and twolamemp2enc with avenc (libav) 

[92f36](https://github.com/tsitle/photofilmstrip/commit/92f365928cd3ea0) jensgoe *2020-11-03 22:26:49*

**use mpegpsmux as muxer**


[59f01](https://github.com/tsitle/photofilmstrip/commit/59f01eec265c721) jensgoe *2020-11-03 22:23:34*

**updated encoding parameters**


[9b7a8](https://github.com/tsitle/photofilmstrip/commit/9b7a8768d4b7855) jensgoe *2020-11-03 10:09:40*

**replaced mpeg2enc and twolamemp2enc with avenc (libav)**


[80173](https://github.com/tsitle/photofilmstrip/commit/8017325903162fc) jensgoe *2020-10-28 22:53:02*

**replace last GTK dependency with GObject**


[eb394](https://github.com/tsitle/photofilmstrip/commit/eb394d52d9e3932) jensgoe *2020-10-28 22:13:25*

**Merge pull request #82 from PhotoFilmStrip/fix-issue79**

* Fix h265 output format 

[63f06](https://github.com/tsitle/photofilmstrip/commit/63f060db1116c94) jensgoe *2020-10-28 21:58:01*

**use raw text for raw formats if escaping markup fails**


[17264](https://github.com/tsitle/photofilmstrip/commit/17264b9f32f7a22) jensgoe *2020-10-28 21:56:04*

**fix h265 format**

* - use mp4 container instead of matroska (mkv) 
* - use raw text for muxed subtitle within mp4 container 

[4951f](https://github.com/tsitle/photofilmstrip/commit/4951f593e6e052e) jensgoe *2020-10-28 21:55:28*

**Merge pull request #81 from PhotoFilmStrip/fix-issue80**

* upgrading windows build to a recent python version 

[452b9](https://github.com/tsitle/photofilmstrip/commit/452b995b73213eb) jensgoe *2020-10-28 21:51:53*

**building with cx_freeze**

* - including manifest for dpi awareness 
* - currently depends on an already installed Python-Gstreamer library 
* inside the virtualenv 
* - py2exe is still used to add manifest as a resource in the exe file 

[c80f8](https://github.com/tsitle/photofilmstrip/commit/c80f8857ffa635e) jensgoe *2020-10-28 21:43:29*

**prepared changes for cx_Freeze**


[edaa5](https://github.com/tsitle/photofilmstrip/commit/edaa59f9b1d880b) jensgoe *2020-10-28 21:36:54*

**fix strange assertion**

* Python int too large to convert to C long 

[b83d5](https://github.com/tsitle/photofilmstrip/commit/b83d581ca2c2cc4) jensgoe *2020-10-28 21:14:28*

**use generic python interpreter in pydev project properties**


[c1e63](https://github.com/tsitle/photofilmstrip/commit/c1e63788b8eb467) jensgoe *2020-10-28 21:13:16*

**determine real python if inside venv**


[e636a](https://github.com/tsitle/photofilmstrip/commit/e636ad08a0939ce) jensgoe *2020-10-28 21:12:24*

**Fix for runing with wxPython4.1**


[a3c6f](https://github.com/tsitle/photofilmstrip/commit/a3c6fe11b6f2305) jensgoe *2020-10-05 07:00:33*


## 4.0.0b1 (2020-02-12)

### Other changes

**bump version suffix**


[028bb](https://github.com/tsitle/photofilmstrip/commit/028bb1ded6e3200) jensgoe *2020-02-12 22:33:24*

**Merge pull request #73 from PhotoFilmStrip/fix-issue72**

* set initial size for some dialogs 

[44ce7](https://github.com/tsitle/photofilmstrip/commit/44ce7a120859598) jensgoe *2020-02-12 22:26:14*

**set initial size for some dialogs**


[b25be](https://github.com/tsitle/photofilmstrip/commit/b25beae9cedf465) jensgoe *2020-02-12 22:19:52*

**Merge branch 'story-guide'**


[a3a91](https://github.com/tsitle/photofilmstrip/commit/a3a91c4bb43fef1) jensgoe *2020-02-12 21:36:53*

**Merge pull request #71 from PhotoFilmStrip/fix-issue70**

* use own cursor for moving rectangle 

[ed795](https://github.com/tsitle/photofilmstrip/commit/ed795e764a317c7) jensgoe *2020-02-02 13:00:28*

**Merge pull request #69 from PhotoFilmStrip/mux_subtitle**

* mux subtitles into resulting video container 

[9b7e5](https://github.com/tsitle/photofilmstrip/commit/9b7e5ff9f8d196c) jensgoe *2020-02-02 12:49:50*

**key for subtitle settings changed and docs updated**


[ba124](https://github.com/tsitle/photofilmstrip/commit/ba124c3a7f75dd7) jensgoe *2020-02-02 12:43:14*

**use own cursor for moving rectangle**


[a9785](https://github.com/tsitle/photofilmstrip/commit/a9785357ba542cc) jensgoe *2020-02-02 08:59:42*

**feed subtitle directly to muxer if it is supported**


[aa6c0](https://github.com/tsitle/photofilmstrip/commit/aa6c0dabc344290) jensgoe *2020-02-02 07:16:21*

**let subtitle file exist before renderer get prepared**


[6060c](https://github.com/tsitle/photofilmstrip/commit/6060c29ea809fe5) jensgoe *2020-01-30 21:25:15*

**added capability for subtitle encoder**


[8fb7d](https://github.com/tsitle/photofilmstrip/commit/8fb7d0566dbc535) jensgoe *2020-01-30 20:48:03*

**Merge pull request #67 from PhotoFilmStrip/fix-issue66**

* Fix issue66 (closes #66) 

[4bf78](https://github.com/tsitle/photofilmstrip/commit/4bf78906f9243b4) jensgoe *2020-01-29 19:54:16*

**call gi.require_version for Pango**


[b5977](https://github.com/tsitle/photofilmstrip/commit/b59773343fa8ac0) jensgoe *2020-01-29 19:52:17*

**fixed handling of not well formatted subtitle in pango markup**

* check subtitle text with pango parser before passing to gestreamer. 
* if it is not well formed escape the text. 

[7264a](https://github.com/tsitle/photofilmstrip/commit/7264a977c7f9f6e) jensgoe *2020-01-29 19:51:47*

**fixed colors in format combobox**


[b9c8a](https://github.com/tsitle/photofilmstrip/commit/b9c8a5d1f295d37) jensgoe *2020-01-29 16:07:32*

**fixed wrong missing coding message**


[b08a3](https://github.com/tsitle/photofilmstrip/commit/b08a35cb394a974) jensgoe *2020-01-29 16:07:32*

**minor optimizations for player class**


[3569e](https://github.com/tsitle/photofilmstrip/commit/3569ed5955d02bc) jensgoe *2020-01-29 16:07:32*

**Merge pull request #58 from jmespadero/patch-1**

* Draw rule of thirds guides in rectangle editor 

[4cf1d](https://github.com/tsitle/photofilmstrip/commit/4cf1dac58e7f1df) jensgoe *2020-01-29 10:19:55*

**Merge pull request #64 from PhotoFilmStrip/fix-issue63**

* lang.install does not need unicode flag anymore 

[a7b1c](https://github.com/tsitle/photofilmstrip/commit/a7b1c1cf6f3aef0) jensgoe *2020-01-29 10:09:23*

**lang.install does not need unicode flag anymore**


[42ad7](https://github.com/tsitle/photofilmstrip/commit/42ad75a604f4075) jensgoe *2020-01-29 10:07:35*

**Merge pull request #62 from PhotoFilmStrip/fix-issue48**

* fix wrong subtitle order when rendering into video 

[e7fbf](https://github.com/tsitle/photofilmstrip/commit/e7fbf5d9a7f0943) jensgoe *2019-12-30 06:39:21*

**fix wrong subtitle order when rendering into video**


[4af3e](https://github.com/tsitle/photofilmstrip/commit/4af3eb94dc9b501) jensgoe *2019-12-30 06:35:28*

**Merge pull request #60 from jmespadero/patch-2**

* Fix. Avoid crash if dirname is empty 

[7804a](https://github.com/tsitle/photofilmstrip/commit/7804a9f5e000c9d) jensgoe *2019-12-04 11:51:38*

**Fix. Avoid crash if dirname is empty**

* Add a check to avoid execute &#x60;os.makedirs(dirname)&#x60; when dirname is empty. 

[123e0](https://github.com/tsitle/photofilmstrip/commit/123e087ec43ea5b) jmespadero *2019-11-28 11:25:46*

**Draw rule of thirds guides in rectangle editor**

* Draw guides inside the rectangle to implement the [rule of thirds](https://en.wikipedia.org/wiki/Rule_of_thirds) in the editor 
* ![See in action](https://i.stack.imgur.com/7poW8.png) 

[36e24](https://github.com/tsitle/photofilmstrip/commit/36e24f227e4c99e) jmespadero *2019-11-22 17:22:28*

**Merge pull request #57 from fahrstuhl/PFS-3.7.x**

* adds 16:10 aspect ratio 
* (cherry picked from commit 7399e2c7e17e57e742849d60001bcc8404a92a59) 

[15f57](https://github.com/tsitle/photofilmstrip/commit/15f57ef1c141ea6) jensgoe *2019-11-20 08:48:14*

**updates for CI builds**

* - last wxPython for py34 is 4.0.6 
* - wxPython depends on numpy, fixed version for py34 
* - py2exe 

[663b6](https://github.com/tsitle/photofilmstrip/commit/663b66f24f2ddeb) jensgoe *2019-10-31 17:51:44*

**Merge pull request #54 from PhotoFilmStrip/fix-issue-53**

* Fix issue #53 

[d087c](https://github.com/tsitle/photofilmstrip/commit/d087c56538df0fa) jensgoe *2019-10-23 07:49:24*

**online help for PhotoFilmStory**


[2a0e5](https://github.com/tsitle/photofilmstrip/commit/2a0e58afeb9e86a) jensgoe *2019-10-22 19:52:18*

**check if wxLocale can be set in specific language**


[b4670](https://github.com/tsitle/photofilmstrip/commit/b4670256af8ec07) jensgoe *2019-05-29 15:48:13*

**Merge pull request #50 from PhotoFilmStrip/sample_music**

* provide sample music (#49) 

[4315d](https://github.com/tsitle/photofilmstrip/commit/4315d07b0512396) jensgoe *2019-05-28 22:02:31*

**more typelibs for GTK stuff needed**


[44bf5](https://github.com/tsitle/photofilmstrip/commit/44bf54b7a723e64) jensgoe *2019-05-28 21:49:46*

**initialize wxLocale in specific language**


[02f3c](https://github.com/tsitle/photofilmstrip/commit/02f3c90a64c1c90) jensgoe *2019-05-28 21:27:16*

**provide sample music (#49)**

[e9d41](https://github.com/tsitle/photofilmstrip/commit/e9d416f86e6787c) jensgoe *2019-05-28 20:26:17*

**display 100 characters of job results in debug output**


[4f32a](https://github.com/tsitle/photofilmstrip/commit/4f32aae0eafd723) jensgoe *2019-04-16 21:49:32*

**Compose slide shows, video clips and sound tracks to a PhotoFilmStory**

* introduced new project type &#x27;Story&#x27; 
* use GES to render and preview Story project 
* reuse of RenderDialog for Story project 
* Make sure a GTK mainloop is running all time 
* unittests for geometry classes 

[9f802](https://github.com/tsitle/photofilmstrip/commit/9f802896491e7a6) jensgoe *2019-04-16 21:47:35*


## 4.0.0a1 (2019-04-16)

### Other changes

**action callbacks in gnome notification works**


[761af](https://github.com/tsitle/photofilmstrip/commit/761af87ac488246) jensgoe *2019-04-12 22:05:43*

**minor fixes to czech translation**


[bef9e](https://github.com/tsitle/photofilmstrip/commit/bef9e7e5c91b462) jensgoe *2019-02-19 21:48:03*


## 3.7.2 (2019-02-19)

### Other changes

**localization catalogs updated**


[76f68](https://github.com/tsitle/photofilmstrip/commit/76f6835d06ce7bb) jensgoe *2019-02-19 16:52:02*

**czech translation updated**


[1e646](https://github.com/tsitle/photofilmstrip/commit/1e6463e9f9b5c23) jensgoe *2019-02-19 16:49:48*


## 3.7.1 (2019-01-20)

### Other changes

**use correct muxer when rendering MP4 format (closes #44)**


[13273](https://github.com/tsitle/photofilmstrip/commit/13273a4814583cd) jensgoe *2019-01-16 10:00:01*

**include font config in the windows release (closes #42)**


[626c4](https://github.com/tsitle/photofilmstrip/commit/626c44409085731) jensgoe *2018-11-25 17:30:08*
