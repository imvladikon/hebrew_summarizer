#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, SummarizationPipeline


class HebrewSummarizationPipeline(SummarizationPipeline):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        return super().__call__(*args, **kwargs)

    @classmethod
    def from_pretrained(self, *args, **kwargs):
        model = AutoModelForSeq2SeqLM.from_pretrained(*args, **kwargs)
        tokenizer = AutoTokenizer.from_pretrained(*args, **kwargs)
        return self(model=model, tokenizer=tokenizer)

    def fit(self, *args, **kwargs):
        raise NotImplementedError("training is not implemented for this pipeline, please use the `cli` for training")


if __name__ == '__main__':
    summarizer = HebrewSummarizationPipeline.from_pretrained("google/mt5-small")
    article = """
        איינשטיין נולד ב-14 במרץ 1879 בעיר אולם, שהייתה בממלכת וירטמברג שבקיסרות הגרמנית (כיום במדינת באדן-וירטמברג), למשפחה יהודית – פאולינה לבית קוך והרמן, בעל מפעל אלקטרוכימי קטן שכשל בעסקיו. שישה שבועות לאחר לידתו, עברה משפחתו להתגורר במינכן שבבוואריה בשל עסקי האב.[1] בגיל חמש חלה, וכדי לשמח את לבו התקין עבורו אביו מצפן פשוט. כבר אז, כך סיפר כעבור שנים, החל לחקור את צפונות חוקי הטבע. בסתיו של 1885 החל ללמוד בבית ספר עממי קתולי, כילד יהודי יחיד בכיתתו, והחל גם ללמוד לנגן בכינור. במקביל הוא קיבל חינוך יהודי בביתו, ותקופת מה נמשך לדת והיה מתפלל בסתר, מחבר מנגינות לכבוד אלוהים, ואף שמר כמה מצוות.
    """
    print(summarizer(article, min_length=5, max_length=20))
