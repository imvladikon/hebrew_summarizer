
## Summarization Experiments for Hebrew

This directory contains examples for finetuning and evaluating transformers on summarization  tasks.
Based on the [HuggingFace Transformers](https://github.com/huggingface/transformers/tree/main/examples/pytorch/summarization) examples.

## Installation

To install the requirements for this example, run:

```bash
pip install -r requirements.txt
```

For development:
```bash
pip install -r requirements-dev.txt
```

## Training

Here is an example on a summarization task:

```bash
python -m summarizer.cli \
    --model_name_or_path "google/mt5-small" \
    --do_train \
    --do_eval \
    --dataset_name <dataset_name> \
    --dataset_config <dataset_config> \
    --source_prefix "summarize: " \
    --output_dir <output_dir_for_checkpoints> \
    --per_device_train_batch_size=4 \
    --per_device_eval_batch_size=4 \
    --overwrite_output_dir \
    --predict_with_generate
```

**Note: only T5 models `t5-small`, `t5-base`, `t5-large`, `t5-3b` and `t5-11b` must use an additional argument: `--source_prefix "summarize: "`.**

### Resume training

To resume training from a checkpoint, you can use the `--resume_from_checkpoint` argument. 
Which is optional, if not specified, in case of `--overwrite_output_dir` is set, the latest checkpoint in the output directory will be used.

### Using local data

For using local data, you can use the `--train_file` and `--validation_file` arguments. 
And need to specify the  `--text_column` and `--summary_column`, example:

```bash
python -m summarizer.cli \
    --model_name_or_path "google/mt5-small" \
    --do_train \
    --do_eval \
    --train_file <path_to_csv_or_jsonlines_file> \
    --validation_file <path_to_csv_or_jsonlines_file> \
    --source_prefix "summarize: " \
    --output_dir <output_dir_for_checkpoints> \
    --overwrite_output_dir \
    --per_device_train_batch_size=4 \
    --per_device_eval_batch_size=4 \
    --predict_with_generate
```

The task of summarization supports custom CSV and JSONLINES formats.

#### Custom CSV Files

If it's a csv file the training and validation files should have a column for the inputs texts and a column for the summaries.

If the csv file has just two columns as in the following example:

```csv
text,summary
"I'm sitting here in a boring room. It's just another rainy Sunday afternoon. I'm wasting my time I got nothing to do. I'm hanging around I'm waiting for you. But nothing ever happens. And I wonder","I'm sitting in a room where I'm waiting for something to happen"
"I see trees so green, red roses too. I see them bloom for me and you. And I think to myself what a wonderful world. I see skies so blue and clouds so white. The bright blessed day, the dark sacred night. And I think to myself what a wonderful world.","I'm a gardener and I'm a big fan of flowers."
"Christmas time is here. Happiness and cheer. Fun for all that children call. Their favorite time of the year. Snowflakes in the air. Carols everywhere. Olden times and ancient rhymes. Of love and dreams to share","It's that time of year again."
```

The first column is assumed to be for `text` and the second is for summary.

If the csv file has multiple columns, you can then specify the names of the columns to use:

```bash
    --text_column text_column_name \
    --summary_column summary_column_name \
```

For example if the columns were:

```csv
id,date,text,summary
```

and you wanted to select only `text` and `summary`, then you'd pass these additional arguments:

```bash
    --text_column text \
    --summary_column summary \
```

#### Custom JSONLINES Files

The second supported format is jsonlines. Here is an example of a jsonlines custom data file.


```json
{"text": "I'm sitting here in a boring room. It's just another rainy Sunday afternoon. I'm wasting my time I got nothing to do. I'm hanging around I'm waiting for you. But nothing ever happens. And I wonder", "summary": "I'm sitting in a room where I'm waiting for something to happen"}
{"text": "I see trees so green, red roses too. I see them bloom for me and you. And I think to myself what a wonderful world. I see skies so blue and clouds so white. The bright blessed day, the dark sacred night. And I think to myself what a wonderful world.", "summary": "I'm a gardener and I'm a big fan of flowers."}
{"text": "Christmas time is here. Happiness and cheer. Fun for all that children call. Their favorite time of the year. Snowflakes in the air. Carols everywhere. Olden times and ancient rhymes. Of love and dreams to share", "summary": "It's that time of year again."}
```

Same as with the CSV files, by default the first value will be used as the text record and the second as the summary record. Therefore you can use any key names for the entries, in this example `text` and `summary` were used.

And as with the CSV files, you can specify which values to select from the file, by explicitly specifying the corresponding key names. In our example this again would be:

```bash
    --text_column text \
    --summary_column summary \
```

#### Scripts

Check examples in the [scripts](scripts) folder.
To run the script, you can use the following command:

```bash
chmod +x scripts/<script_name>.sh
./scripts/<script_name>.sh
```

## Evaluation

To evaluate a model on a summarization task, you can use the `--do_eval` argument.
Metrics are computed and logged into output_dir. Currently, the following metrics are supported:
`ROUGE` by hugginface (see [here](https://huggingface.co/metrics/rouge) for more details)

## Testing

To generate summaries on a summarization task, you can use the `--do_predict` argument.
Predictions are saved into output_dir as `generated_predictions.txt`.

## Inference

```python
from hebrew_summarizer import HebrewSummarizationPipeline

summarizer = HebrewSummarizationPipeline.from_pretrained("google/mt5-small")
article = """
נחשף התאריך בו תופיע הזמרת הישראלית נועה קירל בחצי הגמר הראשון של האירוויזיון - 9/5/23. קירל הוגרלה לחצי השני של הערב, כלומר השיר יתבצע באחד מהמקומות 8-1.
"""
summarizer(article, min_length=30, max_length=100)
```
