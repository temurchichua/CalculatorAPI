# Calculator API
This is first ever collaboration by Unilab Python Dev Team 2021

## Instruction
To run the app remotely run following commands:
```bash
pip install -r requirements.txt
python main.py
```

To test the API Check the [PostMan Documentation](https://documenter.getpostman.com/view/12376335/Tz5v3vVA)

## Methods 
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/f09a9fdc7be3c6955711)

### Name of the Functionality
#### description
small description of the method

#### structure
endpoint: `/function_endpoint/`

return: type | content description


### Calculating Standard Deviation
#### description
Receives a JSON containing a list of numbers (`integers` or `floats`) and calculates Population Standard Deviation of the data.
#### structure
endpoint: `/stddev/`

return: `float` | standard deviation of the data


### პითაგორას ფორმულა
თუ გინდათ რომ მართკუთხ სამკუთხედის ჰიპოთენუზა გაიგოთ ჩაწერეთ მისამართში a და b კათეტები. მაგ.: 
http://127.0.0.1:8080/pythagoras/3&4

### რადიანებში გადაყვანა

**URL:** `{base_url}/to_radians/7`

**Return:** `1/8 იგივე რაც 0.12217304763960307 რადიანები`

## Links

## References
