# slackbot-dm-users
I wrote this project to reduce the amount of messaging we were having to do with users
that were still outstanding during compliance checks and tech rollouts. The challenges
I found when I was initially writing this was, while many projects had bots that would
message to channel, none tackled the issue of messaging directly to the user. We felt this
would be a better approach due to the increased privacy, and user engagement of the messages.
In my opinion, this also allows multiple technicians to handle users evenly across time zones
without the chaos of keeping up with a general channel and users would feel more accountable to
answer the message instead of just another channel to ignore. 

In order to resolve this issue, I leveraged the lookupByEmail call in Slack to pull userIDs into
a list and then use them as the channel ID to send a postMessage call. Since emails are often
the unique identifier used to manage user objects in SaaS apps, it made perfect sense to populate
a list using a csv file and then feed that list to Slack to get the user values needed for the messenger.

Another interesting challenge was getting around the Slack API limitation of sending to multiple channels at once.
This required the use of a reiterative loop to pass each userID to the postMessage request in sequence.

You will notice that I chose to keep each function in its own file. The reasoning for this is that I can see each 
of these functions being usable in other useful ways in the future and wanted to maintain modularity of the functions.

It is my hope that anyone that has a similar problem is able to use this with minimal tweaking. 
I added notes to the code to make things as clear as possible, even for beginners or people that are not interested in analyzing the code. 
I also invite any notes or criticism of my code. This was a fun and useful project that started simply and morphed to be
modestly complex.
