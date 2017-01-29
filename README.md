ProductivityPal tm

An application to quantify your productivity level and compare it with other developers.


Feature list:
- Automated repo detection

- Counts lines of code written via git

- Counts wpm, words written, and other metrics like whatpulse.

-Detects focused window to detect IDE/program used 
(for filtering by wpm written in ide) etc.

-Detects websites visited and whether they are productive/unproductive
(machine learning trained on 'productive' and 'unproductive' data)

-Compare productivity with others in your company/network and see 
what percentile you are in!


Client:
Monitors productivity, uploads productivity data to server

Server:
compares productivity data between users, rankings

JSON transfer format for a data upload to the server (must authenticate with the server first):

{
    'time_start': sometimestamp,
    'time_end': sometimestamp,
    'window_intervals': [{url: url, time_productive: timedelta, time_total: timedelta},...]
    'git_intervals': [{url: remoterepourl, time_productive: timedelta, time_total: timedelta, lines: int, words: int},...]
}