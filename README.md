# hackathon-finder

## Inspiration
When I was looking for my first hackathon to participate in, I also found an API called Kontest, and they have up to date hackathon information. 
So I thought how perfect! I will build a hackathon-finder for my first hackathon.
## What it does
 It displays all the current hackathons and their upcoming start times and end dates. If you leave your email you'll get an email notification on
 monday, wednesdau and saturday for any hackathons beginning in the next 24 hour!
## How I built it
This was built ultilizing Svelte as the frontend, and Django as the back. I used Django as an rest api, and orm to save user data to database.
I used python to automate the confirmation emails, emailing the subscriber list every monday, wednesday, and saturday if there are any hackathons 
that are starting within 24 hours.
## Challenges I ran into
It was a challenge to make fetch request with a token authorization in django and javascript because something was causing javascript to send the
headers incorrectly. I ultimately decided I will circle back to it if i actually have sensitivate data since it was taking a lot of precious time to
troubleshoot and i started late.
## What I learned
I learned a lot about svelte since it was my first time working with this framework but i already love it and the courier api is pretty useful, and
it can actually connect a wide variety of apis which is nice because it saves you from going in your application and replacing your keys, and it sort of give you an interface to do some automations and things with the apis you connect.
## What's next for Hackathon Finder
Honestly, I am not sure since it's my first hackathon but robably make the table display look better and add sorting if people actually use it
