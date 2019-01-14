# Name-ly API

## What is Name-ly?
Welcome to Name-ly! Yes, this app generated its own name!

I'll take your through a short quiz and give you a list of awesome, unique names. Whether you're at a loss while creating a Dungeons and Dragons character, or if you're looking for some unique options to name your child, give it a try at https://name-ly.herokuapp.com/.

## Name-ly API
If you need names or words generated through a Markov model, this microservice might be able to help. Currently, it produces names and it takes in four parameters: 'nameNumber' 'gender', 'culture' and 'literary'. These are named for the types of influences requested of the user in their submitted form.  

### 'nameNumber'
This parameter is an integer. It describes the number of names produced every time the API is run. Please be aware that while I work on more efficient scaling the app works more slowly the more values that you request at once.
### 'gender'
This parameter is a string. It takes 'feminine', 'masculine' or 'unisex' as input. It only takes one value at a time. Any other value will result in a 500 error.

### 'culture'
This parameter is a string. It takes 'American', 'German' or 'Latin' as input. It only takes in one value at a time. Any other value will result in a 500 error.

### 'literary'
This parameter is a string. It takes 'modern', 'classic' or 'fantasy' as input. It only takes in one value at a time. Any other value will result in a 500 error.

## Getting Started
To use the api, you can send a POST request (e.g. with POSTMAN, as a query string) to the root route (http://127.0.0.1:5000 or https://name-ly-api.herokuapp.com/) as JSON. In the name-ly app, a POST request is sent via Axios from the Node application as demonstrated below.
```
axios.post('https://name-ly-api.herokuapp.com/', {
                    nameNumber: 10,
                    gender: quiz.gender.toLowerCase(),
                    cultural: quiz.cultural.toLowerCase(),
                    literary: quiz.literary.toLowerCase(),
                })
```
Full controller with Axios post request can be viewed here: https://github.com/fchikwekwe/name-ly/blob/master/controllers/quizzes.js.

## Demonstration
To see the kinds of results that this API generates, check out https://name-ly-api.herokuapp.com/api for JSON values or https://name-ly-api.herokuapp.com/index for a web template with results.

To run the app locally, after cloning this repo and running your virtual environment the app can be viewed at http://127.0.0.1:5000/api or http://127.0.0.1:5000/index to see JSON or a web template respectively.

## Hosting
This shipped version of the API is currently hosted on Heroku. When you first ping the API, it may take up to 30 seconds for the first result as the app wakes up its service worker. Subsequent pings should not experience any delays.

## Testing
[WIP] Coming soon.

#### Contributor(s): Faith Chikwekwe 👩🏾‍💻 Please feel free to reach out or open an issue if you have any questions.
