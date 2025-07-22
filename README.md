# My solution to the tab coding assignment

The solution is a pure Python-based API made with the FastAPI library. There is no database, as the data is provided in JSON files. The solution follows a basic API structure with schemas and routes.

## How to run the application

Make sure you have Python 3.13+ installed on your machine to use this repository.

1. Clone the repository.
   ```
   git clone https://github.com/andrew21-b/TabCodingAssignment.git
   ```

2. Change directory to the repository.
   ```
   cd TabCodingAssignment
   ```
3. Activate the virtual environment.
   ```
   .venv\Scripts\Activate.ps1
   ```
4. Install dependencies.
   ```
   pip install -r requirements.txt
   ```
5. Change directory to the app.
   ```
   cd app
   ```
6. Run the API.
   ```
   fastapi dev main.py
   ```

## Considerations

The development of the application involved some considerations, mostly due to time constraints and the openness of the problem.

For instance, regarding the conversion of currencies for the API response, no direction was given for the exchange rates or where they should come from. Therefore, I took liberties and hardcoded imaginary exchange rates to simulate FX changes in a real system.

Additionally, the number of endpoints was not specified—only one was required. So, for testing purposes and overall completeness that a real system would have, I added extra endpoints, as the modularity of the project is very good.

Lastly, the transactions had timestamps. However, I didn't factor that into my summary calculations, as the focus was to make the calculations as robust as possible.

## Future improvements/performance enhancements

If I had more time, I would have spent more time on the system design of the API.

The data is in a JSON format, which would have been better stored in a database. Since it is already in JSON, a NoSQL database such as MongoDB would have been great for this project, as the ORM would integrate really well and it would have the ability to scale as more data is added. In addition to storage systems, having the storage done through a cloud solution like a storage blob would be great to handle much older data that does not need to be retrieved as often. This leads to a future improvement for performance, which is caching. Since the data for the endpoints is being fetched from a data source, in the future this data source would be a database. Therefore, having some sort of cache to sit in front of the database will speed up the retrieval of data for the summary calculation. Another aspect that I didn't have time to implement was security. If this was deployed, making sure there is some rate limiter to stop potential DDoS or brute force attacks would be essential. Additionally, removing or hiding some endpoints behind accounts so that a user cannot see accounts they do not own would be important. For testing, there is no endpoint testing—only the business logic is tested. It would be good to extend the current tests to integrate the API and test networking cases.





# Coding assignment
As part of our selection process, we kindly ask candidates to complete a programming assignment. This will be used to provide a backbone for discussions in one or more of your technical interviews. Writing, reviewing and discussing code will be a big part of most of your days with us so this challenge is intended to provide both you and us with an experience of what it will be like to work with each other. We will be looking for good code quality and design, as well as evidence of good thinking and problem solving ability. Feel free to make any reasonable assumptions - there is no right or wrong answer. 
- We work primarily with Python and FastAPI on the backend, so we always like to see this, but if you feel more comfortable with another language and/or web framework, feel free to use this instead. 
- Please take no longer than 3-4 hours to complete the exercise.
- Please provide the solution as a private Github repository, shared with `tfedawy`, as well as an accompanying readme file with your notes as outlined below.
- The deadline for the task is 7 days from receipt but if this doesn't work for any reason, please let me know as soon as possible.
				
## Objective


We have a list of accounts and a list of transactions from multiple payment service providers, in multiple currencies, provided in the accompanying JSON files. These transactions will either have a status of `settled`, `refunded` or `chargeback`. 
Build a system that will consume the data from these sources, perform some calculations and make the result available in an API endpoint that takes as input an account number and returns the list of transactions grouped by category as well as a total.


For example:
```
// Request:
{ “account_id”: "7299be1b-8506-4702-8eb9-c418761f2dcf"}


// Response:
{
   "account":{
      "name":"TEST ACCOUNT 1",
      "id":"7299be1b-8506-4702-8eb9-c418761f2dcf"
   },
   "transactions":{
      "settled":{
         "GBP":1003000,
         "EUR":200000
      },
      "chargeback":{
         "GBP":100300,
         "EUR":40000
      },
      "refunded":{
         "GBP":104000,
         "EUR":20030
      }
   },
   "balance":{
      "GBP":798700,
      "EUR":139970
   }
}
```


## Considerations
* Good code structure and tests are encouraged
* Provide a ReadMe.md file containing: How to run the application, and considerations that went into it, any future improvements or performance enhancements you would do if you had more time.




