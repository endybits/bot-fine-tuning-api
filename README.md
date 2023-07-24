# bot-fine-tuning-api
An example about how we can use Fine-tuning for train chatbot with tailored data for a particular interest.

### Data Preparation
We can preparing the data for train our model using the CLI with thist command:  
`openai tools fine_tunes.prepare_data -f <LOCAL_FILE>`

In my case I replaced `<LOCAL_FILE>` by [aws_dataset.csv]
Some validations:
![image](https://github.com/endybits/bot-fine-tuning-api/assets/22806426/01a27326-b9cc-4e62-8e2c-d90e0c2cd1d2)

Finally was generated the jsonl file [filename]

### Fine-tune model creation
`openai api fine_tunes.create -t <TRAIN_FILE_ID_OR_PATH> -m <BASE_MODEL>`
in may case is 
`openai api fine_tunes.create -t aws_dataset_prepared.jsonl -m davinci`
