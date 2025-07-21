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




