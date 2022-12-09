This project was designed using HTML, CSS, Python, and Flask. I also used JavaScript to create an event listener where, if the user presses the "submit" button for user input, there is music. The API I used was PokeAPI: https://pokeapi.co/ 

All photos of the Pokemon are taken from PokeAPI. The Pokeball submit button was taken from Google, and all music and fonts and cursors are from: 
https://downloads.khinsider.com/game-soundtracks/album/pokemon-x-y 
https://www.cufonfonts.com/font/pokemon-hollow
https://www.cursor.cc/

The Favicon is from the picture from this article: https://www.theverge.com/2019/5/6/18531287/pokemon-neuroscience-visual-cortex-brain-information

My main layout page has no navigation bar and has title blocks as well as a footer that is on every page. I made the body of the website centered. 

In app.py, I have app routes for both random and pokemon. When the user clicks the random button, the function will generate a random number and then the random number will be input into the ID for the API. Then the API will output a random Pokemon. For the user input search, when the user submits their search, the function will grab the name of the pokemon the user input and then get output from the API. I decided to design a search bar and a random button to diversify how the user can interact with the Pokedex, and it will allow users who don't have Pokemon knowledge to learn more. My form validation for user input was ensuring that it was lowercase and then getting rid of whitespace before and after the words.

In helpers.py, I have two lookup functions - one for app route /pokemon and one for app route /random. There is also apology, where I have an HTML page of a Pikachu gif and then two 403 errors that will populate based on whether there is an incorrect input or if the Pokemon does not exist.

Each HTML page - except for index - has music. I also added different cursors to make the page seem more exciting. My index page has a sound when the user clicks the submit button after inputting user input. 

I also tried to import different fonts into /style, but the .woff for Pokemon Hollow doesn't seem to work, and the .mp3s I had for each page weren't being read in /style so I exported them into separate MP3 hosting sites and used linked mp3s instead. 