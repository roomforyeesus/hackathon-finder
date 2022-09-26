# hackathon-finder

##**If you want to run this project** <br>
**note** you need docker + docker compose downloaded for this<br><br>
`git clone <this url>`<br>
`cd hackathon-finder`<br>
`docker-compose build`<br>
`docker-compose up`<br>
navigate to http://127.0.0.1<br><br>
**this is to remove your containers**<br><br>
`docker-compose down`<br><br><br>


## Inspiration
When I was looking for my first hackathon to participate in, I also found an API called Kontest, and they have up to date hackathon information. 
So I thought how perfect! I will build a hackathon-finder for my first hackathon.
## What it does
 It displays all the current hackathons plus if they have started or not and if you leave your email you'll get an email notification and/or text every other day for any hackathons beginning in the next 24 hour!
## How I built it
This was built ultilizing Svelte as the frontend, and Django as the backend. I used Django as an rest api, and orm to save user data to database.
I used python to automate the confirmation emails, emailing the subscriber list every other day if there are any hackathons that match the criterias.
## Challenges I ran into
It was a challenge to work with django's autorization using svelte. There was an issue where my headers with the token was being sent incorrectly by javascript to django. I just stuck with no authorization for the moment to build the app
## What I learned
I learned a lot about svelte since it was my first time working with this framework but i already love it and the courier api is pretty useful.
it can actually connect a wide variety of apis which is nice because it saves you from going in your application and replacing your keys, and it sort of give you an interface to do some automations and things with the apis you connect. I also learned more about authorizations avaliable on Django and which ones are useable in production.
## What's next for hackathon finder?
I am not sure, but I will keep working on it if i can think of new features or if people end up finding it useful
