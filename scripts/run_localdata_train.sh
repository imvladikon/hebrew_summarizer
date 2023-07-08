#!/bin/bash
python3 -m hebrew_summarizer.cli \
    --model_name_or_path "google/mt5-small" \
    --do_train \
    --do_eval \
    --train_file "../data/train.csv" \
    --validation_file "../data/val.csv" \
    --output_dir "../models" \
    --text_column "article" \
    --summary_column "highlights" \
    --per_device_train_batch_size=4 \
    --per_device_eval_batch_size=4 \
    --overwrite_output_dir \
    --predict_with_generate \
    --load_best_model_at_end \
    --save_total_limit 2 \
    --save_strategy "steps" \
    --evaluation_strategy "steps" \
    --save_steps 2000 \
    --logging_steps 2000