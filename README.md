# Name-ly API

## What is Name-ly?
Welcome to Name-ly! Yes, this app generated its own name!

I'll take your through a short quiz and give you a list of awesome, unique names. Whether you're at a loss while creating a Dungeons and Dragons character, or if you're looking for some unique options to name your child, give it a try at https://name-ly.herokuapp.com/.

## Name-ly API
If you need names or words generated through a Markov model, this microservice might be able to help. Currently, it produces names and it takes in four parameters: 'nameNumber' 'gender', 'culture' and 'literary'. These are named for the types of influences requested of the user in their submitted form.  

### 'nameNumber'
This parameter is an integer. It describes the number of names produced every time the API is run. Please be aware that while I work on more efficient scaling, the app moves very slowly if you request more than 100 names.

### 'gender'
This parameter is a string. It takes 'feminine', 'masculine' or 'unisex' as input. It only takes one value at a time. Any other values will result in a 500 error.

### 'culture'
This parameter is a string. It takes 'American', 'German' or 'Latin' as input. It only takes in one value at a time. Any other value will result in a 500 error.

### 'literary'
This parameter is a string. It takes 'modern', 'classic' or 'fantasy' as input. It only takes in one value at a time. Any other value will result in a 500 error.

## Using the API
To use the api, you can send a POST request (e.g. with POSTMAN, as a query string) to the root route (http://127.0.0.1:5000) as JSON. In the name-ly app, a POST request is sent via Axios from the Node application.

## Demonstration
To see this API at work, check out https://name-ly-api.herokuapp.com/api for JSON values or https://name-ly-api.herokuapp.com/index for a web template with results.

To run the app locally, after cloning this repo and running your virtual environment the app can be viewed at http://127.0.0.1:5000/api or http://127.0.0.1:5000/index to see JSON or a web template respectively.

## Testing
[WIP] This API uses Pytest for testing.

#### Contributor(s): Faith Chikwekwe 👩🏾‍💻 Please feel free to reach out or open an issue if you have any questions. 
