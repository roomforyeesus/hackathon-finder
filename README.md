# hackathon-finder

## Inspiration
When I was looking for my first hackathon to participate in, I also found an API called Kontest, and they have up to date hackathon information. 
So I thought how perfect! I will build a hackathon-finder for my first hackathon.
## What it does
 It displays all the current hackathons and if they have started or not and if you leave your email you'll get an email notification every other day for any hackathons beginning in the next 24 hour!
## How I built it
This was built ultilizing Svelte as the frontend, and Django as the backend. I used Django as an rest api, and orm to save user data to database.
I used python to automate the confirmation emails, emailing the subscriber list every other day if there are any hackathons that match the criterias.
## Challenges I ran into
It was a challenge to display the time data from the api because there were different formats and I didn't have enough time to figure out how to display the start and end dates properly after the query.
## What I learned
I learned a lot about svelte since it was my first time working with this framework but i already love it and the courier api is pretty useful, and
it can actually connect a wide variety of apis which is nice because it saves you from going in your application and replacing your keys, and it sort of give you an interface to do some automations and things with the apis you connect. I also learned more about authorizations avaliable on Django and if it's usable in production.
## What's next for hackathon finder?
I am not sure, but I will keep working on it if people end up finding it useful
