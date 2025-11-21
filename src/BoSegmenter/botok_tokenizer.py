from botok.tokenizers.sentencetokenizer import sentence_tokenizer
from botok.tokenizers.wordtokenizer import WordTokenizer

def get_segment_spans(segments):
    spans = []
    char_walker = 0
    for segment in segments:
        start = char_walker
        end = char_walker + len(segment)
        spans.append(
            {
                'span': {
                    "start": start,
                    "end": end,
                }
            }
        )
        char_walker += len(segment)
    return spans

def is_valid_segment(segment_text):
    Delimeters = ["༔", "།", "༎",]
    if segment_text[-4:] == "༅། །":
        return False
    elif segment_text[-1] in Delimeters or segment_text.endswith("། "):
        return True
    return False

def get_segments(text: str) -> list[str]:
    segments = []
    current_segment = ""
    tokenizer = WordTokenizer()
    tokens = tokenizer.tokenize(text)
    sentence_tokens = sentence_tokenizer(tokens)
    for sentence_index, sentence_token in enumerate(sentence_tokens):
        sentence_text = ''
        for token in sentence_token['tokens']:
            sentence_text += token["text"]
        current_segment += sentence_text
        if is_valid_segment(sentence_text):
            segments.append(current_segment)
            current_segment = ""
    if current_segment:
        segments.append(current_segment)
    return segments