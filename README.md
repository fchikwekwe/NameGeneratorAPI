# Name-ly API

## What is Name-ly?
**Description Here**

This API processes submitted form data from Name-ly application through a Markov chain and returns results.

## Demonstration
To see this API at work, check out https://name-ly-api.herokuapp.com/api for JSON values or https://name-ly-api.herokuapp.com/index for a web template with results.

To run the app locally, after cloning this repo and running your virtual environment the app can be viewed at http://127.0.0.1:5000/api or http://127.0.0.1:5000/index to see JSON or a web template respectively.

To use the api, you can send a POST request (e.g. with POSTMAN, as a query string) to the root route (http://127.0.0.1:5000) as JSON. It takes in four parameters: 'nameNumber' 'gender', 'culture' and 'literary'. These are named for the types of influences requested of the user in their submitted form.  

## Testing
[WIP] This API uses Pytest for testing.

#### Contributor(s): Faith Chikwekwe 👩🏾‍💻
