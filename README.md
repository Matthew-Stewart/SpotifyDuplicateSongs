Find All Duplicate Songs In A Playlist
======================================

About
-----
Finds all duplicate tracks in a Spotify playlist.

Use ```-r``` to include duplicate remixes of the same songs.

Register a new Spotify Developer Application on the [Spotify Developer site](https://developer.spotify.com/my-applications).

### Usage
```
main.py user playlist [-r]
```

### Examples
Normal:  
```
python main.py 12131743478 5pav73knYSACPBFyQDknPb
```  
output:  
```
Artist                                 Track
------                                 -----
Aero Chord                             Wanchu Back
Camo & Krooked, Ayah Marar             Watch It Burn
Culture Code, Karra                    Make Me Move
Dan Dakota                             We Let Em Go
Direct                                 So Sure
Disfigure                              Hollah!
Draper, Laura Brehm                    Pressure (feat. Laura Brehm)
Elephante, Nevve                       Catching On (feat. Nevve)
EvenS                                  Coalesce - Original Mix
Fred V & Grafix, Collin McLoughlin     Here With You
Gryffin, Bipolar Sunshine, Faux Tales  Whole Heart - Faux Tales Remix
Kove, Dimension                        Feel Love Again
Matrix & Futurebound                   Control - Edit
NCT                                    Go Back Home
NCT, Veela                             Go Back Home
ODESZA                                 How Did I Get Here
ODESZA, Madelyn Grant                  Sun Models (feat. Madelyn Grant)
ODESZA, Shy Girls                      All We Need (feat. Shy Girls)
ODESZA, Zyra                           Say My Name (feat. Zyra)
Ookay                                  Back Again
Route 94, Jess Glynne                  My Love - Prince Fox Remix
Snail's House                          First Love
Snail's House                          Kirara
Snail's House                          Pixel Dream
```


With remixes:  
```
python main.py 12131743478 5pav73knYSACPBFyQDknPb -r
```  
output:  
```
Artist                                      Track
------                                      -----
3LAU, Bright Lights                         How You Love Me
3LAU, Bright Lights                         How You Love Me - Arston Remix
3LAU, Yeah Boy, Arty                        Is It Love - Arty Remix
3LAU, Yeah Boy, Justin Caruso               Is It Love - Justin Caruso Remix
A R I Z O N A                               Oceans Away
A R I Z O N A, Sam Feldt                    Oceans Away - Sam Feldt Remix
Aero Chord                                  Wanchu Back
Alan Walker                                 Faded
Alan Walker                                 Faded - Instrumental
Alessia Cara                                Scars To Your Beautiful
Alessia Cara, Luca Schreiner                Scars To Your Beautiful - Luca Schreiner Remix
Alina Baraz, Galimatias                     Fantasy
Alina Baraz, Galimatias, Vices              Fantasy - Vices Remix
Aruna, Culture Code                         The End - Culture Code Remix
Aruna, WRLD                                 The End - WRLD Remix
Autograf                                    Heartbeat
Autograf, GRMM                              Heartbeat - GRMM Remix
Camo & Krooked, Ayah Marar                  Watch It Burn
Cartoon, Kristel Aaslaid                    Immortality
Cartoon, Kristel Aaslaid, Futuristik        Immortality - Futuristik Remix
Cash Cash                                   Overtime
Cash Cash, Vicetone                         Overtime - Vicetone Remix Edit
Clean Bandit, Jess Glynne                   Real Love
Clean Bandit, Jess Glynne                   Real Love - The Chainsmokers Remix
Clean Bandit, Louisa Johnson                Tears (feat. Louisa Johnson)
Clean Bandit, Louisa Johnson, Wideboys      Tears (feat. Louisa Johnson) - Wideboys Remix
Culture Code, Karra                         Make Me Move
Culture Code, Tobu, Karra                   Make Me Move - Tobu Remix
Dabin, Daniela Andrade                      Hold feat. Daniela Andrade - Original Mix
Dabin, Fred V & Grafix, Daniela Andrade     Hold feat. Daniela Andrade - Fred V & Grafix Remix
Dabin, Hyper Potions, Daniela Andrade       Hold feat. Daniela Andrade - Hyper Potions Remix
Dabin, Mr FijiWiji, Daniela Andrade         Hold feat. Daniela Andrade - Mr FijiWiji Remix
...
```
