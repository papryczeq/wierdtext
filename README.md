# WierdText
Simple text encoder and decoder.

## Setup
Clone repo.

    cd wierdtext/

## Available parameters

    --mode {encode,decode}  #Choose between encoding and decoding text - required
    --text TEXT             #The text to be processed
    --file FILE             #Path to file with text to be processed

## Sample run

    python main.py --mode encode --text "Some awesome top secret message"
    python main.py --mode decode --file example_file_to_decode.txt 

## Testing

    python -m unittest test

## Api testing

    pip install fastapi
    uvicorn api:app --reload

Then open in browser: http://127.0.0.1:8000/docs